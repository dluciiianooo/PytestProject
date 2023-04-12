from cryptographyFramework import *

initializeWrite()
user = "Douglas"
password = "123456"
encryptedText = encryptMessage(user, password, "Primeira mensagem secreta!")
saveNewLine(encryptedText)
encryptedText = encryptMessage(user, password, "Segunda mensagem secreta!")
saveNewLine(encryptedText)

