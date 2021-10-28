#def q1(lst,n):
#    return lst[-n:]
#
#print(q1([34,24],1))

#def q1(filename,lst):
#
#    with open(filename, 'w') as f:
#        for item in lst:
#            if item.lower() != 'stop':
#                f.writelines(str(item) + '\n')
#            else:
#                break
#    
#
#q1('test.txt',['Hello','World','this','STop','no','this','isnt','working'])

#def q1(filename):
#    with open(filename, 'r') as f:
#        firstLine = f.readline()
#    
#    return len(firstLine.strip())

#
#def q1(miltime):
#    miltime = int(miltime)
#    greeting = 'Good '
#    if miltime < 259 or miltime > 2100:
#        greeting += 'Night'
#    elif miltime < 1159:
#        greeting += 'Morning'
#    elif miltime < 1559:
#        greeting += 'Afternoon'
#    elif miltime < 2059:
#        greeting += 'Evening'
#
#    return greeting
#
#
#def q1(string):
#    encoded_str = string.encode()
#    byte_array = bytearray(encoded_str)
#    return list(byte_array)
#
#def q1(*args):
#    return sum(args)/len(args)
#
#def q1(string):
#    return tuple(string.split())
#
#def q1(numlist):
#    for num in numlist:
#        if num < 0:
#            return False
#        
#    return True
#
#def q6(catalog, order):
#    total = 0
#    for item in order:
#        total += catalog[item[0]] * item[1]
#    
#    return total
##
#def q1(floatstr):
#    floatstr = floatstr.split(',')
#    for i,el in enumerate(floatstr):
#        floatstr[i] = float(el)
#    return floatstr
##
#def q1(integer,limit):
#    numList = []
#    curnum = 0
#    while curnum <= limit and curnum % 2 == 0:
#        numList.append(curnum)
#        curnum += integer
#    return numList
#
#def q1(f0, f1):
#    f0Line = 0
#    counter = 0
#    difLineNums = []
#    with open(f0, 'r') as f0, open(f1, 'r') as f1:
#        while f0Line != '':
#            f0Line = f0.readline()
#            f1Line = f1.readline()
#            if f0Line != f1Line:
#                difLineNums.append(counter)
#            counter += 1
#
#    return difLineNums
#
#

def q1(s1,s2,s3):
    if sum((s1,s2,s3))/3 > 50:
        return 'GO'
    else:
        return 'NOGO'

def q1(string):
    strList = string.split()
    lenList = [len(el) for el in strList]
    return min(lenList)

def q1(sentance):
    wordList = sentance.split()
    return ' '.join(wordList[::-1])

def q1(lst0, lst1):
    newList = lst0 + lst1
    return sorted(newList,reverse=True)

def q1(lst):
    for elem in lst:
        if lst.count(elem) > 1:
            return elem

print(q1([5,7,9,1,3,7,9,5]))

def q1(lst):
    counter = lst[0]
    for elem in lst:
        if elem != counter:
            return elem
        counter += 1
    return None

def q1(num):
    formatedNum = "{:,}".format(num)
    return formatedNum

def q1(string):
    intList = []
    for l in string:
        if l.isdigit():
            intList.append(l)
    
    return chr(int(''.join(intList)))

