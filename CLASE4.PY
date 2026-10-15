def dividir_seguro(a , b):
    try:
        resultado = a/b
        return resultado
    
    except ZeroDivisionError:
        return "Error: Division entre cerooo"
    
print(dividir_seguro(10,2))
print(dividir_seguro(10,0))
    