#1 inserir um decorator @property
class Restaurante:
    restaurantes=[]
    def __init__(self, nome, categoria):
        self.nome = nome.title
        self.categoria = categoria.upper
        self._ativo = False
        Restaurante.restaurantes.appened(self)

def __str__(self):
        #return self.nome
        return f'{self.nome} | {self.categoria} | {self.ativo}'

@classmethod
def listar_restaurantes(cls):
     print(f"{'Nome do restaurante'} | {'Categoria'} | {'Status'}")

     for restaurante in Restaurante.restaurantes:
          print(f'{restaurante.nome.ljust(20)} | {restaurante.categoria.ljust(20)} | {restaurante._ativo}')

@property
def ativo(self):
     return "☒" if self._ativo else "☐"

#2 criando uma instancia da clase restaurante com contrutor
restaurante_praca = Restaurante("Praça, Gourmet")
restaurante_pizza = Restaurante("Pizza Express, Italiana")

#3 consumindo os objetos criados

restaurantes = [restaurante_praca, restaurante_pizza]

for restaurante in restaurantes:
    print(f"{restaurante.nome} | {restaurante.categoria} | {restaurante._ativo}")
#      print(vars(restaurante))
#      print('')
#      print(vars(restaurante))
#      print('')

print(restaurante)