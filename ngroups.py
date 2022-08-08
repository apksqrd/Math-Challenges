'''
l=[1, 2, 3, 4, 5], n=2
=>[[1, 2], [1, 3], [1, 4], [1, 5], [2, 3], [2, 4], [2, 5], [3, 4], [3, 5], [4, 5]]

l=[1, 2, 3, 4] n=3
=>[[1, 2, 3], [1, 2, 4], [1, 3, 4], [2, 3, 4]]

'''


def ngroupFinder(l, n):
    groups=[]
    if n==0:
        return [[]]
    
    for element in range(0, len(l)):
        newL=l[element+1:]
        smallGroups=ngroupFinder(newL, n-1)
        for smallGroup in smallGroups:
            groups.append([l[element]]+smallGroup)
    return groups

l=['a', 'b', 'c', 'd', 'e']

print(ngroupFinder(l, n=3))