'''
1. Cadastro de filmes

Crie um programa para organizar uma lista de filmes. O programa deverá:

1. Criar uma lista contendo inicialmente 5 filmes.
2. Exibir todos os filmes cadastrados.
3. Exibir o primeiro filme da lista.
4. Exibir o último filme da lista.
5. Adicionar um novo filme ao final da lista.
6. Inserir um novo filme em uma posição específica.
7. Remover um filme da lista.
8. Alterar o nome de um dos filmes.
9. Exibir a quantidade de filmes cadastrados.
10. Verificar se um determinado filme está presente na lista. '''

#1:
filmes = ["Justice League", "Spider-man", "Batman", "Superman", "Iron Man"]

#2:
print("\nFilmes cadastrados: ")
print(filmes)

#3:
print("\nPrimeiro filme: ")
print(filmes[0])

#4:
print("\nÚltimo filme: ")
print(filmes[-1])

#5:
filmes.append("Ant Man")
print(filmes)

#6:
filmes.insert(1,"Captain America")
print(filmes)

#7:
filmes.remove("Superman")
print(filmes)

#8:
filmes[0] = "Avengers"
print(filmes)

#9:
print(f"\nA quantidade total de filmes é: {len(filmes)}")

#10:
if "Batman" in filmes:
    print("\nBatman está na lista")
else:
    print("\nBatman não está na lista")