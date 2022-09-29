from logger import *
from multiprocessing import *
import os,threading
import traceback
import psutil
import os,time,inspect
import datetime


# Shared variable dictionary
dict_ = Manager().dict()

#Custom Exception class
class MemoryExceedException(Exception):
    """Memory Exceed Custom Exception"""
    pass


#Dependencies involved in the Memory
class Memory_monitor(object):



    def __init__(self,name="monitor",size = 100):

        """Initialize the monitor thread name, threshold and starting the monitoring thread"""


        self.SIZE = size  #Default size is 100 MB
        self.key = True
        self.name = name
        self.threshold = 1024 * 1024 * size

        dict_[self.name] = None  # assigning the dict to capture the values

        #starting the monitoring thread
        self.monitor_thread = threading.Thread(target=self.monitor, args=(dict_,))
        self.monitor_thread.start()



    def __call__(self,param_args):
        """Decorator to control and run the monitor thread and actual decorated process"""

        def wrapper(*args):

            dict_[self.name] = os.getpid() # defining here the process id

            #actual program starts
            param_args(*args)
            #actual program ends

            dict_.pop(self.name) # popping the dict after finishing the process

            self.monitor_thread.join() # Join the monitor thread

        return wrapper



    def calculate_memory(self,p_id):

        """Memory calculation and the threshold check happens in this function"""

        if not p_id:
            return 0
        try:
            main_process = psutil.Process(p_id)
        except Exception as e:
            dict_.pop(self.name)
            return

        memory=main_process.memory_info().rss #appending the parent process memory with resident size set refers to RAM


        #child process check
        child_process = main_process.children(recursive=True)

        for child in child_process:
            if(child!=psutil.Process(os.getpid())): #condition check to exclude the monitor process
                memory+=(child.memory_info().rss)


        #memory logger
        logger.info(f"Process name :{self.name} Memory Consumed: {self.to_mb(memory)} mb")

        if (memory >= self.threshold):  # Memory exceed condition
            raise MemoryExceedException

        return memory



    def to_mb(self,bytes):
        """ Bytes to Mega bytes conversion """
        return round((bytes / 1024.0 ** 2), 3)



    def monitor(self,dict_):
        """Monitor function triggered when the monitor thread is created and does timely check which monitors our memory consumption"""

        try:
            while self.name in dict_: #Internal thread check
                # print(self.monitor_thread.is_alive())
                if (dict_.get(self.name)): # None check
                    logger.info(f"Process name :{self.name} CPU Percentage: {psutil.cpu_percent(interval=0.2, percpu=True)}")
                    logger.info(f"Process name :{self.name} Memory: {psutil.virtual_memory().percent} ")
                    self.calculate_memory(dict_.get(self.name)) # calculate mmemory (mb) via calculate function
                    #logger.info(f"line: {inspect.currentframe().f_back.f_lineno}")

        except MemoryExceedException:
            err_logger.error(f"Process name :{self.name} Memory exceeded then the fixed limit")









