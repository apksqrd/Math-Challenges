from math import ceil
from collections import Counter
from random import randint

lowercase='abcdefghijklmnopqrstuvwxyz'
uppercase='ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def caesarCipher(plaintext: str, key: int=0) -> str:
    plaintext=plaintext.upper()
    cyphertext=''
    for letter in plaintext:
        if letter not in uppercase:
            cyphertext+=letter
        else:
            cyphertext+=chr((ord(letter)-65+key)%26+65)
    return cyphertext.upper()

def caesarDecipher(cyphertext: str, key: int=0) -> str:
    return caesarCipher(plaintext=cyphertext, key=-key).lower()

def cycleCaesar(cyphertext: str) -> list:
    '''
    Run:
    print(ndJoin(cycleCaesar(cyphertext="insert cyphertext"), joiners=['\n'.join, ' '.join]))
    to display this well.
    '''
    cases=[]
    for key in range(0, 26):
        cases.append([str(key), caesarDecipher(cyphertext=cyphertext, key=key)])
    return cases


def lrArray(plain: str, width: list) -> list:
    return [[plain[width*row+col] if width*row+col<len(plain) else '*' for col in range(width)] for row in range(ceil(len(plain)/width))]

def lrReader(array: list) -> str:
    s=''
    return ''.join([''.join(row) for row in array])

def udReader(array: list) -> list:
    newA=[]
    for column in range(len(array[0])):
        newRow=[]
        for row in range(len(array)):
            newRow.append(array[row][column])
        newA.append(newRow)
    return newA

betterJoin=lambda words, split=' ', processor=lambda x: x:split.join([processor(word) for word in words])

def ndJoin(array: list, joiners: list=['\n'.join, ' '.join]) -> str:
    if type(array[0])!=list: return joiners[0]([str(elem) for elem in array])
    return joiners[0]([ndJoin(row, joiners=joiners[1:]) for row in array])

def cycleArray(cyphertext: str) -> list:
    pass


def vigenereCipher(plaintext: str, key: str) -> str:
    plaintext=plaintext.upper()
    key=key.upper()
    cyphertext=''
    for letterIndex in range(len(plaintext)):
        if plaintext[letterIndex] not in uppercase:
            cyphertext+=plaintext[letterIndex]
        else:
            cyphertext+=chr((ord(plaintext[letterIndex])-65+ord(key[letterIndex%len(key)])-65)%26+65)
    return cyphertext.upper()

def vigenereDecipher(plaintext: str, key: str) -> str: #i don't wanna label correctly
    plaintext=plaintext.upper()
    key=key.upper()
    cyphertext=''
    for letterIndex in range(len(plaintext)):
        if plaintext[letterIndex] not in uppercase:
            cyphertext+=plaintext[letterIndex]
        else:
            cyphertext+=chr((ord(plaintext[letterIndex])-65-ord(key[letterIndex%len(key)])+65)%26+65)
    return cyphertext.lower()

def wordMaker(wordLen: int, letters: list = uppercase) -> list:
    if wordLen==1:
        return letters
    words=[]
    for l in letters:
        subwords=wordMaker(wordLen=wordLen-1, letters=letters)
        for subword in subwords:
            words.append(l+subword)
    return words

def cycleVigenere(cyphertext: str, keyLen: int) -> str:
    plains=[]
    for key in wordMaker(keyLen):
        plain=vigenereDecipher(cyphertext, key)
        likely=wordness(plain)
        plains.append([likely, key, plain])
    return sorted(plains, key=lambda x: -x[0])
    
# wordFreq={'the':53, 'of':31, }

def wordness(s: str) -> float:
    s=s.lower()
    w=0
    for letter in s:
        if letter=='z' or letter=='x':
            w-=10000000000000
        if letter in letterFreq.keys():
            w+=(1000*letterFreq[letter])**2
        else:
            w+=5
    if 'th' in s:
        w+=100
    if 'he' in s:
        w+=100
    if 'in' in s:
        w+=100
    if 'en' in s:
        w+=100
    if 'nt' in s:
        w+=100
    if 'er' in s:
        w+=100
    if 'the' in s:
        w+=10000
    if 'and' in s:
        w+=10000
    if 'tha' in s:
        w+=10000
    if 'ent' in s:
        w+=10000
    if 'ing' in s:
        w+=10000
    return w

def primefactorizer(number: int) -> list:
    spf=smallestprimefactor(number)
    if spf==number:
        return [number]
    return [spf, *primefactorizer(int(number/spf))]

def smallestprimefactor(number: int) -> int:
    for x in range(2,int((number)**(1/2))+1):
        if number%x==0:
            return x
    return number

