def Password():
    Password = input("Informe sua senha: ")
    return Password

def Passwordmin(Password):
    if len(Password) < 10:
        return False
    else:
        return True

def SpecialPassword(Password):
    if not any(not c.isalnum() for c in Password):
        return False
    else: 
        return True
    
def NumberPassword(Password):
    if any(i.isdigit() for i in Password):
        return True
    else:
        return False

def UpperPassword(Password):
    if any(char.isupper() for char in Password):
        return True
    else:
        return False

def LowerPassword(Password):
    if any(char.islower() for char in Password):
        return True
    else:
        return False