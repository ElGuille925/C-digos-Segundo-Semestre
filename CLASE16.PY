class CuentaBancaria:  
    def __init__(self, saldo_inicial):      
        self.__saldo = saldo_inicial   
               
        
    def depositar(self, cantidad):        
        if cantidad > 0:           
            self.__saldo += cantidad            
            print(f"Depósito exitoso. Nuevo saldo: ${self.__saldo}")          
            
    def retirar(self, cantidad):        
        if 0 < cantidad <= self.__saldo:            
            self.__saldo -= cantidad           
            print(f"Retiro exitoso. Nuevo saldo: ${self.__saldo}")        
        else:             
            print("Saldo insuficiente")  
            cuenta = CuentaBancaria(1000) 
            cuenta.depositar(500) 
            cuenta.retirar(300) 