def gcf(*numbers: int): #doesn't work lol
    gcf=primefactorizer(numbers[0])
    print(gcf)
    for number in numbers[1:]:
        factors=primefactorizer(number)
        print(factors)
        for factor in gcf:
            if factor not in factors:
                gcf.remove(factor)
            else:
                factors.remove(factor)
    return gcf

def modMultTable(m:int) -> list: 
    '''print(ndJoin(modMultTable(m='INSERT_M'), joiners=['\n'.join, ' '.join]))'''
    '''print(ndJoin(modMultTable(m=13), joiners=['\n'.join, lambda words: betterJoin(words, ' |', processor=lambda x: x.rjust(3))]))'''
    return[[(x*y)%m for y in range(m)] for x in range(m)]

def modPower(m:int, exponent:int, power:int) -> int:
    '''print(ndJoin([[' ']+list(range(0, 10))]+[[exp]+[modPower(m=11, exponent=exp, power=p) for p in range(0, 10)] for exp in range(0, 11)], joiners=['\n'.join, lambda words: betterJoin(words, ' |', processor=lambda x: x.rjust(3))]))'''
    p=1
    for i in range(power):
        p*=exponent
        p=p%m
    return p

def modRoot(m:int, radicand:int, index:int) -> list:
    roots=[]
    for exponent in range(0, m):
        if modPower(m=m, exponent=exponent, power=index)==radicand:
            roots.append(exponent)
    return roots

def genericCryptogram(plain:str, key: dict) -> str:
    cipher=''
    for letter in plain:
        if letter in key: cipher+=key[letter]
        else: cipher+=letter
    return cipher

letterFreq={'E':0.111607, 'A':0.084966, 'R':0.075809, 'I':0.075448, 'O':0.071635, 'T':0.069509, 'N':0.066544, 'S':0.057351, 'L':0.054893, 'C':0.045388, 'U':0.036308, 'D':0.033844, 'P':0.031671, 'M':0.030129, 'H':0.030034, 'G':0.024705, 'B':0.020720, 'F':0.018121, 'Y':0.017779, 'W':0.012899, 'K':0.011016, 'V': 0.010074, 'X':0.002902, 'Z':0.002722, 'J':0.001965, 'Q':0.001962}
def keyGuesser(cipher:str, knownKey: dict={' ':' '}, genericFreq=letterFreq) -> dict:
    cipherFreqs=dict(Counter(cipher))
    predKey={}
    for letter in knownKey.keys():
        if letter in cipherFreqs.keys(): 
            del cipherFreqs[letter]
        if letter in genericFreq.keys():
            del genericFreq[letter]
    for i in range(len(cipherFreqs)):
        predKey[list(cipherFreqs.keys())[i]]=list(genericFreq.keys())[i]
    return predKey

def isbnVerify(pin):
    pin=str(pin)
    s=0
    for i in range(len(pin)):
        s+=(10-i)*int(pin[i])
    return s%11

def numberCipher(plain: str, shift: int, endMod: int, addMod: int = 10, repeatFreq: int = 2, letters: list = lowercase, backwards: bool = True) -> str:
    numbers=[]
    plain=plain.lower()
    if backwards:
        def baseNto10(numberList):
            sum([numberList[i2]*addMod**(len(numberList)-i2-1) for i2 in range(0, len(numberList))])
    else:
        def baseNto10(numberList):
            sum([numberList[i2]*addMod**(i2) for i2 in range(0, len(numberList))])

    for i in range(ceil(len(plain)/repeatFreq)):
        numberList=[]
        for i2 in range(i*letterFreq, min((i+1)*letterFreq+1, len(plain))): 
            numberList.append(letters.index(plain[i2]))
        number=baseNto10(numberList)
        numbers.append(number)
    return numbers

def rsaRandomKeysGenerator(p, q):
    n=p*q
    phiN=(p-1)*(q-1)
    e=randint(2, phiN)
    d=pow(e, -1, n)
    return e, d

def rsaEncrypt(plain, e, n):
    return modPower(plain, e, n)

def rsaDecrypt(cipher, d, n):
    return modPower(cipher, d, n)






if __name__ == "__main__":
    print(vigenereDecipher("QYQGEHQYOVSEGTBCQDQZAAMSUEZGYFCWCPODASWNVOJPFGDZGCSYOJGEVKBLGPBEVGEVG", "Clocks"))



"once upon a time in a gloomy castle on a lonely hill where there were thirteen clocks"
# while True:
#     print(exec(input('Type your cmd: ')))