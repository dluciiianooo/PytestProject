def Message():
    message = input("Escreva a Mensagem: ")
    return message    
    
def caracteremax(message):
    if len(message) > 70:
        return False
    else:
        return True