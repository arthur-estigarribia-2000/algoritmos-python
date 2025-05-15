# Operadores
# Exemplo: cálculo de porcentagem

# O método input(mensagem) consiste em obter os dados digitados no console (linha de comando)
# É necessário converter o valor obtido para ponto flutuante decimal (tipo float) para efetuar operações numéricas usando float(valor)
entrada_valor = float(input('Digite o valor total ou inicial: '))
entrada_porcentagem = float(input('Digite o percentual: '))

# Operadores aceitos: + (soma ou concatenação), - (subtração), * (multiplicação), / (divisão), % (resto) e ** (potência)
taxa = porcentagem / 100

parte = valor_inicial * taxa

# O comanod print(texto) retorna o dado no console
# É necessário converter os dados para str na concatenação
print('Parte: ' + str(parte))

aumento = valor_inicial + parte
desconto = valor_inicial - parte

print('Aumento: ' + str(aumento))
print('Desconto: ' + str(desconto))
