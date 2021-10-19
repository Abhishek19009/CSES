'''
Not correct. 
Check mistakes.
'''

from itertools import permutations


def isValid(i,j, obs, elem):
    sum_index = i+j
    diff_index = j-i

    if (i,j) in obs:
        return False
    
    while True and i>0:
        i = i-1
        colr = sum_index - i
        coll = i + diff_index

        for j in range(0,8):
            if (j, elem[j]) == (i, colr):
                break
            elif (j, elem[j]) == (i, coll):
                break
        else:
            continue

    else:
        return True
    
    return False

if __name__ == "__main__":
    # Input
    grid = []
    obs = []
    count = 0

    for _ in range(8):      # main input grid
        grid.append(input().strip())

    for i in range(8):          # populating the obstacles with respective indices
        for j in range(8):
            if grid[i][j] == "*":
                obs.append((i,j))

    

    pos = [0,1,2,3,4,5,6,7]

    all_conf = permutations(pos)        # calculating all permutations

    for elem in all_conf:               # looping through all permutations
        for  i in range(len(elem)):
            if isValid(i, elem[i], obs, elem):      # if position in particular permutation is valid
                continue
            else:
                break
        else:                                       # if loop completes successfully, increase the counter
            count += 1

            
    print(count)
