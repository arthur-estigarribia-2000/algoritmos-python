# Repetição - Exemplo: tabuada multiplicativa

# Entrada de um inteiro
numero = int(input('Digite um número inteiro: '))

# Contador
i = 0

# Estrutura de repetição while
# O bloco é executado enquanto a condição for verdadeira, parando apenas quando for falsa
# Indentação obrigatória e cumulativa
while i <= 10:
	resultado = i * numero

	# Saída de dados
	# A concatenação textual exige operandos do tipo str
	print(str(i) + ' * ' + str(numero) + ' = ' + str(resultado))

	# Para poder alterar o valor de i até que a condição seja falsa, devemos incrementar seu valor
	# Sem isso, o código fica em loop infinito, não parando devido à condição ser sempre verdadeira - é necessário mudar o valor da variável da condição para poder ter mais chances do loop ser encerrado (devido à condição falsa) e prossegue o código
	i = i + 1
