class Vehiculo:  
    def __init__(self, marca, h):       
        self.marca = marca  
        self.h = h       
    
    def arrancar(self): 
         print("El vehículo arranca") 
           
class Coche(Vehiculo):
    def __init__(self, marca,h, num_puertas):    
        super().__init__( marca, h)   
        self.num_puertas = num_puertas 
                   
     # Prueba 
coche = Coche("Toyota", 4) 
print(f"Marca: {coche.marca}, Puertas: {coche.num_puertas}") 
coche.arrancar() 
