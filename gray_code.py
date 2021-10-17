n = int(input())

if n == 1:
	print("0", "1", sep="\n")

# base case
arr1 = ["00", "01", "11", "10"]
arr2 = ["10", "11", "01", "00"]

while True and n != 1:	
	if len(arr1) == 2**n:
		print(*arr1, sep = "\n")
		break
		
	# prefixing 0 to arr1 and 1 to arr2
	for i in range(len(arr1)):
		arr1[i] = "0" + arr1[i]
		arr2[i] = "1" + arr2[i]

	arr_conc = arr1 + arr2
	arr1 = arr_conc
	arr2 = arr_conc[::-1]
