# Atividade: Listas, Tuplas e Dicionários



# 1. CADASTRO DE FILMES

filmes = ["Vingadores", "Harry Potter", "Enrolados", "Toy Story", "Homem-Aranha"]

print("----- 1. CADASTRO DE FILMES -----")

# 2. Exibir todos os filmes
print("Filmes cadastrados:")
print(filmes)

# 3. Exibir o primeiro filme
print("Primeiro filme:", filmes[0])

# 4. Exibir o último filme
print("Último filme:", filmes[-1])

# 5. Adicionar um novo filme
filmes.append("Interestelar")
print("Depois de adicionar:", filmes)

# 6. Inserir um filme em uma posição específica
filmes.insert(2, "Frozen")
print("Depois de inserir:", filmes)

# 7. Remover um filme
filmes.remove("Toy Story")
print("Depois de remover:", filmes)

# 8. Alterar o nome de um filme
filmes[0] = "Vingadores: Ultimato"
print("Depois de alterar:", filmes)

# 9. Quantidade de filmes
print("Quantidade de filmes:", len(filmes))

# 10. Verificar se um filme está presente
if "Harry Potter" in filmes:
    print("Harry Potter está na lista.")
else:
    print("Harry Potter não está na lista.")



# 2. CONTROLE DE NOTAS

print("\n----- 2. CONTROLE DE NOTAS -----")

notas = [7.5, 8.0, 6.5, 9.0, 8.5]

# 2. Exibir todas as notas
print("Notas:", notas)

# 3. Calcular a soma
soma = 0

for nota in notas:
    soma = soma + nota

print("Soma das notas:", soma)

# 4. Calcular a média
media = soma / len(notas)
print("Média:", media)

# 5. Maior nota
print("Maior nota:", max(notas))

# 6. Menor nota
print("Menor nota:", min(notas))

# 7. Verificar se existe nota igual a 10
if 10 in notas:
    print("Existe uma nota igual a 10.")
else:
    print("Não existe uma nota igual a 10.")

# 8 e 9. Verificar aprovação
if media >= 7:
    print("Estudante aprovado.")
else:
    print("Estudante reprovado.")


# 3. INFORMAÇÕES DE UM PRODUTO
print("\n----- 3. INFORMAÇÕES DO PRODUTO -----")

produto = ("Notebook", "Informática", 3500.00, 101)

# 1. Exibir cada informação individualmente
print("Nome:", produto[0])
print("Categoria:", produto[1])
print("Preço:", produto[2])
print("Código:", produto[3])

# 2. Exibir todas as informações com repetição
print("\nTodas as informações:")

for informacao in produto:
    print(informacao)

# 3. Quantidade de informações
print("Quantidade de informações:", len(produto))

# 4. Tentar alterar uma informação
# produto[0] = "Computador"

# 5. Explicação
print("Não é possível alterar uma informação da tupla.")
print("As tuplas são imutáveis.")


# 4. CADASTRO DE FUNCIONÁRIO

print("\n----- 4. CADASTRO DE FUNCIONÁRIO -----")

funcionario = {
    "nome": "Carlos",
    "idade": 25,
    "cargo": "Programador",
    "salario": 3500.00,
    "setor": "Tecnologia"
}

# 1. Exibir cada informação
print("Nome:", funcionario["nome"])
print("Idade:", funcionario["idade"])
print("Cargo:", funcionario["cargo"])
print("Salário:", funcionario["salario"])
print("Setor:", funcionario["setor"])

# 2. Alterar o salário
funcionario["salario"] = 4000.00
print("Novo salário:", funcionario["salario"])

# 3. Adicionar uma nova informação
funcionario["email"] = "carlos@email.com"
print("Email:", funcionario["email"])

# 4. Remover uma informação
del funcionario["email"]

# 5. Verificar se uma chave existe
if "cargo" in funcionario:
    print("A chave 'cargo' existe.")
else:
    print("A chave 'cargo' não existe.")

# 6. Percorrer o dicionário
print("\nDados do funcionário:")

for chave, valor in funcionario.items():
    print(chave, ":", valor)


# 5. SISTEMA DE ESTOQUE
print("\n----- 5. SISTEMA DE ESTOQUE -----")

estoque = [
    {
        "nome": "Notebook",
        "categoria": "Informática",
        "preco": 3500.00,
        "quantidade": 8
    },
    {
        "nome": "Mouse",
        "categoria": "Periféricos",
        "preco": 80.00,
        "quantidade": 25
    },
    {
        "nome": "Teclado",
        "categoria": "Periféricos",
        "preco": 150.00,
        "quantidade": 7
    },
    {
        "nome": "Monitor",
        "categoria": "Informática",
        "preco": 900.00,
        "quantidade": 12
    },
    {
        "nome": "Headset",
        "categoria": "Periféricos",
        "preco": 200.00,
        "quantidade": 5
    }
]

# 1. Exibir todos os produtos
print("Produtos cadastrados:")

for produto in estoque:
    print(produto)


# 2. Exibir nome, preço e quantidade
print("\nNome, preço e quantidade:")

for produto in estoque:
    print("Nome:", produto["nome"])
    print("Preço:", produto["preco"])
    print("Quantidade:", produto["quantidade"])
    print()


# 3. Calcular quantidade total de itens
quantidade_total = 0

for produto in estoque:
    quantidade_total = quantidade_total + produto["quantidade"]

print("Quantidade total de itens:", quantidade_total)


# 4. Calcular valor total do estoque
valor_total = 0

for produto in estoque:
    valor_total = valor_total + (produto["preco"] * produto["quantidade"])

print("Valor total do estoque: R$", valor_total)


# 5. Produtos com menos de 10 unidades
print("\nProdutos com menos de 10 unidades:")

for produto in estoque:
    if produto["quantidade"] < 10:
        print(produto["nome"])


# 6. Verificar se determinado produto está cadastrado
produto_procurado = "Mouse"
encontrado = False

for produto in estoque:
    if produto["nome"] == produto_procurado:
        encontrado = True

if encontrado:
    print("\nO produto", produto_procurado, "está cadastrado.")
else:
    print("\nO produto", produto_procurado, "não está cadastrado.")


# 7. Alterar quantidade de um produto
for produto in estoque:
    if produto["nome"] == "Mouse":
        produto["quantidade"] = 30

print("\nQuantidade do Mouse alterada para 30.")


# 8. Adicionar um novo produto
novo_produto = {
    "nome": "Webcam",
    "categoria": "Periféricos",
    "preco": 250.00,
    "quantidade": 15
}

estoque.append(novo_produto)

print("Novo produto adicionado:", novo_produto)


# 9. Relatório final
print("\n----- RELATÓRIO FINAL DO ESTOQUE -----")

for produto in estoque:
    print("Nome:", produto["nome"])
    print("Categoria:", produto["categoria"])
    print("Preço: R$", produto["preco"])
    print("Quantidade:", produto["quantidade"])
    print("-------------------------")