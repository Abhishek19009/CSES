# n = int(input())
#
# temp_list = []
#
# for i in range(1, n+1):
#     if i%2 != 0:
#         temp_list.append(i)
#
# for i in range(1, n+1):
#     if i%2 == 0:
#         temp_list.append(i)
#
# if temp_list[-1] - temp_list[-2] == -1:
#     print("NO SOLUTION")
# else:
#     for i in temp_list:
#         print(i, end = " ")

n = int(input())

if n == 1:
    print(1)

if n == 2 or n == 3 :
    print("NO SOLUTION")

# 2 4 1 3
else:
    for i in range(1, n+1):
        if i%2 == 0:
            print(i , end = " ")

    for i in range(1, n+1):
        if i%2 != 0:
            print(i, end = " ")