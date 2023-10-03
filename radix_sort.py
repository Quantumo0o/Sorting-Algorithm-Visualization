def radix_sort(arr):
    
    plt.figure(figsize=(20, 10))
    print(arr)
    # Find the maximum number to determine the number of digits
    max_num = max(arr)
    num_digits = len(str(max_num))

    # Perform counting sort for each digit, from LSD to MSD
    for digit_index in range(num_digits):
        # Initialize counting buckets
        count = [0] * 10
        output=arr.copy()

        # Count the occurrences of each digit in the current place value
        for num in arr:
            digit = (num // 10 ** digit_index) % 10
            count[digit] += 1

        # Calculate the cumulative count
        for i in range(1, 10):
            count[i] += count[i - 1]

        # Build the output array by placing elements in their sorted order
        i = len(arr) - 1
        while i >= 0:
            plt.bar(range(len(arr)), output)
            plt.savefig(f'heap_sort_step_{i}_{digit_index}.jpg', format='jpg')
            plt.clf()
            digit = (arr[i] // 10 ** digit_index) % 10
            output[count[digit] - 1] = arr[i]
            count[digit] -= 1
            i -= 1
            plt.bar(range(len(arr)), output)
            plt.savefig(f'heap_sort_step_{i}_{digit_index}.jpg', format='jpg')
            plt.clf()
            

        # Copy the sorted elements back to the original array
        for j in range(len(arr)):
            arr[j] = output[j]

    return arr

# Example usage:
y = np.random.randint(1, 101, 50)
sorted_arr = radix_sort(y)
print(sorted_arr)
