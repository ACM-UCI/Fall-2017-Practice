#for all vertices i, if there is a pair of vertices j and k for which
#ijk is a triangle (i.e. there's an edge between ij, jk, and ik), then i is not weak.
#otherwise, i is weak.
#to find out if there exists some pair jk for a given vertex i, we simply iterate through all possible pairs
n = int(input())
while n != -1:
    am = []
    for i in range(n):
        am.append([int(x) for x in input().split()])
    ans = []
    for i in range(n):
        part_of_a_triangle = False
        for j in range(n):
            for k in range(n):
                if am[i][j] and am[i][k] and am[j][k]:
                    part_of_a_triangle = True
        if not part_of_a_triangle:
            ans.append(i)
    print(' '.join(map(str,ans)))
    n = int(input())
