# n = input()
# temp = 0
# count = 0
# max_count = 0
#
#
# for i in range(len(n)-1):
#     if n[i] == n[i+1]:
#         count += 1
#         temp = 1
#
#     else:
#         temp = 0
#         count = 0
#
#     if temp == 1:
#         max_count = max(max_count, count)
#
#
# print(max_count+1)

n = input()

max_count = 0
count = 0
flag = 0

for i in range(len(n)-1):
    if n[i] == n[i+1]:
        flag = 1
        count += 1

    else:
        flag = 0
        count = 0

    if flag == 1:
        max_count = max(max_count, count)

print(max_count+1)