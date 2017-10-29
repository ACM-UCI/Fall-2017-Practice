m, n = map(int, input().split())
grid = []

for i in range(n):
    grid.append(input())
    if 'P' in grid[-1]:
        location = (i, grid[-1].index('P'))

safe = [[1 for j in range(m)] for i in range(n)]
#safe[i][j] will be 0 if the position (i,j) is adjacent to a trap, and 1 otherwise

#fill in the safe table
for i in range(n):
    for j in range(m):
        if grid[i][j] == 'T':
            for x,y in [(0,1), (1,0), (0,-1), (-1,0)]:
                new_x = j+x
                new_y = i+y
                if 0 <= new_x < m and 0<=new_y < n:
                    safe[new_y][new_x] = 0

#perform DFS through the grid, but when the current location is not safe,
#then we don't explore any further (i.e. we don't put any neighbors onto the stack like we would otherwise)
stack = [location] #standard DFS setup (stack is a list of all the places that are on our to-do list to explore)
G = 0 #gold counter
been = set() #standard DFS setup (been is a set that keeps track of where we've been)
while(len(stack) > 0): #standard DFS (as long as we have more places we want to explore, then explore them)
    old_y, old_x = stack.pop() #standard DFS (explore the last thing in our to-explore list, and take it off the list)
    if (old_y, old_x) in been: #standard DFS (if we've already explored here, then do not explore it now.)
        continue
    been.add((old_y, old_x)) #standard DFS (add current location to been so that we don't explore it again)
    if grid[old_y][old_x] == 'G': #if this square contains gold, increment our gold counter
        G+= 1
    if not safe[old_y][old_x]: #if this square is adjacent to a trap, then don't add its neighbors to the stack
        continue
    for dx,dy in [(0,1), (1,0), (0,-1), (-1,0)]: #standard DFS (add all valid neighbors to the stack because we want to explore them)
        new_x = old_x + dx
        new_y = old_y + dy
        if 0 <= new_x < m and 0<=new_y < n and (new_y, new_x) not in been and grid[new_y][new_x] != '#':
            #the x and y coordinates must be valid, and we must not have already explored there, and it must not be a wall
            stack.append((new_y, new_x))

print(G)
