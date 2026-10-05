#O que é uma função:

#Uma função é um bloco de código criado para realizar uma determinada tarefa
#Ela permite organizar e reutilizar código.

# 1. Criando uma função
#Utilizar a palavra DEF para uma função.

def saudacao():
    print("Olá seja bem-vindo")

saudacao()

# 2. Criando uma função com parâmetro
#Parâmetros permitem enviar informações para a função.

def saudacao(nome):
    print(f"Olá {nome}")
saudacao("Ana")
saudacao("João")

# 3. Mais de um parâmetro

def apresentar(nome, idade):
    print(f"nome: {nome}")
    print(f"idade: {idade}")

apresentar("Maria",17)
apresentar("João",20)

# 4. Função com cálculo

def somar(numero1, numero2):
    resultado = numero1 + numero2
    print(f"resultado: {resultado}")

somar( 10, 20)
somar( 10, 90)

# 5. Retornando um Valor

def somar(numero1, numero2):
    return numero1 + numero2
print(somar(10,5))

# 6. função com condição
def vereficarIdade(idade):
    if idade >= 18:
        return "Maior idade"
    else:
        return "Menor idade"
print(vereficarIdade(20))

# 7. Parâmetro com valor padrão
def saudacao(nome = "Aluno"):
    print (f"Ola {nome}")

    saudacao("João")
    saudacao(nome)

# 8. Função utilizando lista
def calcularMedia(notas):

    soma = 0
    for nota in notas:
        soma += nota
    return soma/len(notas)
notas = [8, 7, 9, 10]
media = calcularMedia(notas)
print(f"Média das notas: {media}")
