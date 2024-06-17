#Questão 1
class Carro:
    def __init__(self, modelo, cor, ano):
        self.modelo = modelo
        self.cor = cor
        self.ano = ano

# Criando uma instância da classe Carro e atribuindo valores
meu_carro = Carro('Golf GTI', 'Preto', 2019)
print(f"Modelo: {meu_carro.modelo}, Cor: {meu_carro.cor}, Ano: {meu_carro.ano}")


#Questão 2
class Restaurante:
    def __init__(self, nome, categoria, ativo, endereco, capacidade):
        self.nome = nome
        self.categoria = categoria
        self.ativo = ativo
        self.endereco = endereco
        self.capacidade = capacidade

# Instanciando um restaurante e atribuindo valores aos seus atributos
restaurante1 = Restaurante("Forno Mágico", "Pizzas", True, "Rua das Flores, 123", 100)
print(f"Nome: {restaurante1.nome}, Categoria: {restaurante1.categoria}, Ativo: {restaurante1.ativo}, Endereço: {restaurante1.endereco}, Capacidade: {restaurante1.capacidade}")


#Questão 3
class Restaurante:
    def __init__(self, nome, categoria, endereco, capacidade):
        self.nome = nome
        self.categoria = categoria
        self.ativo = False
        self.endereco = endereco
        self.capacidade = capacidade

# Criando uma instância utilizando o construtor
restaurante2 = Restaurante("Rota", "Rodízio", "Avenida Central, 456", 150)
print(f"Nome: {restaurante2.nome}, Categoria: {restaurante2.categoria}, Ativo: {restaurante2.ativo}, Endereço: {restaurante2.endereco}, Capacidade: {restaurante2.capacidade}")


#Questão 4
class Restaurante:
    def __init__(self, nome, categoria, endereco, capacidade):
        self.nome = nome
        self.categoria = categoria
        self.ativo = False
        self.endereco = endereco
        self.capacidade = capacidade

    def __str__(self):
        return f"Restaurante: {self.nome}, Categoria: {self.categoria}"

# Exibindo uma mensagem para uma instância de restaurante
restaurante3 = Restaurante("Óleos Divinos", "Pastel", "Rua do Fogo, 789", 60)
print(restaurante3)


#Questão 5
class Cliente:
    def __init__(self, nome, idade, email, telefone):
        self.nome = nome
        self.idade = idade
        self.email = email
        self.telefone = telefone

# Instanciando 3 objetos da classe Cliente e atribuindo valores aos seus atributos
cliente1 = Cliente("João da Silva", 30, "joao.silva@example.com", "1234-5678")
cliente2 = Cliente("Maria Oliveira", 25, "maria.oliveira@example.com", "2345-6789")
cliente3 = Cliente("Pedro Souza e Souza", 35, "pedro.souza@example.com", "3456-7890")

# Exibindo os detalhes dos clientes
print(f"Cliente 1: Nome: {cliente1.nome}, Idade: {cliente1.idade}, Email: {cliente1.email}, Telefone: {cliente1.telefone}")
print(f"Cliente 2: Nome: {cliente2.nome}, Idade: {cliente2.idade}, Email: {cliente2.email}, Telefone: {cliente2.telefone}")
print(f"Cliente 3: Nome: {cliente3.nome}, Idade: {cliente3.idade}, Email: {cliente3.email}, Telefone: {cliente3.telefone}")