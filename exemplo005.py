# Listas
# Exemplo: registros de bandas

# Declaração de uma lista (array) com tipos homogêneos
bandas = ['Linkin Park', 'Evanescence', 'Simple Plan', 'Muse']

# Mostra o elemento na posição inteira indicada (as posições de 0 a n - 1)
print(str(bandas[1]))

# Acrescenta o elemento ao final da lista
bandas.append('Spiritbox')

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
