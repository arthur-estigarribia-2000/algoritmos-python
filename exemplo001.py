# Operações - Exemplo: aproveitamento de um time no Campeonato Brasileiro de Futebol

# Entrada de dados
# O método input(mensagem) permite a entrada de dados no terminal, a mensagem é um str (texto entre aspas duplas) e o método retorna str que deve ser convertido para int com str(variavel)
vitorias = int(input("Digite o número de vitórias: "))
empates = int(input("Digite o número de empates: "))
derrotas = int(input("Digite o número de derrotas: "))

# Processamento de dados
# Operadores numéricos (int/float) aceitos em Python: + (soma), - (subtração), * (multiplicação), / (divisão), % (resto) e ** (potência)
pontos = 3 * vitorias + 1 * empates + 0 * derrotas
jogos = vitorias + empates + derrotas
total = 3 * jogos

# É preciso converter int para float com float(variavel); os operadores em Python não aceitam tipos diferentes
aproveitamento = (float(pontos) / float(total)) * 100.0

# Saída de dados
# O método print(mensagem) efetua a saída de dados no terminal
# O método round(decimal, casas) efetua o arredondamento para exibir com um número determinado (0-15) de casas decimais
# O operador + entre duas str efetua a concatenação; é preciso converter float para str com str(variavel) para ser concatenado corretamente
print("Aproveitamento: " + str(round(aproveitamento, 2)))
