x = int(input())
i = input()
parents = dict() #if i is a node id, parents[i] contains the id of its parent
while i != '-1':
    l = [int(j) for j in i.split()[1:]]
    for j in l:
        parents[j] = (int(i.split()[0]))
    i = input()

print(x)
while x in parents:
    #walk up the tree to the root and print each node we visit
    x = parents[x]
    print(x)

