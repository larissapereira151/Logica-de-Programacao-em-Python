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

'''
## 2. Controle de notas

Crie um programa para armazenar as notas de um estudante. O programa deverá:

1. Criar uma lista contendo 5 notas.
2. Exibir todas as notas.
3. Calcular a soma das notas.
4. Calcular a média das notas.
5. Identificar a maior nota.
6. Identificar a menor nota.
7. Verificar se existe uma nota igual a 10.
8. Informar se o estudante foi aprovado ou reprovado.
9. Considerar média igual ou superior a 7 como aprovação.'''

# 1. Criar uma lista contendo 5 notas
notas = [8.5, 7.0, 9.5, 6.0, 10.0]

# 2. Exibir todas as notas
print("Notas do estudante:", notas)

# 3. Calcular a soma das notas
soma = sum(notas)
print("Soma das notas:", soma)

# 4. Calcular a média das notas
media = soma / len(notas)
print("Média das notas:", media)

# 5. Identificar a maior nota
maior = max(notas)
print("Maior nota:", maior)

# 6. Identificar a menor nota
menor = min(notas)
print("Menor nota:", menor)

# 7. Verificar se existe uma nota igual a 10
if 10 in notas:
        print("Existe uma nota igual a 10.")
else:
        print("Não existe uma nota igual a 10.")

# 8 e 9. Verificar se o estudante foi aprovado ou reprovado
# Média igual ou superior a 7 = aprovado
if media >= 7:
        print("Estudante aprovado!")
else:
        print("Estudante reprovado!")

'''
## 3. Informações de um produto

Crie um programa para armazenar informações de um produto utilizando uma tupla. A tupla deverá armazenar:

1. Nome do produto.
2. Categoria.
3. Preço.
4. Código do produto.

O programa deverá:

1. Exibir cada informação individualmente.
2. Exibir todas as informações utilizando uma estrutura de repetição.
3. Informar a quantidade de informações armazenadas.
4. Tentar alterar uma das informações da tupla.
5. Observar e explicar o que acontece ao tentar modificar um elemento.'''

# Criando a tupla
produto = ("Notebook", "Eletrônicos", 3500.00, "NB001")

# 1. Exibir cada informação individualmente
print("Nome:", produto[0])
print("Categoria:", produto[1])
print("Preço:", produto[2])
print("Código:", produto[3])

# 2. Exibir todas as informações utilizando uma estrutura de repetição
print("Todas as informaçoes:")

for informacao in produto:
    print(informacao)

# 3. Informar a quantidade de informações armazenadas
print("Quantidade de informações:", len(produto))

# 4. Tentar alterar uma informação da tupla
print("Tentando alterar o nome do produto...")

try:
    produto[0] = "Celular"
except TypeError:
    print("Erro: não é possível alterar uma informação da tupla.")

# 5. Explicação
print("\nExplicação:")
print("As tuplas são imutáveis, ou seja, depois de criadas,")
print("não podemos alterar seus elementos.")

'''## 4. Cadastro de funcionário

Crie um programa para armazenar os dados de um funcionário utilizando um dicionário.

O cadastro deverá possuir:

1. Nome.
2. Idade.
3. Cargo.
4. Salário.
5. Setor.

O programa deverá:

1. Exibir cada informação do funcionário.
2. Alterar o salário do funcionário.
3. Adicionar uma nova informação ao cadastro.
4. Remover uma informação do cadastro.
5. Verificar se determinada chave existe.
6. Percorrer o dicionário exibindo as chaves e seus respectivos valores.'''

# Criando o dicionário
funcionario = {
    "nome": "Carlos",
    "idade": 25,
    "cargo": "Analista",
    "salario": 3000.00,
    "setor": "Tecnologia"
}

# 1. Exibir cada informação do funcionário
print("Nome:", funcionario["nome"])
print("Idade:", funcionario["idade"])
print("Cargo:", funcionario["cargo"])
print("Salário:", funcionario["salario"])
print("Setor:", funcionario["setor"])

# 2. Alterar o salário do funcionário
funcionario["salario"] = 3500.00

print("\nSalário após alteração:", funcionario["salario"])

# 3. Adicionar uma nova informação ao cadastro
funcionario["cidade"] = "Joinville"

print("\nNova informação adicionada:")
print("Cidade:", funcionario["cidade"])

# 4. Remover uma informação do cadastro
del funcionario["idade"]

print("\nCadastro após remover a idade:")
print(funcionario)

# 5. Verificar se determinada chave existe
if "cargo" in funcionario:
    print("\nA chave 'cargo' existe no cadastro.")
else:
    print("\nA chave 'cargo' não existe no cadastro.")

# 6. Percorrer o dicionário exibindo as chaves e seus respectivos valores
print("\nDados do funcionário:")

for chave, valor in funcionario.items():
    print(chave, ":", valor)

