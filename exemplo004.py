# Funções
# Exemplo: média de notas escolares

# Estrutura de função def
# Permite a reutilização de código que seria repetido muitas vezes
# Pode ter vários parâmetros, mas apenas um retorno
# Indentação obrigatória e cumulativa (com outras estruturas)
def media(nota1, nota2, nota3):
	soma = round(float(nota1) + float(nota2) + float(nota3), 1)
	razao = round(float(soma) / 3, 1)
	
	# O método round(numero, casas) é recomendado para evitar erros de máquina numa operação decimal
	# Pode ter de 0 a 15 casas decimais
	return round(media, 1)

# Entrada de dados
n1 = float(input('Digite a nota 1: '))
n2 = float(input('Digite a nota 2: '))
n3 = float(input('Digite a nota 3: '))

# Chamada do método já declarado (seu retorno será armazenado na variável m)
m = media(n1, n2, n3)

# Saída de dados
print('Média: ' + str(m))

if m >= 7.0:
	print('Aprovado. ')
else:
	print('Reprovado. ')
