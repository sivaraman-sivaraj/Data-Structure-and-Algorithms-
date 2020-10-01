
"""
Created on Thu Sep 17 23:09:37 2020

@author: Sivaraman
"""

import random 
import time

def quicksort(array, start, stop): 
    if(start < stop): 
        pivotindex = partitionrand(array, start, stop) 
        quicksort(array , start , pivotindex) 
        quicksort(array, pivotindex + 1, stop) 
  
 
def partitionrand(array, start, stop): 
    randpivot = random.randrange(start, stop) 
    array[start], array[randpivot] = array[randpivot], array[start] 
    return partition(array, start, stop) 
  

def partition(array,start,stop): 
    pivot = start # pivot 
    i = start - 1
    j = stop + 1
    while True: 
        while True: 
            i = i + 1
            if array[i] >= array[pivot]: 
                break
        while True: 
            j = j - 1
            if array[j] <= array[pivot]: 
                break
        if i >= j: 
            return j 
        array[i] , array[j] = array[j] , array[i]
    return array



trial = list()
for _ in range(100):
    "Creating the test data"
    Array_list = list()
    for _ in range(10000):
         temp = random.randint(0, 10000)
         Array_list.append(temp)
        
    
    n = len(Array_list)
    start_merge = time.time()
    sorted_list_merge = quicksort(Array_list, 0, n-1)
    stop_merge = time.time()
    run_time_m = stop_merge - start_merge
    trial.append(run_time_m)
    
    
print(trial)








# # Driver Code 
# if __name__ == "__main__": 
#     array = [10, 7, 8, 9, 1, 5] 
#     quicksort(array, 0, len(array) - 1) 
#     print(array) 