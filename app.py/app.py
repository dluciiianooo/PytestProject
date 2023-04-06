from appmessage import *
from appuser import *
from apppassword import*
from re import *

# Função para validar se a senha atende aos requisitos
def validar_senha(Password):
    if len(Password) <= 10:
        return False
    if not any(char.isdigit() for char in Password):
        return False
    if not any(char.islower() for char in Password):
        return False
    if not any(char.isupper() for char in Password):
        return False
    if not any(char in '!@#$%^&*()_-+=[{]}\|;:",<.>/?' for char in Password):
        return False
    return True

# Solicita login e senha do usuário
login = input("Digite seu login: ")
senha = input("Digite sua senha: ")

# Criptografa Message
def Message():
    message = input("Informe a mensagem a ser criptografada: ")
    return message    
    
def caracteremax(message):
    if len(message) > 70:
        return False
    else:
        return True
