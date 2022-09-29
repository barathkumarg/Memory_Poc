'''
Scenario :  Mainprocess is given some function to execute (no idle condition)
                the monitor thread is also created within the main process at this situation mainprocess manging
                not only the monitor thread but also the function execution given to it so the monitoring approach
                fails at this situation

Note: The manager dict used for process communication creates the actualy pitfall, where it was useful in test_1.py file condition
      but not here as no subprocess or child process is created ih this approach

'''

import multiprocessing
import time
import threading
from Memory_monitor import *
import csv

@Memory_monitor("monitor-2",200)
def func():
    print("array operation started")
    array_1 = [1] * (10 ** 6)

    threads = threading.enumerate()
    # report the name of all active threads
    for thread in threads:
        print(f"{thread.name} - {thread.is_alive()} {thread.ident}")

    array_2 = [2] * (2 * 10 ** 8)
    del array_2
    print("array operation ended")
    # print(os.getpid())
    print("Program completed")

func()
