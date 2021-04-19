my_list = ["a", 1, True]
my_list[2] = False
print(my_list)

# Append - Adiciona um valor ao final da lista.
my_list.append(10)

# Clear - Remove todos os valores em uma lista.
my_list.clear()

# Copy - Faz uma cópia da lista
my_other_list = ["a", 1, "2"]
my_list = my_other_list.copy()

# Remove - Remove um item da lista, se existir na lista
print(my_list)
my_list.remove(1)  # Procura na lista e remove o item
print(my_list)

# Count - Conta a quantidade de itens que é igual ao argumento passado.
l = [1, 2, 3, 4, 5, 5, 5, 5]
print(l.count(1))  # 1
print(l.count(5))  # 4

# Extend - Adiciona em uma lista os valores de outra lista.
l.extend([6, 7, 8])
print(l)

# Index - Retorna o index do argumento passado, retorna assim que encontrar.
print(l.index(5))

# Insert - Pega um index e um valor e adiciona o valor na lista.
# Obs: Se tiver um valor no index, esse valor irá para o index
# superior, não substituindo os valores.


l.insert(4, "Incrível")  # Retorna None
print(l)

# Pop - Retira o valor da lista, se for dado um index como argumento
# retira o valor nesse index.
l.pop(4)
print(l)

# Remove - Procura na lista o argumento passado e retira a primeira
# ocorrência.
l.remove(5)
print(l)

# Reverse - Reverte a lista. Isso muda a lista original
l.reverse()
print(l)

# Sort - Organiza a lista em ordem crescente, isso muda a lista.
l.sort()
print(l)

# Slicing lists
# Retorna algumas partes da lista, dependendo do range que for
# solicitado. Não muda a lista, apenas retorna os valores dos ranges
# list[start:end:step]
l[::-1]  # Retorna a lista ao contrário
l[::-2]  # Retorna a lista ao inverso de dois em dois
l[:5]  # Retorna do ínicio até o index 5
l[4:]  # Retorna a lista do indice 4 até o final

# Interação de listas e compreensão

# for in -> Interação de listas.
values = [1, 2, 3, 4]

for val in values:
    print(val)

for char in "awesome":
    print(char)

    # As vezes é necessário utilizar o index e o valor da lista,
    # Para isso utiliza-se a função enumerate() com a lista como
    # argumento.

for idx, char in enumerate("awesome"):
    print(idx, char)

# while
i = 0
while i < 5:
    print(i)
    i += 1

# Continue and break

for num in [1, 2, 3, 4, 5, 6, 7]:
    if num % 2 == 0:
        continue  # Pula uma interação
    elif num > 5:
        break  # Sai da interação
    print(num)

# Range -> range(start, stop, step), o stop não é contabilizado.
for num in range(4, 10):
    print(num)

# chr -> Transforma um número ASCII em caracteres dessa tabela.
capital_letters = []
for num in range(65, 91):
    capital_letters.append(chr(num))

print(capital_letters)

# Compreensão de lista - Formas de declarar lista, mas de forma resumida
print([chr(num) for num in range(65, 91)])

# Código sem compreensão de lista
vowels = []
for letter in 'awesome':
    if letter in ['a', 'e', 'i', 'o', 'i']:
        vowels.append(letter)

print(vowels)

# Código com compreensão de lista
print([letter for letter in 'awesome' if letter in ['a', 'e', 'i', 'o', 'u']])
