class Nadador:
    def nadar(self):
        print("Nadador")
        
class Volador:
    def volar(self):
        print("volador")
        
class Pato(Nadador, Volador):
    def __init__(self, nombre):
        self.nombre = nombre
    
    def graznar(self):
        print("cuaci")
        
pato = Pato("Mario")
pato.nadar()
pato.volar()
pato.graznar()
