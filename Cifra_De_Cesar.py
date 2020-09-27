#obtem os caracteres
def get_strs():
    array = []
    
    for ID_ in range(ord("a"), ord("z") + 1):
        caractere = chr(ID_)
        array.append(caractere)
    return array

#faz a autenticação na chave de criptografia
def key_Variable(key):
    if 0 < key < 26:
        return True
    return False

#se a chave for inválida irá retornar um erro
def value_KEY():
   if not key_Variable(key):
        return "Erro (valor de chave inválida)\ntente colocando key > 0 "

#para cifrar será usado duas atribuições "TEXT" e "key"
def encrypt(TEXT, key = 3):
    TEXT = TEXT.lower()
    array = get_strs()
    new_TEXT = ""

    for caractere in TEXT:
        position = array.index(caractere)
        position += key
        new_Caractere = array[position % len(array)]
        new_TEXT += new_Caractere
    return new_TEXT.upper()

#responsável por decifrar
def decrypt(TEXT, key = 3):
    TEXT = TEXT.lower()
    array = get_strs()
    new_TEXT = ""

    for caractere in TEXT:
        position = array.index(caractere)
        position -= key
        new_Caractere = array[position]
        new_TEXT += new_Caractere
    return new_TEXT.upper()
user1 = ""

#laço WHILE para que enquanto USER1 for diferente de "n" executa o bloco de código
while user1 != "n":
    print("Bem vindo ao CRIPT E DECRIPT")
    print("[1] para criptografar")
    print("[2] para descriptografar")
    option = input(str("SELECT: "))

    if option == "1":
        input__STR__CT = input(str("Digite o texto para criptografar: "))
        select__KEY = int(input("Digite a KEY: "))
        print(encrypt(input__STR__CT, select__KEY))

    elif option == "2":
        input__STR__DT = input(str("Digite o texto para descriptografar: "))
        select__KEY = int(input("Digite a chave de cifra: "))
        print(decrypt(input__STR__DT, select__KEY))

    user1 = str(input("Deseja continuar? (s/n)"))
else:
    print("até a próxima! ;) ")
