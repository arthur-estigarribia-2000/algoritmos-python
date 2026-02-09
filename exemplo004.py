# Funções - Exemplo: calculadora de porcentagem

# Estrutura de função def
# Permite a reutilização de código que seria repetido muitas vezes
# Pode ter vários parâmetros, mas apenas um retorno
# Indentação obrigatória e cumulativa (com outras estruturas)
def porcentagem(taxa, valor):
	return (float(taxa) / 100) * float(valor)

def aumento(taxa, valor):
	return float(valor) + float(porcentagem(taxa, valor))

def desconto(taxa, valor):
	return aumento(-float(taxa), float(valor))

v0 = float(input("Digite o valor inicial: "))
p = float(input("Digite a taxa de variação: "))

# Chamada de método
t = porcentagem(p, v)
aum = aumento(p, v)
des = desconto(p, v)

# O método nativo round(numero, casas) usa o arredondamento para exibir o número decimal com um número especificado (0-15) de casas decimais
print("Taxa: " + str(round(t, 2)))
print("Aumento: " + str(round(aum, 2)))
print("Dewsconto: " + str(round(des, 2)))
