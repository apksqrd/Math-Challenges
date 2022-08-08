def lookSayNext(term):
    stringTerm=str(term)
    listTerm=list(stringTerm)
    newTerm=''
    prevLetter=None
    count=0
    for letter in listTerm:
        if letter==prevLetter:
            count+=1
        else:
            if prevLetter==None:
                pass
            else:
                newTerm+=str(count)+prevLetter
            prevLetter=letter
            count=1
    newTerm+=str(count)+letter
    return newTerm

def lookSayNth(startTerm, iterations):
    allTerms=[startTerm]
    for iteration in range(1, iterations):
        term=lookSayNext(allTerms[-1])
        allTerms.append(term)
    return allTerms

def displayTerms(allTerms):
    for iteration in range(0, len(allTerms)):
        print('%sth term: %s'%(iteration, allTerms[iteration]))

displayTerms(lookSayNth(1, iterations=20))