p=2

def elementFinder(m, n):
    return (p**n)%m

def sequenceFinder(m):
    seq=[]
    n=1
    while True:
        s=elementFinder(m ,n)
        if s in seq:
            return seq+[s]
        seq.append(s)
        n+=1

def tailFinder(m):
    seq=sequenceFinder(m)
    numbersUsed=[]
    firstDuplicate=None
    n=0
    while firstDuplicate==None:
        if seq[n] in numbersUsed:
            firstDuplicate=seq[n]
        numbersUsed.append(seq[n])
        n+=1
    for n in range(len(seq)):
        if seq[n]==firstDuplicate:
            return seq[:n]

def ordp(number):
    if number%p==0:
        return 1+ordp(number/p)
    else:
        return 0

def periodFinder(m):
    seq=sequenceFinder(m)
    tail=tailFinder(m)
    period=seq[len(tail):-1]
    return period

def primeFactorizer(number):
    spf=smallestPrimeFactor(number)
    if spf==number:
        return number
    return (str(spf)+'*'+str(primeFactorizer(int(number/spf))))

def smallestPrimeFactor(number):
    for x in range(2,int((number)**(1/2))+1):
        if number%x==0:
            return x
    return number

# tail0=[]
# tailed=[]
# for m in range (3, 101):
#     tail=sequenceFinder(m)
#     if tail[-1]==p:
#         tail0.append(m)
#     else:
#         tailed.append(m)
#     print(m, tail)

# print('Tailless', tail0)
# print('Tailed:', tailed)

# for m in range(3, 101):
#     # print(m//(p**ordp(m)), '*', p,  '^', ordp(m), ':', tailFinder(m))
#     print(ordp(m)-len(tailFinder(m)))

# for m in range (3, 101):
#     print(m, ':', max(ordp(m)-1, 0), len(tailFinder(m)))
primes=[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
for count in primes:
    m=3*count
    per=len(periodFinder(m))
    print(m, '=', primeFactorizer(m), ':', per, '=', primeFactorizer(per)) #, ':' , m-per, ':', (m-1)/(per))
    print(len(periodFinder(m//3)), '=', primeFactorizer(len(periodFinder(m//3))))
    print((m/3-1)/per, per/len(periodFinder(m//3)))
    print('===>', periodFinder(m))

'''
Conjecture for B: the length of the tail is max(0, ord2(m)-1)
=>Tailed are multiples of 4
=>Tailess are not multiples of 4
    Iff you have a 2 in your period then you will have no tail.
    Either 2*odd or odd
        If m is odd, then (2^k)%m=2 for some k>1.
            Prove that (2^(k-1))%m=1
        If m is 2*odd, then (2^k)%m=2 for some k>1.

Conjecture for C: 
=>The period of 2m is the period of m but all elements are multiplied by 2
=>The o(3m) is a factor of (m-1) and a multiple of o(m) if m is prime greater than 3
'''

# for k in range(1, 101):
#     if (p**k)%11==p:
#         print(k)