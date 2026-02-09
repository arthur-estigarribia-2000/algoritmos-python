# Listas
# Exemplo: registros de bandas

# Declaração de uma lista (array) com tipos homogêneos
bandas = ['Linkin Park', 'Evanescence', 'Simple Plan', 'Muse', 'Avenged Sevenfold', 'Green Day']

# Mostra o elemento na posição inteira indicada (as posições de 0 a n - 1)
print(str(bandas[1]))

# Acrescenta o elemento ao final da lista
bandas.append('Spiritbox')
bandas.append('Bad Omens')

# Mostra todos os valores no console
print(str(bandas))

# O método nativo len(lista) retorna o tamanho (a quantidade de elementos) da lista (retorna um valor do tipo int)
pos = len(lista)
print(str(pos))

# Remoção de um elemento pelo índice
lista.pop(pos - 1)

# A remoção do elemento no índice 1 removerá o 2º elemento da lista (na ordenação humana normal)
lista.pop(1)

print(lista)

# Cópia da lista
import copy

# A lógica usual lista2 = lista faz referência dinâmica mutável e não cópia, para cópia, usa-se copy.deepcopy(array), que exige a importação (import copy)
lista2 = copy.deepcopy(lista)

lista2.pop(2)

print('Tamanho da lista inicial: ' + str(len(lista)))
print('Tamanho da lista 2: ' + str(len(lista2)))
