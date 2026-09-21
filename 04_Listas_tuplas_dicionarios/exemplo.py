#Listas, tuplas e Dicionarios

#1. Listas
#Lista são utilizadas para armazenar varios valores dentro de uma unica variavel.

nomes = ["Ana","Carlos", "João","Maria"]
print(nomes)

#2. Acessando elementos da Lista
print(nomes[0])

#Podemos acessar o último elemento usando -1
print(nomes[-1])

#3. Alterando elementos
nomes[0] = "Pedro"
print(nomes)

#4. Adicionar Elementos

#append() adiciona um elemento no final da lista
nomes.append("Lucas")
print(nomes)

#insert() adiciona um elemento em uma posição especifica
nomes.insert(1,"Mariana")
print(nomes)

#5. Removendo elementos
# - REMOVE UM ELEMENTO PELO VALOR

nomes.remove("Lucas")
print(nomes)

#pop() remove um elemento pelo indice
nomes.pop(0)
print(nomes)

#6. Tamanho da lista
#len() informa a quantidade de elementos
print(len(nomes))

#7. Percorrendo uma lista
for nome in nomes:
    print(nome)

#8. Verificando se um elemento existe

if "João" in nomes:
 print("João está na lista")
else:
 print("João não está na lista")

# 9. Lista com diferentes tipos de dados

dados = ["João", 18, 1.75, True]
print(dados)

# 10. Lista de números
notas = [7.5, 8.0, 6.5, 9.0]

soma = 0

for nota in notas:
    soma = soma + nota

media = soma / len(notas)
print(f"Média: {media}"

# 11. Tuplas
# Tuplas são semelhantes às listas. As tuplas não podem ser alteradas.

coodernadas = (10, 20)
print(coodernadas)

print(coodernadas[0])

#12 Dicionários

#Dicinários armazenam informações no formato: chave: valor
aluno = {
    "nome": "Carlos",
    "idade": 17,
    "nota": 8.5
}

print(aluno)