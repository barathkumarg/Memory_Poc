"""

Check the snap shot memory and
displaying the peak memory consumed in the following program

"""


import tracemalloc
tracemalloc.start(1)
#.......Program starts.........


listOne = [n for n in range(15000)]
listTwo = [n*n for n in range(150000)]
listThree = [n*n*n for n in range(15000)]

#..........Program ends...............


#getting the current , peak stack trace
current, peak =  tracemalloc.get_traced_memory()

print(f"Peak memory in kilobytes : {peak/1024}") # converting to kb

snapshot = tracemalloc.take_snapshot()
top_stats = snapshot.statistics('lineno')

#summary report
for stat in top_stats:
    print(stat)

