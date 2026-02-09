# Listas
# Exemplo: registros de bandas

# Declaração de uma lista (array) com tipos homogêneos
bandas = ["Linkin Park", "Evanescence", "Simple Plan", "Muse", "Avenged Sevenfold", "Green Day"]

# Mostra o elemento na posição inteira indicada (as posições de 0 a n - 1)
print(str(bandas[1]))

# Acrescenta o elemento ao final da lista
bandas.append("Spiritbox")
bandas.append("Bad Omens")

# Mostra todos os valores no console
print(str(bandas))

# O método nativo len(lista) retorna o tamanho (a quantidade de elementos) da lista (retorna um valor do tipo int)
pos = len(bandas)
print(str(pos))

# Remoção de um elemento pelo índice; a remoção do elemento no índice 1 removerá o 2º elemento da lista (na ordenação humana normal)
bandas.pop(3)

print(bandas)

# Cópia da lista: a lógica usual lista2 = lista faz referência dinâmica mutável e não cópia, para cópia, usa-se copy.deepcopy(array), que exige a importação (import copy)
import copy

numetal = copy.deepcopy(bandas)

numetal.pop(2)

print("Tamanho da lista inicial: " + str(len(bandas)))
print("Tamanho da lista das bandas de nu-metal: " + str(len(numetal)))

# Loop for, utilizado com arrays, onde a variável iteradora (i) assume cada elemento do array

for i in numetal:
  print("É banda de nu-metal: " + str(i) + "!")
