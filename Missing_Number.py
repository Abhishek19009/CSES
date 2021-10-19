n = int(input())

m = input().strip().split()
s = 0

for i in m:
    s += int(i)

print(int(n*(n+1)/2) - s)