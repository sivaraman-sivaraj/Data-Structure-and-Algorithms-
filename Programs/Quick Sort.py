import random
import time





def partition(arr, low, high):
    i = (low-1)         # index of smaller element
    pivot = arr[high]     # pivot
 
    for j in range(low, high):
 
        # If current element is smaller than or
        # equal to pivot
        if arr[j] <= pivot:
 
            # increment index of smaller element
            i = i+1
            arr[i], arr[j] = arr[j], arr[i]
 
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return (i+1)

def quickSort(arr, low, high):
    if len(arr) == 1:
        return arr
    if low < high:
 
        # pi is partitioning index, arr[p] is now
        # at right place
        pi = partition(arr, low, high)
 
        # Separately sort elements before
        # partition and after partition
        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)
        
        
        



trial = list()
for _ in range(100):
    "Creating the test data"
    Array_list = list()
    for _ in range(10000):
         temp = random.randint(0, 10000)
         Array_list.append(temp)
        
    
    n = len(Array_list)
    start_merge = time.time()
    sorted_list_merge = quickSort(Array_list, 0, n-1)
    stop_merge = time.time()
    run_time_m = stop_merge - start_merge
    trial.append(run_time_m)
    
    
print(trial)
# print("Total time has taken by Merge sort Algorithm (in seconds):", run_time_m)











