a = input()

result = []

def permute(i, length, data):
    if i == length:
        result.append("".join(data))

    else:
        for j in range(i, length):
            data[i], data[j] = data[j], data[i]
            permute(i+1, length, data)
            data[i], data[j] = data[j], data[i]


permute(0, len(a), list(a))

result = list(set(result))

print(len(result))

result.sort()

print(*result, sep = "\n")





