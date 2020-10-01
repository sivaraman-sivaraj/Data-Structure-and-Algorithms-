import random
import time


"Creating the test data"
Array_list = list()
for _ in range(10000):
    temp = random.randint(0, 10000)
    Array_list.append(temp)

"Merge sort Algorithm"

def merge(left, right):
    result = []
    i,j = 0,0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while (i < len(left)):
        result.append(left[i])
        i += 1
    while (j < len(right)):
        result.append(right[j])
        j += 1
    # print('merge: ' + str(left) + '&' + str(right) + ' to ' +str(result))
    return result

def merge_sort(L):
    # print('merge sort: ' + str(L))
    if len(L) < 2:
        return L[:]
    else:
        middle = len(L)//2
        left = merge_sort(L[:middle])
        right = merge_sort(L[middle:])
        return merge(left, right)
    
    
    





trial = list()
for _ in range(100):
    "Creating the test data"
    Array_list = list()
    for _ in range(10000):
         temp = random.randint(0, 10000)
         Array_list.append(temp)
        
    
    n = len(Array_list)
    start_merge = time.time()
    sorted_list_merge = merge_sort(Array_list)
    stop_merge = time.time()
    run_time_m = stop_merge - start_merge
    trial.append(run_time_m)

print(trial)


# start_merge = time.time()
# sorted_list_merge = merge_sort(Array_list)
# stop_merge = time.time()
# run_time_m = stop_merge - start_merge
# print("Total time has taken by Merge sort Algorithm (in seconds):", run_time_m)











