import numpy as np
import matplotlib.pyplot as plt
y = list(np.random.randint(1,100,size=50))
x = list(np.arange(1,51,1))
plt.figure(figsize=(20,10))
def bubble_sort(arr):
    n = len(arr)
    t=0
    for i in range(n):

        
        
        for j in range(0, n - i - 1):
            
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                t=t+1
                plt.bar(x,arr)
                plt.savefig(f'bar_graph_{t}.jpg', format='jpg')
                plt.clf()

bubble_sort(y)
print("done")
