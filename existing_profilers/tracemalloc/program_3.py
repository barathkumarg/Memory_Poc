""" Here the program for taking the snapshots and """


import tracemalloc

tracemalloc.start(25)

#.....Program starts ...........

l1 = [i for i in range(100)]
l2 = [i for i in range(500)]
snapshot1 = tracemalloc.take_snapshot()
print("SNAP-SHOT 1")

for stat in snapshot1.statistics("traceback"):
    print(stat)

#erasing the trace indirectly deleting the resudials
tracemalloc.clear_traces()

l2 = [i for i in range(1000)]
l3 = [i for i in range(100)]
snapshot2 = tracemalloc.take_snapshot()
print("SNAP-SHOT 2")

for stat in snapshot2.statistics("traceback"):
    print(stat)
#..........Program ends ............

print("SNAP-SHOT Difference")
#comparing the snapshots
stats = snapshot2.compare_to(snapshot1,'traceback')
for stat in stats:
    print(stat)

tracemalloc.stop()

