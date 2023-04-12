from appuser import*
from apppassword import*
from appmessage import*
def test_appuser():
    # Testa se o nome do usuário não tem mais de trinta caracteres.
    assert True == usuáriocaractere("Douglas")
    assert False == usuáriocaractere("DouglasDouglasDouglasDouglasDouglasDouglasDouglasDouglas")
    # Testa se não contêm algum espaço dentro do nome do usuário.
    assert True == usuárioSpace("Douglas")
    assert False == usuárioSpace("Douglas Luciano silva")
    # Testa se não tem caracteres especiais.
    assert True == usuárioSpecial("Douglas")
    assert False == usuárioSpecial("@Douglas")
    # Testa se a primeira letra não é maiúscula.
    assert True ==  usuárioUpper("Douglas")
    assert False ==  usuárioUpper("douglas")

def test_password():
    # Testa se na senha pelo menos uma letra maiúscula.
    assert True == UpperPassword("@Douglas19")
    assert False == UpperPassword("@douglas19")
    # Testa se tem pelo menos uma letra minúscula.
    assert True == LowerPassword("@Douglas19")
    assert False == LowerPassword("@DOUGLAS19")
    # Testa se a senha possui pelo menos algum número.
    assert True == NumberPassword("@Douglas19")
    assert False == NumberPassword("@Douglas")
    # Testa se a senha possui caracteres especiais.
    assert True == SpecialPassword("@Douglas19")
    assert False == SpecialPassword("Douglas19")
    # Testa se a senha possui menos 10 caracteres.
    assert True == Passwordmin("@Douglas19")
    assert False == Passwordmin("@Do19")

def test_message():
    # Testa se a mensagem não possui mais de 70 caracter.
    assert  caracteremax("ooi, lo da dougl.") == True
    assert False == caracteremax("loko loko,loko loko,loko loko,loko loko,loko loko,loko loko,loko loko,loko loko,loko loko,loko loko,loko loko,loko loko")