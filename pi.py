import random

def gregoryLeibniz(iterations):
    pi=0
    for count in range(iterations):
        thing2add=4/(2*count+1)
        if count%2==0: #even
            pi+=thing2add
        else:
            pi-=thing2add
        print(pi)
    return pi

def nilakantha(iterations):
    pi=3
    for count in range(iterations):
        thing2add=4/((2+2*count)*(3+2*count)*(4+2*count))
        if count%2==0:
            pi+=thing2add
        else:
            pi-=thing2add
        print(pi)
    return pi

def randomPi(tests):
    IN=0
    OUT=0
    for count in range(1, tests+1):
        x=random.random()
        y=random.random()
        if x**2+y**2<1:
            #print('in')
            IN+=1
        else:
            #print('out')
            OUT+=1
        print(4*IN/count)

def summationPi(Mx, My):
    IN=0
    for x in range(0, Mx+1):
        for y in range(0, My+1):
            IN+=inCircle(x/Mx, y/My)
    return 4*IN/(Mx*My)

inCircle=lambda x, y: 1 if x**2+y**2<=1 else 0

print(summationPi(10000, 10000))