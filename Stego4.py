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
    msgList = list(msg + sentinel())

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
        characterInt = (int(byteString,2))
        if characterInt == ord(sentinel()):
            return ''.join(charList)
        charList.append(chr(characterInt))
    
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

testTuple = read_pgm('result.txt')

encode_pgm('Jello','test.txt','result.txt')
print(decode_pgm('result.txt'))