# Operações
# Exemplo: porcentagem

# O método input(mensagem) consiste em obter os dados digitados no console (linha de comando)
# É necessário converter o valor obtido para ponto flutuante decimal (tipo float) para efetuar operações numéricas usando float(valor)
valor = float(input('Digite o valor total ou inicial: '))
porcentagem = float(input('Digite o percentual: '))

# Operadores numericos aceitos no Python 3: + (soma ou concatenação), - (subtração), * (multiplicação), / (quociente da divisão), % (rest da divisãoo) e ** (potência)
taxa = porcentagem / 100

parte = valor * taxa

# O comanod print(texto) retorna o dado no console
# É necessário converter todos os valores para str na concatenação (operador + entre dois str)
print('Parte: ' + str(parte))

aumento = valor + parte
desconto = valor - parte

print('Aumento: ' + str(aumento))
print('Desconto: ' + str(desconto))
