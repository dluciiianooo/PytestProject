from cryptographyFramework import *

initializeRead()
user = "Douglas"
password = "123456"
line1 = readNextLine()
print(line1)
print(decryptMessage(user, password, line1))
line2 = readNextLine()
print(line2)
print(decryptMessage(user, password, line2))