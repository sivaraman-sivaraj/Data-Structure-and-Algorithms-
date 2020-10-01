import random
import time


"Creating the test data"
Array_list = list()
for _ in range(10000):
 temp = random.randint(0, 10000)
 Array_list.append(temp)





"Bubble Sort Algorithm"
def bubble_sort(L):
     swap = False
     while not swap:
         swap = True
         for j in range(1, len(L)):
             if L[j-1] > L[j]:
                 swap = False
                 temp = L[j]
                 L[j] = L[j-1]
                 L[j-1] = temp
     return L





trial = list()
for i in range(15):
    "Creating the test data"
    Array_list = list()
    for _ in range(10000):
         temp = random.randint(0, 10000)
         Array_list.append(temp)
        
    
    n = len(Array_list)
    start_merge = time.time()
    sorted_list_merge = bubble_sort(Array_list)
    stop_merge = time.time()
    run_time_m = stop_merge - start_merge
    trial.append(run_time_m)
    print(i)
print(trial)







# start_bubble = time.time()
# sorted_list_bubble = bubble_sort(Array_list)
# stop_bubble = time.time()
# run_time_b = stop_bubble - start_bubble
# print("Total time has taken by Bubble sort Algorithm (in seconds):", (run_time_b
# ))
