a = input().strip()

hash_table = {}

for i in a:
	try:
		hash_table[i] += 1
	except:
		hash_table[i] = 1
	
odd_counter = 0
odd_var = None
out_str = ""

for i in hash_table:
	if hash_table[i]%2 != 0:
		odd_counter += 1
		odd_var = i

	else:
		out_str += i*(int(hash_table[i]/2))
		

if odd_counter > 1:
	print("NO SOLUTION")

else:	
	try:
		temp_str = out_str
		out_str += odd_var*hash_table[odd_var] + temp_str[::-1]
	except:
		out_str += temp_str[::-1]

	print(out_str)
		
