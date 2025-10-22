def max_heapify(arr, n, i):
    largest = i
    left = 2*i + 1
    right = 2*i + 2
    
    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right
    
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        max_heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)
    # Build max heap
    for i in range(n//2 - 1, -1, -1):
        max_heapify(arr, n, i)
    # Extract elements
    for i in range(n-1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        max_heapify(arr, i, 0)
    return arr

A = [4, 16, 15, 8, 7, 13, 14, 2, 5]
print("정렬 결과:", heap_sort(A))
