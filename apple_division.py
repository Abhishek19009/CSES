def findMinRec(arr, i, sumCalculated, sumTotal):
	if (i==0):
		return abs((sumTotal - sumCalculated) - sumCalculated)

	return min(findMinRec(arr, i-1, sumCalculated + arr[i-1], sumTotal), findMinRec(arr, i-1, sumCalculated, sumTotal))


def findMin(arr, n):
	sumTotal = 0
	for i in arr:
		sumTotal += i

	return findMinRec(arr, n, 0, sumTotal)

if __name__ == "__main__":
	n = int(input().strip())

	p = list(map(int, input().strip().split(" ")))

	print(findMin(p, len(p)))


