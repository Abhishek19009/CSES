n = int(input())
m = list(map(int, input().strip().split()))

print(m)

m2 = m[:]

m2.sort()

count = 0

for i in range(len(m)):
    if m[i] != m2[i]:
        m[i] = m2[i]
        count += 1


print(count)