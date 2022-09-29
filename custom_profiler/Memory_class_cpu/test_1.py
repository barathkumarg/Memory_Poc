import multiprocessing

from Memory_monitor import *
import csv

# print(f"{os.getpid()} Parent id")

@Memory_monitor("monitor-1",150)
def my_func(a):
    logger.info("file reading started")
    try:
        with open("sample.csv", "r") as f:
            reader = csv.reader(f)
            text =[]

            for i in reader:
                text.append(i)

    except Exception as e:
        print(e)
    logger.info("file reading ended")
    # print(os.getpid())
    print("File Finished")



@Memory_monitor("monitor-2",200)
def func():
    logger.info("array operation started")

    array_1 = [1] * (10 ** 6)
    array_2 = [2] * (2 * 10 ** 8)
    del array_2
    logger.info("array operation ended")
    # print(os.getpid())
    print("Program completed")

@Memory_monitor("monitor-3",20)
def func_1(a):
    j = []
    # print(os.getpid())
    for i in range(1000):
        j.append(i)

process_1 = multiprocessing.Process(target=my_func ,args=(1,))
process_2 = multiprocessing.Process(target=func)
process_3 = multiprocessing.Process(target=func_1, args=(1,))

process_1.start()
process_2.start()
process_3.start()

process_1.join()
process_2.join()
process_3.join()




