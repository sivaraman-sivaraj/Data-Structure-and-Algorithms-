import random
import time


"Creating the test data"
Array_list = list()
for _ in range(10000):
     temp = random.randint(0, 10000)
     Array_list.append(temp)



def insertionSort(array): 
  
    # Traverse through 1 to len(arr) 
    for i in range(1, len(array)): 
  
        key = array[i] 
  
        # Move elements of arr[0..i-1], that are 
        # greater than key, to one position ahead 
        # of their current position 
        j = i-1
        while j >=0 and key < array[j] : 
                array[j+1] = array[j] 
                j -= 1
        array[j+1] = key
    return array
  
  


trial = list()
for i in range(15):
    "Creating the test data"
    Array_list = list()
    for _ in range(10000):
         temp = random.randint(0, 10000)
         Array_list.append(temp)
        
    
    n = len(Array_list)
    start_merge = time.time()
    sorted_list_merge = insertionSort(Array_list)
    stop_merge = time.time()
    run_time_m = stop_merge - start_merge
    trial.append(run_time_m)
    print(i)

print(trial)



# start_insertion = time.time()
# sorted_list_bubble = insertionSort(Array_list) 
# stop_insertion = time.time()
# run_time_b = stop_insertion - start_insertion
# print("Total time has taken by Bubble sort Algorithm (in seconds):", (run_time_b
# ))


# print ("Sorted array is:") 
# for i in range(len(Array_list)): 
#     print ("%d",Array_list[i]) 
    







