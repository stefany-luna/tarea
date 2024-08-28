# Solicitar el valor de n (debe ser un entero positivo máximo de 9)
n = int(input("Ingrese el valor de n (1 a 9): "))

# Verificar que el valor de n esté en el rango permitido
while n < 1 or n > 9:
    print("El valor de n debe estar entre 1 y 9.")
    n = int(input("Ingrese el valor de n (1 a 9): "))

# Inicializar el contador para el exponente
x = 0

# Bucle para calcular n^x y mostrar los resultados
while x <= n:
    resultado = 1  # Inicializar el resultado de n^x en 1
    i = 0
    
    # Bucle para calcular n^x mediante multiplicaciones repetidas
    while i < x:
        resultado *= n
        i += 1
    
    # Imprimir el resultado
    print(f"{n}^{x} = {resultado}")
    
    # Incrementar el exponente
    x += 1
