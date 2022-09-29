"""Check the snap shots for the following code"""


import os,csv,sys,time
import tracemalloc

tracemalloc.start(10)


#.....Program starts.............

array_1 = [1] * (10 ** 6)
array_2 = [2] * (2 * 10 ** 8)

#........Program ends...............

#getting the current , peak stack trace
current, peak =  tracemalloc.get_traced_memory()
print(f"Total memory consumed {peak/1024 ** 2} MB") # converting to MB


snapshot = tracemalloc.take_snapshot()
top_stats = snapshot.statistics('lineno')


#summary report
for stat in top_stats:
    print(stat)