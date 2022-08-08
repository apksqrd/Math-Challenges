import random

def disjointCycleNotation(seq):
    # input:  1, 2, 3, 4, 5
    #        [2, 1, 4, 5, 3]
    #
    # output: [(1, 2), (3, 4, 5)]
    # pretend this goes from 0-4 cus i forgor python
    # visa versa
    seq=seq[:]
    cycles=[]
    for order in range(len(seq)):
        if seq[order]==None:
            pass
        else:
            cycle=[order]
            cycling=True
            prevOrder=order
            while cycling:
                newOrder=seq[prevOrder]
                if newOrder==None:
                    cycles.append(cycle[:-1]) #unclean. the entire thing is. maybe i can make this recursive?
                    cycling=False
                else:
                    cycle.append(newOrder)
                    seq[prevOrder]=None
                    prevOrder=newOrder
            seq[order]=None
    return cycles

def sequence(cycles):
    numOfElements=0
    for cycle in cycles:
        numOfElements+=len(cycle)
    seq=[None] * numOfElements
    for cycle in cycles:
        for order in range(len(cycle)):
            seq[cycle[order]]=cycle[(order+1)%len(cycle)]
    return seq

def mult(sigma1, sigma2):
    # assume sorted(sigma1) == sorted(sigma2) = list(range(n))
    # reads right to left
    # ex: perms=[[1, 3, 2, 4, 0], [4, 3, 0, 1, 2]]
    # 0 1 2 3 4 
    # 1 3 2 4 0
    # |
    # \
    #  \
    #   |
    # 0 1 2 3 4
    # 4 3 0 1 2
    # so 0->3
    # return: [3, 1, 0, 2, 4]
    # basically run x through the 0th perm, then the next one and keep on doing it and do that for all x in the range

    return [sigma1[sigma2[i]] for i in range(len(sigma2))]

def product(*sigmas):
    if len(sigmas) == 1:
        return sigmas[0]

    return mult(sigmas[0], product(*sigmas[1:]))

def inverse(sigma): 
    tau = [0 for a in sigma]
    for i in range(len(sigma)):
        tau[sigma[i]]=i
    return tau

def inversions(sigma):
    return len([i for i, a in enumerate(sigma) if i < a])

def descents(sigma):
    return [i for i, a in enumerate(sigma[:-1]) if a>sigma[i+1]]

def transp(i, n):
    l=list(range(n))
    l[i]=i+1
    l[i+1]=i
    return l

def factorizeRec(sigma):
    # factorize sigma into a product of transpositions
    # input [4, 2, 0, 1, 3]
    # output of this form [[1,2], [0,1], [3,4], ...]
    # actually transp not pairs
    # so that sigma == product(*factorize(sigma))
    # bubble sort but always switches lowest 

    d=descents(sigma)

    if len(d)==0:
        return []
    
    pivot=d[0]
    factor=transp(pivot, len(sigma))
    reduced=mult(sigma, factor)
    return [factor] + factorizeRec(reduced)

def factorize(sigma):
    done=False
    result=[]
    while not done:
        d=descents(sigma)
        if len(d)==0:
            done=True
            continue
        factor=transp(d[0], len(sigma))
        sigma=mult(sigma, factor)
        result=[factor]+result
    return result


def randPerm(size):
    sigma=[]
    unusedI=list(range(size))
    for a in range(size):
        r=random.randint(0, len(unusedI)-1)
        sigma.append(unusedI.pop(r))
    return sigma
    

#0, 2, 3
# p=[[4, 2, 3, 1, 0], transp(0, 5), transp(1, 5), transp(2, 5), transp(1, 5), transp(0, 5), transp(3, 5), transp(2, 5), transp(1, 5), transp(0, 5)]
# for i in range(1, len(p)+1):
#     sigma=product(*p[:i])
#     print(sigma, descents(sigma))
# print(product(*p[:0:-1]))
tot=0
for i in range(10000):
    sigma = randPerm(20)
    # l=max(len(a) for a in disjointCycleNotation(sigma)) #average length of longest cycle
    l=len(factorize(sigma))
    tot+=l
    print(sigma, l, tot/(i+1))

print(len(factorize(list(range(20))[::-1])))

# questions: what is average length of bubblesort for a random permutation on n elements?
#               n=20, avg=95.387, m=190
#
#            what is average length of longest cycle in disjoint cycle decomposition?
#               6.55 for n=10
#               12.789 for n=20
#               19.03 for n=30
#               62.78 for n=100
#               624.8523 for n=1000