def calc_coin_pile(a,b):
	if (a+b)%3 == 0 and 2*a >= b and 2*b >= a:
		print("YES")
	else:
		print("NO")
	

if __name__ == "__main__":
	n = int(input())

	for _ in range(n):
		a,b  = input().strip().split()
		calc_coin_pile(int(a), int(b))


