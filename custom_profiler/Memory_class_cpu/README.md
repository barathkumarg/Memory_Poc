Custom Memory Profiler

* A decorator to monitor the memory usage
* Monitor the python code parallely and throws exception when it exceeds the fixed limit specified by the user
* Creating the thread for each decorated function and starting monitoring the function using the created threads
* Logs are generated in timely manner in separate log file
* Memory_monitor.py is the actual class file where the monitor functionality implemented
* logger.py used to generate logs
