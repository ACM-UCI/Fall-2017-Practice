S = int(input())
for s in range(S):
    #read in input for this case
    n = int(input())
    intervals = []
    for i in range(n):
        a, b = map(int, input().split())
        intervals.append((a,b))
    #sort the intervals by their ENDing point
    intervals.sort(key = lambda a: a[1])
    #greedily go through our intervals in that order and take all the intervals that we can
    intervals_chosen = []
    rightmost_overlap = None #the point of the rightmost overlap (so that we know if there will be a double-overlap)
    for interval in intervals:
        if rightmost_overlap is None or interval[0] > rightmost_overlap:
            #if we can choose this interval without making a double-overlap, then we use it.
            intervals_chosen.append(interval)
            if len(intervals_chosen) > 1 and intervals_chosen[-2][1] >= intervals_chosen[-1][0]:
                #if there is an overlap, then record the point of the rightmost overlap
                rightmost_overlap = intervals_chosen[-2][1]
    print(len(intervals_chosen))
    