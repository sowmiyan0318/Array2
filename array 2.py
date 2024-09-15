def rotate_array(arr, k):
    k = k % len(arr)  # In case k is greater than the length of the array
    return arr[-k:] + arr[:-k]

# Example usage:
arr = [1, 2, 3, 4, 5, 6, 7]
k = 3
print(rotate_array(arr, k))  # Output: [5, 6, 7, 1, 2, 3, 4]
