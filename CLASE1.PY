class Producto:
    
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.__precio = precio
        
    @property
    def precio(self):
        return self.__precio
    
    @precio.setter
    def precio(self, nuevo_precio):
        if nuevo_precio > 0:
            self.__precio = nuevo_precio
        else:
            print("EL precio debe ser positivo")
            
#prueba
producto = Producto("laptop", 1000)
print(producto.precio)
producto.precio = 1200
print(producto.precio)
producto.precio = -500
print(producto.precio)        
        
  