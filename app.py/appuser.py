def User():
    usuário = input("Digite seu Login: ")
    return usuário

def usuárioUpper(usuário):
    if not usuário[0].isupper():
        return False
    else:
        return True
        
def usuárioSpace(usuário):
    if " " in usuário:
        return False
    else:
        return True

def usuárioSpecial(usuário):
    if any(not c.isalnum() for c in usuário):
        return False
    else:
        return True

def usuáriocaractere(usuário):
    if len(usuário) > 30:
        return False
    else:
        return True