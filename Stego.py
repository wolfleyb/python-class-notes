#def invert(l):
#   for i, pixel in enumerate(l):
#       l[i] = str(255 - int(pixel))
#    
#
#def inverted(l):
#    return [str(255 - int(pixel)) for pixel in l]


#def steg_encode_char(char, cover):
#    msgBin = format(ord(char), '0>8b')
#    msgBinL = list(msgBin)
#
#    for i, msgBit in enumerate(msgBinL):
#        coverInt = int(cover[i])
#        coverBin = format(coverInt, '0>8b')
#        coverBinL = list(coverBin)
#        coverBinL[-1] = msgBit
#        cover[i] = str(int(''.join(coverBinL),2))
#    
#    print(cover)

def write_pgm(filename, content):

    writeContent = ''

    for el in content:
        writeContent += '/n'.join(el) + '/n'

    with open(filename, 'w') as dest:
        dest.write(writeContent)

#def invert(content):
#    pixelValL = content[1]
#    invertedPixelValL = []
#    for pixel in pixelValL:
#        invertedPixelValL.append(str(255 - int(pixel)))
#
#    content = (content[0],invertedPixelValL)
#    header = []
#    body = []
#    Line = None
#
#
#
#def invert(content):
#    pixelValL = content[1]
#    invertedPixelValL = []
#    for pixel in pixelValL:
#        invertedPixelValL.append(str(255 - int(pixel)))
#
#    content = (content[0],invertedPixelValL)
#
#
#        
#
#def write_pgm(filename, content):
#
#    writeContent = ''
#
#    for el in content:
#        writeContent = '/n'.join(el) + '/n'
#
#    with open(filename, 'w') as dest:
#        dest.write(writeContent)
#
#def invert(content):
#    pixelValL = content[1]
#    invertedPixelValL = []
#    for pixel in pixelValL:
#        invertedPixelValL.append(str(255 - int(pixel)))
#
#    content = (content[0],invertedPixelValL)
#    for i, pixel in enumerate(stego):
#        pixelInt = int(pixel)
#        pixelBin = format(pixelInt, '0>8b')
#
#        myCharList.append(pixelBin[-1])
#
#    myChar = chr(int(''.join(myCharList),2))
#    return myChar
#
#



    






#def read_pgm(filename):
#    header = []
#    body = []
#    Line = None
#
#    with open(filename, 'r') as src:
#        
#        while Line != '255':
#            Line = src.readline().strip()
#            header.append(Line)
#    
#        Line = None
#        counter = 0
#        while Line != '':
#            Line = src.readline().strip()
#            body.append(Line)
#
#    return (header, body)


        




#
#
#def pread_pgm(filename):
#    with open(filename) as f:
#        data = f.read()
#    content = data.split()
#    tuple = ()
#    tuple = tuple + (content[0:4],)
#    tuple = tuple + (content[4:],)
#    return tuple
#
#def pwrite_pgm(filename,content):
#    f = open(filename)
#    writer = ''
#    for item in content:
#        writer = "\n".join(item) + "\n"
#        f.write(writer)
#    f.close()
#
#
#def pinvert(content):
#    data = list(content)
#    index = 0
#    for item in data[1]:
#        newPixel = str(255 - int(item))
#        data[1][index] = newPixel
#        index += 1
#    content = tuple(data)
#
#
#def read_pgm(filename):
#    header = []
#    body = []
#    Content = ''
#
#    with open(filename, 'r') as src:
#        data = src.read()
#    Content = data.split()
#    header = Content[:4]
#    body = Content[4:]
#
#    return (header, body)
#        
#
#def write_pgm(filename, content):
#
#    writeContent = ''
#
#    for el in content:
#        writeContent = '\n'.join(el) + '\n'
#
#    with open(filename, 'w') as dest:
#        dest.write(writeContent)
#
#def invert(content):
#    pixelValL = content[1]
#    invertedPixelValL = [str(255 - int(pixel)) for pixel in pixelValL]
#    content = (content[0],invertedPixelValL)
#
#
#print(read_pgm('test.txt'))

#def steg_encode(msg, cover):
#    msgList = list(msg)
#    coverCounter = 0
#    for char in msgList:
#        msgBin = format(ord(char), '0>8b')
#        msgBinL = list(msgBin)
#
#        for msgBit in msgBinL:
#            coverInt = int(cover[coverCounter])
#            coverBin = format(coverInt, '0>8b')
#            coverBinL = list(coverBin)
#            coverBinL[-1] = msgBit
#            cover[coverCounter] = str(int(''.join(coverBinL),2))
#            coverCounter += 1
#
#    
#    print(cover)
#
#def steg_decode_char(stego):
#    myCharList = []def read_pgm(filename):def read_pgm(filename):
#    header = []
#    body = []
#    Line = None
#
#    with open(filename, 'r') as src:
#        
#        while Line != '255':
#            Line = src.readline().strip()
#            header.append(Line)
#    
#        Line = None
#        counter = 0
#        while Line != '':
#            Line = src.readline().strip()
#            body.append(Line)
#
#    return (header, body)
#


def read_pgm(filename):
    with open(filename) as f:
        data = f.read()
    content = data.split()
    tuple = ()
    tuple = tuple + (content[0:4],)
    tuple = tuple + (content[4:],)
    return tuple



def write_pgm(filename, content):

    writeContent = ''

    for el in content:
        writeContent += '\n'.join(el) + '\n'

    with open(filename, 'w') as dest:
        dest.write(writeContent)



def steg_encode(msg, cover):
    msgList = list(msg)
    coverCounter = 0
    for char in msgList:
        msgBin = format(ord(char), '0>8b')
        msgBinL = list(msgBin)

        for msgBit in msgBinL:
            coverInt = int(cover[coverCounter])
            coverBin = format(coverInt, '0>8b')
            coverBinL = list(coverBin)
            coverBinL[-1] = msgBit
            cover[coverCounter] = str(int(''.join(coverBinL),2))
            coverCounter += 1



def steg_decode(stego):
    charList = []
    counter = 0

    while counter < len(stego):
        bitList = []
        for i in range(8):
            binEl = format(int(stego[counter]), '0>8b')
            bitList.append(binEl[-1])
            counter += 1

        byteString = ''.join(bitList)
        charList.append(chr(int(byteString,2)))
    
    return ''.join(charList)

def sentinel():
    return chr(128)

def encode_pgm(msg, coverfilename, outputfilename):
    content = read_pgm(coverfilename)
    coverBod = content[1]
    
    steg_encode(msg, coverBod)
    
    content = (content[0], coverBod)
    write_pgm(outputfilename, content)


def decode_pgm(filename):
    pgm = read_pgm(filename)
    decodeData = pgm[1]
    return steg_decode(decodeData)



#encode_pgm('Goodbye', 'test.txt', 'result.txt')
print(decode_pgm('result.txt'))


        
