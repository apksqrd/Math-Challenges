'''
Complex Numbers
x represents a, y represents b
z=a+bi
z=[a, b]

Finding z squared
z**2=(a+b*i)*(a+b*i)=(a**2)+(a*b*i)+(b*i*a)+[(b*i)**2]=(a**2)+(2*a*b*i)+[(b**2)*(-1)]=(a**2-b**2)+(2*a*b*i)
    newA=a**2-b**2
    newB=2*a*b

How to see if a number z0 (aka a+bi) is in the Mandelbrot set:
zn=z(n-1)**2+z0 or the new term is the previous term squared, plus the 0th term
If the terms shoot off into infinity in any direction as you go to the next ones, then the term is not in the Mandelbrot set.

We can compute this in python by seeing if it ever goes away from the origin more than 2 units (Pythagorean theorem) while running it for many (20+) iterations

'''

import sys
import pygame


#basic operations n stuff
def add(z0, z1):
    return (z0[0]+z1[0], z0[1]+z1[1])
    
def multiply(z0, z1):
    return (z0[0]*z1[0]-z0[1]*z1[1], z0[0]*z1[1]+z0[1]*z1[0])

def square(z):
    return ((z[0]**2)-(z[1]**2), 2*z[0]*z[1])

def distanceSqrd(z):
    return (z[0]**2)+(z[1]**2)

def ratio(mid, segment):
    return (mid-segment[0])/(segment[1]-segment[0])

def ratioReverse(pointOld, segmentOld, segmentNew):
    ''' Explanation:
finds a point in the new segment that corresponds to the old point in the old segment 
kinda like how similarity works in geomentry
pointOld=2
segmentOld=[0, 5]
segmentNew=[-1, 9]
r=2/5
return 1'''
    r=ratio(pointOld, segmentOld)
    return segmentNew[0]+((segmentNew[1]-segmentNew[0])*r)

def multiDimRelocator(oldPoint, oldWin, newWin):
    newPoint=[]
    for dim in range(len(oldPoint)):
        newPoint.append(ratioReverse(oldPoint[dim], oldWin[dim], newWin[dim]))
    return newPoint

def defaultColorKey(num):
    x=ratioReverse((1-1/(num+1))**(4), [0, 1], [0, 255])
    return (255-x/2, x, x)

#fractals
def mandelbrotTest(z, iterations):
    Zs=[z[:]]
    for iteration in range(0, iterations):
        newZ=add(square(Zs[-1]), z)
        Zs.append(newZ)
        if distanceSqrd(newZ)>=4:
            return False, Zs
    return True, Zs

class Mandelbrot:
    def __init__(self, size=(720, 720), viewWindow=[[-2, 2], [-2, 2]], colorKey=defaultColorKey, iterations=100, visibleProgress=True):
        pygame.init()

        self.surface=pygame.display.set_mode(size)

        #sizes
        self.dispSize=[[0, size[0]], [0, size[1]]]
        self.viewWindow=viewWindow

        self.colorKey=colorKey
        self.iterations=iterations
        self.visibleProgress=visibleProgress

        self.mandelbrotGrid()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.routeTracer(event.pos)

    def mandelbrotGrid(self):
        for pixelX in range(self.dispSize[0][-1]):
            for pixelY in range(self.dispSize[1][-1]):
                a, b=multiDimRelocator([pixelX, pixelY], self.dispSize, self.viewWindow)
                inside, Zs=mandelbrotTest((a, b), self.iterations)
                if inside:
                    self.surface.set_at((pixelX, pixelY), 'black')
                else:
                    self.surface.set_at((pixelX, pixelY), self.colorKey(len(Zs)))
            if self.visibleProgress:
                pygame.display.flip()
        print('done')
        pygame.display.flip()

    def routeTracer(self, pos):
        z=multiDimRelocator(pos, self.dispSize, self.viewWindow)
        Zs=[z[:]]
        for iteration in range(0, self.iterations):
            newZ=add(square(Zs[-1]), z)
            Zs.append(newZ)
            if not ((self.viewWindow[0][0]<newZ[0]<self.viewWindow[0][1]) and (self.viewWindow[1][0]<newZ[1]<self.viewWindow[1][1])):
                break
        pixels=[]
        for z in Zs: #turn coords to pixelcoords
            pixels.append(multiDimRelocator(z, self.viewWindow,  self.dispSize))
        # self.shapes=[]
        for zCount in range(len(pixels)):
            if zCount!=0:
                line=pygame.draw.line(self.surface, (255, 255, 255), pixels[zCount-1], pixels[zCount], 2)
                # self.shapes.append(line)
            circle=pygame.draw.circle(self.surface, (255, 255, 255), pixels[zCount], 5)
            # self.shapes.append(circle)
        pygame.display.flip()

m=Mandelbrot()