# There is syntax error at line 40.


import numpy as np
'''
There are 48 characters in input string.
Thus path can be chosen to be something that covers all 
the squares in grid.

This leaves us with case where we strike the wall or path in 
such a way that both col-1 and co+1 is not visited or 
row-1 and row+1 is not visited.

We need to include this special case.


'''


# Python program to calculate grid paths.


# Some constants to be used

# visited array that tracks whether given position is visited or not

visited = np.zeros((7,7))

n = 7 # the len of grid 


reserved = np.empty(n**2)


def move(r, c, ans, steps):
	if r == n-1 and c == 0:
		ans += (steps == n**2 - 1)
		return

	if ((r+1 == n or (visited[r-1][c] and visited[r+1][c])) and c-1 >= 0 and c+1 < n and !visited[r][c-1] and !visited[r][c+1]) or  ((c+1 == n or (visited[r][c-1] and visited[r][c+1])) and r-1 >= 0 and r+1 < n and !visited[r-1][c] and !visited[r+1][c]) or ((r==0  or (visited[r+1][c] and visited[r-1][c])) and c-1 >= 0 and c+1 < n and !visited[r][c-1] and !visited[r][c+1]) or ((c == 0 or (visited[r][c-1] and visited[r][c+1])) and r-1 >= 0 and r+1 < n and !visited[r-1][c] and !visited[r+1][c]):
		return

	visited[r][c] = True

	if reserved[steps] != -1:
		if reserved[steps] == 0:
			if r - 1 >= 0:
				if !visited[r-1][c]:
					steps += 1
					move(r-1, c, ans, steps)
					steps -= 1

		elif reserved[steps] == 1:
			if c + 1 < n:
				if !visited[r][c+1]:
					steps += 1
					move(r, c+1, ans, steps)
					steps -= 1

		elif reserved[steps] == 2:
			if r + 1 < n:
				if !visited[r][c-1]:
					steps += 1
					move(r+1, c, ans, steps)
					steps -= 1

		elif reserver[steps] == 3:
			if c - 1 >= 0:
				if !visited[r][c-1]:
					steps += 1
					move(r, c-1, ans, steps)
					steps -= 1
		visited[r][c] = False
		return

	if r+1 < n:
		if !visited[r+1][c]:
			steps += 1
			move(r+1, c, ans, steps)
			steps -= 1

	if c+1 < n:
		if !visited[r][c+1]:
			steps += 1
			move(r, c+1, ans, steps)
			steps -= 1

	if c-1 >= 0:
		if !visited[r][c-1]:
			steps += 1
			move(r, c-1, ans, steps)
			steps -= 1

	if r-1 >= 0:
		if !visited[r-1][c]:
			steps += 1
			move(r-1, c, ans, steps)
			steps -= 1

		

	visited[r][c] = False
	
# Input

path = input().strip()

for i in range(len(path)):
	if path[i] == '?':
		reserved[i] = -1
	elif path[i] == 'U':
		reserved[i] = 0
	elif path[i] == 'R':
		reserved[i] = 1
	elif path[i] == 'D':
		reserved[i] = 2
	elif path[i] == 'L':
		reserved[i] = 3

ans = 0
steps = 0

move(0,0, ans, steps)

print(ans)


	
