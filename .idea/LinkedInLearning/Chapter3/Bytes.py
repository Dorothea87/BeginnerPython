#Bytes
#common behind the scenes, rarely manipulated or modified directly
#just a sequence of data, used for streaming files, transmitting text without knowing the encoding, often used under the hood in Python libraries

print(bytes(4)) #creates an empty bytes object that is 4 bytes long, are immutable like tuples

print(bytes('😴', 'utf-8'))

smileyFace = bytes('🙈', 'utf-8')

print(smileyFace.decode('utf-8'))

#if we want something that is mutable we need a byte array, can be manipulated like a string
smileyFaceTwo = bytearray('🙈', 'utf-8')
print(smileyFaceTwo)

anotherVal = smileyFaceTwo[3] = int('88', 16)
print(anotherVal)