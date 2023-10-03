import numpy as np
import matplotlib.pyplot as plt
y = list(np.random.randint(1,100,size=50))
x = list(np.arange(1,51,1))
plt.figure(figsize=(20,10))
def insertion_sort(arr):
    t=0
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
            t=t+1
            plt.bar(x,arr)
            plt.savefig(f'bar_graph_{t}.jpg', format='jpg')
            plt.clf()
        arr[j + 1] = key
        t=t+1
        plt.bar(x,arr)
        plt.savefig(f'bar_graph_{t}.jpg', format='jpg')
        plt.clf()

insertion_sort(y)
print("Sorted array is:", y)
