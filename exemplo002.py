# Decisão
# Exemplo: maioridade penal no Brasil

# O tipo de dados int trabalha com inteiros positivos ou negativos
idade = int(input('Digite a sua idade em anos: '))

# Estrutura de decisão if-elif-else
# Dentro de estruturas, a indentação (em espaços ou tabs) é obrigatória e cumulativa
# Operadores lógicox aceitos no Python 3: == (igual), != (diferente), < (menor), > (maior), <= (menor ou igual) e >= (maior ou igual)
if idade < 0:
	# Este bloco é executado quando a condição acima for verdadeira (valor booleano True) e as demais condições da estrutura são ignoradas
	print('Idade inválida. ')
elif idade < 18:
	print('Menor de idade. ')
else:
	# Este bloco e executado quando todas as condições forem falsas (valor booleano False)
	print('Maior de idade. ')
