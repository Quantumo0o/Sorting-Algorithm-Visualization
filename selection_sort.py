import numpy as np
import matplotlib.pyplot as plt
y = list(np.random.randint(1,100,size=50))
x = list(np.arange(1,51,1))
plt.figure(figsize=(20,10))

def selection_sort(arr):
    n = len(arr)

    # Traverse through all array elements
    t=0
    for i in range(n):
        # Find the minimum element in the remaining unsorted array
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
            t=t+1
            plt.bar(x,arr)
            plt.savefig(f'bar_graph_{t}.jpg', format='jpg')
            plt.clf()
                
                

        # Swap the found minimum element with the first element
        arr[i], arr[min_idx] = arr[min_idx], arr[i]


    # Test the selection_sort function

selection_sort(y)
print("Sorted array is:", y)
