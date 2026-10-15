def conteo_sensores_presencia():
    try:
        matriz = []
        zonas_activas = 0
        
        print("--- Matriz de Sensores de Presencia (2x2) ---")
        print("Ingrese '1' para presencia detectada o '0' para ausencia.\n")
        
        # Lectura de la matriz 2x2
        for i in range(2):
            fila = []
            for j in range(2):
                valor = int(input(f"Ingrese el estado del sensor [{i + 1}][{j + 1}]: "))
                
                # Validación de datos binarios
                if valor not in (0, 1):
                    raise ValueError("Solo se permite ingresar el valor 0 o 1.")
                
                fila.append(valor)
                if valor == 1:
                    zonas_activas += 1
            matriz.append(fila)

        # Mostrar la matriz construida
        print("\nMatriz de sensores ingresada:")
        for fila in matriz:
            print(fila)
            
        print(f"\nTotal de zonas activas encontradas: {zonas_activas}")

    except ValueError as ve:
        print(f"Error de entrada: {ve}")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")

# Ejecución del programa
conteo_sensores_presencia()