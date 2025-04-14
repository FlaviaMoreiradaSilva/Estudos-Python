##CALCULADORA usando funções##
a = int(input('Digite um inteiro a: '))
b = int(input('Digite um inteiro b: '))

def soma(a,b):
    s= a+b
    print("Soma:", s)

def sub(a,b):
    n= a-b
    print("\nSubtração:", n)

def mult(a,b):
    m= a*b
    print("\nMultiplicação:", m)

def div(a,b):
    if a>b:
        d = a/b
    else:
        d = b/a
    print("\nDivisão:", d)

soma(a,b)
sub(a,b)
mult(a,b)
div(a,b)


##PAR OU ÍMPAR##
def imparpar():
    a = int(input('Digite um inteiro para saber se é par ou ímpar: '))
    if (a % 2) == 0:
        print("O número é par!")
    else:
        print("O número é ímpar!")

imparpar()



##Tabuada##
def tabuada():
    a = int(input('Digite um inteiro para saber a sua tabuada: '))
    i=0
    while i<=10:
        mult = a*i
        print(a, "x", i, "= ", mult)
        i+=1

tabuada()



##CONTADOR##
def contador():
    for cont in range(100):
        print(cont)

contador()


##MAIOR NÚMERO##
def maiornumero():
    a = int(input('Digite um inteiro a: '))
    b = int(input('Digite um inteiro b: '))
    c = int(input('Digite um inteiro c: '))

    if a>b and a>c:
        print("O maior número é ", a)
    elif b>a and b>c:
        print("O maior número é ", b)
    else:
        print("O maior número é ", c)

maiornumero()


##CONVERSOR DE TEMPERATURA##
def conversor():
    temp = int(input('Digite a temperatura em graus Celsius: '))
    temp= (temp * 9/5) +32
    print("A temperatura em Fahrenheit é: ", temp)

conversor()


##VALIDA SENHA##
def validacao():
    senha = input('Digite uma senha com pelo menos 8 caracteres e uma letra maiúscula: ')
    if len(senha)>= 8:
        if senha.lower() == senha:
            print("Senha inválida! Digite pelo menos uma letra maiúscula.")
        else:
            print("Senha válida! Senha: ", senha)
    else:
        print("Senha inválida! Ela precisa ter pelo menos 8 caracteres.")

validacao()


