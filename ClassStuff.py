#def evensandodds(first, last):
#    vals = list(range(first, last+1))
#    evens = [i for i in vals if i % 2 == 0]
#    odds = [i for i in vals if i % 2 == 1]
#
#    for i in evens:
#        print(i)
#    for j in odds:
#        print(j)
#
#
#evensandodds(1,10)



#def guess_number(n):
#    
#    inputNum = -1
#    
#    while inputNum != n:
#        inputNum = int(input("Enter a number: "))
#        if inputNum < n:
#            print("too low")
#        elif inputNum > n:
#            print("too high")
#        
#    print("WIN")
#    return
#
#guess_number(23)

#def user_io():
#    userInfo = []
#    while True:
#        userInput = input("Enter string. Enter '' when finished: ")
#        if userInput == '':
#            return userInfo
# 
#        else:
#            userInfo.append(userInput)
#
#user_io()


#def disect(lst):
#    listLength = int(len(lst)/2)
#    lst1 = lst[:listLength]
#    lst2 = lst[listLength:]
#
#    return (lst1, lst2)
#
#print(disect([1,2,3,4]))

#def make_tuple(a,b):
#    multsOf10 = []
#    for i in range(a,b):
#        if i % 10 == 0:
#            multsOf10.append(i)
#    return tuple(multsOf10)
#
#print(make_tuple(3, 90))

#def reverseit():
#    userInfo = []
#    while True:
#        userInput = input("Enter string. Enter '' when finished: ")
#        if userInput == '':
#            return userInfo
# 
#        else:
#            userInfo.append(userInput[::-1])
#
#print(reverseit())

#def strings():
#    return ('',"Physics is the universe's operating system")

#def reverse_string(userInput):
#    return userInput[::-1]
#
#print(reverse_string())

#def code_points(string):
#    strList = list(string)
#    ordList = [None] * len(string)
#
#    for i, character in enumerate(string):
#        ordList[i] = ord(character)
#
#    return(ordList)
#
#print(code_points("Hello World"))

#def domath(a,b,c):
#    return (a + b) * c

#def make_tuple():
#    tensList = []
#    for i in range(1,11):
#        tensList.append(i * 10)
#    
#    return tuple(tensList)
#
#
#print(make_tuple())

#def linenums(inpath, outpath):
#    with open(inpath, 'r') as src, open(outpath, 'w')as dst:
#        for i, line in enumerate(src):
#           dst.write(str(str(i + 1) + ': ' + line))
#                
#linenums('test.txt', 'result.txt')


#def get_type_str(obj):
#    
#    classType = str(type(obj).__name__)
#
#    if classType == 'str':
#        return 'string'
#    elif classType == 'bool':
#        return 'boolean'
#    elif classType == 'int':
#        return 'integer'
#    elif classType == 'float':
#        return 'float'
#    elif classType == 'list':
#        return 'list'
#    elif classType == 'tuple':
#        return 'tuple'
#    else:
#        return 'unknown'
#    
#print(get_type_str(1))

#def find_product(a,b):
#    return a*b
#
#if __name__ == '__main__':
#    a = int(input("First Num: "))
#    b = int(input('Second Num: '))
#    print(find_product(a,b))
#


#def round_to_position(lst):
#    newList = []
#    for i, myFloat in enumerate(lst):
#        newList.append(round(myFloat, i))
#
#    return newList
#

#def get_hash(data='python'):
#    import hashlib
#    m = hashlib.sha3_256()
#    m.update(data.encode("utf-8"))
#    return m.hexdigest()
#
#print(get_hash())


#def grab(lst):
#    import random
#    index = random.randint(0,len(lst) - 1)
#    return lst[index]
#
#
#print(grab([1,2,3,4,5]))

#def linenums(inpath, outpath):
#    with open(inpath, 'r') as src, open(outpath, 'w')as dst:
#        for i, line in enumerate(src):
#           dst.write(str(str(i + 1) + ': ' + line))
#                
#linenums('test.txt', 'result.txt')

#def count_words(filepath):
#    myDict = {}
#    with open(filepath, 'r') as f:
#        Data = f.read()
#
#    words = Data.split()
#    for word in words:
#        if word not in myDict:
#            myDict[word] = 1
#        else:
#            myDict[word] += 1
#
#    return myDict

#def infinitearguments(*args, **kwargs):
#    for a in args:
#        print(a)
#    newDict = sorted(kwargs)
#    for el in newDict:
#        print(str(el) + '=' + str(kwargs[el]))
#
#
#infinitearguments(1,2,3,4,5,6,7,8, hello='john', asmuch='iknew')


#def sort_length(filepath):
#    with open(filepath,'r') as f:
#        data = f.readlines()
#    
#    data = [line.strip() for line in data]
#    print(data)
#    sortedData = sorted(data, key=lambda a: len(a),reverse=True)
#    return sortedData
#
#print(sort_length('stringLengths.txt'))
#
#def diffwords(fname, words):
#    with open(fname, 'r') as f:
#        data = f.read()
#
#    fileWords = set(data.split())
#    return fileWords.difference(words)
#    

#def sort_ascii(filepath):
#    with open(filepath, 'r') as f:
#        data = f.readlines()
#    data = [line.strip() for line in data]
#
#    data = sorted(data, key=lambda x: x.upper())
#    return data
#
#print(sort_ascii('stringLengths.txt'))



#def sort_embedded(filepath):
#    with open(filepath, 'r') as f:
#        data = f.readlines()
#
#    data = [line.strip() for line in data]
#    sortedData = sorted(data, key=lambda x: x[9:14])
#    return sortedData
#
#sort_embedded('stringLengths.txt')

