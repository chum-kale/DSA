def part(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i = i+1
            arr[i], arr[j] = arr[j], arr[i]
        
    (arr[i+1], arr[high]) = (arr[high], arr[i+1])
    return i + 1

def quicksort(arr, low, high):
    if low < high:
        pi = part(arr, low, high)
        quicksort(arr, low, pi-1)
        quicksort(arr, pi+1, high)

if __name__ == '__main__':
    array = [10, 7, 8, 9, 1, 5]
    N = len(array)

    # Function call
    quicksort(array, 0, N - 1)
    print('Sorted array:')
    for x in array:
        print(x, end=" ")