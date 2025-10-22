import math

def dist(a, b):
    return (a[0]-b[0])**2 + (a[1]-b[1])**2

T = int(input())
for _ in range(T):
    points = [tuple(map(int, input().split())) for _ in range(4)]
    d = sorted([dist(points[i], points[j]) for i in range(4) for j in range(i+1, 4)])
    print(1 if d[0] > 0 and d[0] == d[1] == d[2] == d[3] and d[4] == d[5] == 2*d[0] else 0)
