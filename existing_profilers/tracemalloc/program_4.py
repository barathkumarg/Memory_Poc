'''

traceback.format method to find the lines in the program
where memory spikes occured

'''

import tracemalloc
import os
tracemalloc.start(10)

#.......Program starts............


l1 = [i for i in range(10)]
l2 = [i for i in range(50)]
l4 = [i for i in range(50)]
l3 = [i for i in range(10)]

snapshot = tracemalloc.take_snapshot()
top_stats = snapshot.statistics('traceback')

stat = top_stats[0]
print("%s memory blocks: %.1f KiB" % (stat.count, stat.size / 1024))
for line in stat.traceback.format():
    print(line)



