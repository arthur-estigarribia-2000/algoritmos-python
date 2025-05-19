# Decisão - Exemplo: maioridade penal no Brasil

# O tipo de dados int trabalha com inteiros positivos ou negativos
idade = int(input('Digite a idade em anos: '))

# Estrutura de decisão if-elif-else
# Dentro de estruturas, a indentação (em espaços ou tabs) é obrigatória e cumulativa
# Operadores lógicos aceitos no Python 3: == (igual), != (diferente), < (menor), > (maior), <= (menor ou igual) e >= (maior ou igual)
if idade < 0:
	# Este bloco é executado quando a condição acima for verdadeira (valor booleano True) e as demais condições da estrutura são ignoradas
	print('Idade inválida. ')
elif idade < 18:
	# Se a condição do bloco anterior for falsa, mas esta for verdadeira, executa este bloco e ignora os posteriores
	print('Menor de idade. ')
else:
	# O bloco else é executado quando todas as condições anteriores forem falsas (valor booleano False)
	print('Maior de idade. ')
