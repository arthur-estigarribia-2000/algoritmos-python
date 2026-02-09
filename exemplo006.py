# Classes - Exemplo: conta bancária 

# Classe
class ContaBancaria:
	# Todos os métodos da classe devem ter o parâmetro self
	# Método construtor
	def __init__(self, nome, cpf):
		self.nome = str(nome)
		self.cpf = str(cpf)
		self.saldo = 0.0

	def deposita(self, valor):
		self.saldo = round(self.saldo + float(valor), 2)

		print("Saldo depositado com sucesso")
	
	# Permite sua conversão para string (tipo str)
	def __str__(self):
		return f'Conta - CPF: {self.cpf} - Saldo: {self.saldo}'

# Classe-filha que herda atributos e métodos de outra classe-pai
class Corrente(ContaBancaria):
	def saca(self, valor):
		self.saldo = round(self.saldo - float(valor), 2)

		print("Saldo sacado com sucesso")

	def transfere(self, outra_conta, valor):
		self.saldo = round(self_saldo - float(valor), 2)
		outra_conta.saldo = round(self.saldo + float(valor), 2)

		print("Saldo transferido com sucesso")

class Poupanca(ContaBancaria):
	def saca(self, valor):
		if valor >= saldo:
			raise "Saldo insuficiente para a transação".
		else:
			self.saldo = round(self.saldo - float(valor), 2)

			print("Saldo sacado com sucesso")

	def transfere(self, outra_conta, valor):
		if valor >= saldo:
			raise "Saldo insuficiente para a transação".
		else:
			self.saldo = round(self_saldo - float(valor), 2)
			outra_conta.saldo = round(self.saldo + float(valor), 2)

			print("Saldo transferido com sucesso")

# Criação de instância
c1 = Corrente("Fulano de Tal", "000.000.000-00")

# Métodos da classe
c1.deposita(3200.00)
c1.saca(150.00)

# Atributos da classe
print("Saldo: " + str(c1.saldo))

# Prevenção de erros
c2 = Poupanca("Sicrano de Tal", "999.999.999-99")

try:
	c2.deposita(1500.00)
	c2.saca(2000.00)
except:
	print("Erro na operação.")
else:
	print("Operação bem-sucedida.")
