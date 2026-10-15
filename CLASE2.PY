class Animal:
    def sonido(self):
        print("sonido generico")

class Perro(Animal):
    def sonido(self):
        print("Guao")
        
class Gato(Animal):
    def sonido(self):
        print("Miau")
        
#Prueba
animales = [Perro(), Gato(), Animal()]
for animal in animales:
    animal.sonido( )