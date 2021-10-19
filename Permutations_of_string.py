a = input()

result = []

def permute(data, i, length):
        if i == length:
                result.append(''.join(data))
        else:
                for j in range(i, length):
                    data[i], data[j] = data[j], data[i]
                    permute(data, i+1, length)
                    data[i], data[j] = data[j], data[i]


permute(list(a), 0, len(a))

result = list(set(result))

result.sort()

print(len(result))
print(*result, sep="\n")
