import numpy as np
import matplotlib.pyplot as plt
y = list(np.random.randint(1,100,size=50))

plt.figure(figsize=(20, 10))

def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        plt.bar(range(len(arr)), arr)
        plt.savefig(f'heap_sort_step_{i}.jpg', format='jpg')
        plt.clf()

        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        plt.bar(range(len(arr)), arr)
        plt.savefig(f'heap_sort_step_{i}.jpg', format='jpg')
        plt.clf()

        heapify(arr, i, 0)

# Call heap_sort with the initialized 'y' array
heap_sort(y)
print("Sorted array is:", y)
