# Python program for implementation of Insertion Sort
def insertion_sort(arr):
    # Traverse through 1 to len(arr)
    print('Original list:', arr, '\n')
    for i in range(1, len(arr)):
        key = arr[i]
        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
        print(f'pass {i}, with key = {key}:', arr)


arr = [22, 79, 18, 41, 92, 2, 57, 37, 53, 9]

insertion_sort(arr)

print('\nInsertion sorted:', arr)