#print(type(4).__name__)
#
#
#def mypin(pin):
#    validPin = False
#    try:
#        int(pin)
#    except:
#        validPin = False
#    else:
#        validPin = True


#def perms(mode):
#    permissions = 'rwxrwxrwx'
#    modeBin = format(mode, '09b')
#    modPermissions = []
#
#    for bit, perm in zip(modeBin, permissions):
#        temp = perm
#        if bit != '1':
#            temp = '-'
#        modPermissions.append(temp)
#    
#    return ''.join(modPermissions)
#
#print(perms(511))

#def complexity(password):
#    lowerCharSet = set('abcdefghijklmnopqrstuvwxyz')
#    numSet = set('0123456789')
#    upperCharSet = set('ABCDEFGHIJCLMNOPQRSTUVWXYZ')
#    specialCharSet = set('~!"@#$%^&\'*_-+=`|(){}[]:;<>,.?/')
#
#    complexityVal = 0
#
#    if len(password) >= 15:
#        complexityVal |= 0x1
#    if numSet.intersection(password):
#        complexityVal |= 0x2
#    if upperCharSet.intersection(password):
#        complexityVal |= 0x4
#    if lowerCharSet.intersection(password):
#        complexityVal |= 0x8
#    if specialCharSet.intersection(password):
#        complexityVal |= 0x10
#
#    return complexityVal
#
#print(bin(complexity('h3elloworld')))
#
#def crack(username):
#
#    for i in range(10000):
#        try:
#            login(username, str(i).zfill(4))
#        except PermissionError:
#            continue
#        else:
#            return str(i).zfill(4)
#
#
#
#
#class TicTacToe:
#
#    def __init__(self):
#        self.boardList = [[0,0,0],[0,0,0],[0,0,0]]
#        self.Symbol = 'X'
#        pass
#
#
#    def _checkRows(self, boardList):
#        for row in boardList:
#            if len(set(row)) == 1 and (0 not in set(row)):
#                return row[0]
#        
#        return 0
#
#    def _checkDiags(self, boardList):
#        frontDiagSet = set([boardList[i][i] for i in range(len(boardList))])
#        backDiagSet = set([boardList[i][len(boardList)-i-1] for i in range(len(boardList))])
#        
#        if len(frontDiagSet) == 1 and 0 not in frontDiagSet:
#            return boardList[0][0]
#        if len(backDiagSet) == 1 and 0 not in backDiagSet:
#            return boardList[0][len(boardList)-1]  
#
#        return 0
#
#    def _CheckWin(self, boardList):
#        
#        win = self._checkRows(boardList)
#        if win:
#            return win
#
#        win = self._checkRows(list(zip(*boardList)))
#        if win:
#            return win
#        
#        win = self._checkDiags(boardList)
#        return win
#        
#    def _CheckDraw(self, boardList):
#        mySet = set()
#        for list in boardList:
#            for item in list:
#                mySet.add(item)
#        if 0 not in mySet:
#            return 1
#        else:
#            return 0
#            
#    def move(self,row,col):
#        
#        curVal = self.boardList[row][col]
#
#
#        if curVal != 0:
#            raise  Exception()
#        else:
#            self.boardList[row][col] = self.Symbol
#            if self.Symbol == 'X':
#                self.Symbol = 'O'
#            else:
#                self.Symbol = 'X'
#
#        #print(self.boardList)
#
#        gameStat = self._CheckWin(self.boardList)
#        if gameStat == 'X':
#            return 1
#        elif gameStat == 'O':
#            return 2
#        elif self._CheckDraw(self.boardList):
#            return 0
#        elif gameStat == 0:
#            #print('gameStat')
#            return None
#
#
#MyBoard = TicTacToe()
#print(MyBoard.move(0,0))
#print(MyBoard.move(0,1))
#print(MyBoard.move(0,2))
#print(MyBoard.move(1,0))
#print(MyBoard.move(1,1))
#print(MyBoard.move(1,2))
#print(MyBoard.move(2,0))
#print(MyBoard.move(2,1))
#print(MyBoard.move(2,2))
#
#
#print(MyBoard.boardList)
#
#

#def tough_read(fname):
#    with open(fname, 'r') as f:
#        data = f.readlines()
#
#    charArray = [chr(int(el.strip(),2)) for el in data]
#
#    return ''.join(charArray)
#
#
#print(tough_read('test.txt'))


#def log_to_file(fname, theme):
#    msgList = []
#    while True:
#        message = input('Inspirational message: ')
#        if message == '':
#            break
#        
#        newMessage = str(theme) + ':' + message + '\n'
#        msgList.append(newMessage)
#    with open(fname, 'a') as f:
#        for el in msgList:
#            f.writelines(el)
#
#log_to_file('test.txt', 'MyTheme')


#def replace_in_file(in_path, out_path, reps):
#   
#    with open(in_path, 'r') as f:
#        data = f.read()
#
#    for repl in reps:
#        data = data.replace(repl[0],repl[1])
#
#    with open(out_path, 'w') as f:
#        f.writelines(data)
#
#
#replace_in_file('test.txt', 'result.txt', (('bob', 'no'), ('jerry','chris')))

#def numsys(startint):
#    return (bin(startint), oct(startint), hex(startint))
#
#def getints(binnum, octnum, decnum, hexnum):
#    return [int(binnum, 2), int(octnum, 8), int(decnum), int(hexnum, 16)]
#
#def literals():
#    return getints('0b11110100001001000000', '0o3641100', 1000000, '0xf4240')
#
#print(numsys(1000000))