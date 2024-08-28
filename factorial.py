while True:
    # Solicitar al usuario el número para calcular el factorial
    numero = int(input("Ingrese un número entre 0 y 20: "))

    # Verificar que el número esté en el rango permitido
    if numero < 0 or numero > 20:
        print("Número fuera del rango. Debe estar entre 0 y 20.")
        continue  # Volver a pedir el número si está fuera del rango

    # Inicializar el acumulador del factorial
    factorial = 1

    # Calcular el factorial usando un bucle
    i = 1
    while i <= numero:
        factorial *= i
        i += 1

    # Mostrar el resultado
    print(f"El factorial de {numero} es {factorial}.")

    # Volver a empezar el bucle sin preguntar
    continue

