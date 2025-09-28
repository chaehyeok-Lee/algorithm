# n,m,k 입력
n, m, k = map(int, input().split())
arr = list(map(int, input().split()))

#과제1 select_sort
def select_sort(arr):
    n = len(arr)
    for i in range(n):
        max_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[max_idx]:
                max_idx = j
        arr[i], arr[max_idx] = arr[max_idx],arr[i]
    return arr


arr = select_sort(arr)


first = arr[n-1]
second = arr[n-2]

#큰수 법칙 cycle,remainder
cycle = m // (k+1)
#cycle에 포함되지 않은 수 = first값
remainder = m % (k+1)

result = (cycle * (first * k + second)) + (remainder * first)

print(result)