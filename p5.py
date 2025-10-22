def solution(numlist, n):
    return sorted(numlist, key=lambda x: (abs(x - n), -x))

print(solution([1, 2, 3, 4, 5, 6], 4))  # [4, 5, 3, 6, 2, 1]
