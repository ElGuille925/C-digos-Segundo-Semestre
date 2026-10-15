class TemperaturaInvalidaError(Exception):
    pass

class Temperatura:
    def __init__(self, valor):
        if valor < -273.15:
            raise TemperaturaInvalidaError("Temperatura menor al cero absoluto")
        self.valor = valor
    
try:
    temp1 = Temperatura(25)
    print(f"Tempetatura: {temp1.valor}C")
    temp2 = Temperatura(-300)
    
except TemperaturaInvalidaError as e:
    print(f"Error: {e}")