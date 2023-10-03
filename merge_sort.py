import numpy as np
import matplotlib.pyplot as plt
y = list(np.random.randint(1,100,size=50))
plt.figure(figsize=(20, 10))
def merge_sort(arr):
    t = 0
    if len(arr) > 1:
        mid = len(arr) // 2  # Find the middle of the list
        left_half = arr[:mid]  # Split the list into two halves
        right_half = arr[mid:]

        # Recursive call on each half
        merge_sort(left_half)
        merge_sort(right_half)

        # Merge the sorted halves back together
        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
                t = t + 1
                plt.bar(range(len(arr)), arr)  # Use range(len(arr)) for x-axis
                plt.savefig(f'bar_graph_{t}.jpg', format='jpg')
                plt.clf()
            else:
                arr[k] = right_half[j]
                j += 1
                t = t + 1
                plt.bar(range(len(arr)), arr)  # Use range(len(arr)) for x-axis
                plt.savefig(f'bar_graph_{t}.jpg', format='jpg')
                plt.clf()
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1
            t = t + 1
            plt.bar(range(len(arr)), arr)  # Use range(len(arr)) for x-axis
            plt.savefig(f'bar_graph_{t}.jpg', format='jpg')
            plt.clf()

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
            t = t + 1
            plt.bar(range(len(arr)), arr)  # Use range(len(arr)) for x-axis
            plt.savefig(f'bar_graph_{t}.jpg', format='jpg')
            plt.clf()

# Call merge_sort with the initialized 'y' array
merge_sort(y)
print("Sorted array is:", y)
