def heapify(arr, n, i, key_index=0):
    largest = i
    left = 2*i + 1
    right = 2*i + 2

    if left < n and arr[left][key_index] > arr[largest][key_index]:
        largest = left
    if right < n and arr[right][key_index] > arr[largest][key_index]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest, key_index)

def heap_sort(arr, key_index=0):
    n = len(arr)
    for i in range(n//2 - 1, -1, -1):
        heapify(arr, n, i, key_index)

    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0, key_index)

    return arr

n = int(input())
movies = [tuple(map(int, input().split())) for _ in range(n)]

# 끝나는 시간 기준으로 오름차순 정렬 (key_index=1)
movies = heap_sort(movies, key_index=1)

end = 0
count = 0

for start, finish in movies:
    if start >= end:
        count += 1
        end = finish

print(count)


