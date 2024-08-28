n_notas = int(input("Ingrese el número de notas: "))

suma_notas = 0

contador = 0

while contador < n_notas:
    nota = float(input(f"Ingrese la nota {contador + 1} (0 a 5): "))
    
    while nota < 0 or nota > 5:
        print("¿que paso?. Debe estar entre 0 y 5.")
        nota = float(input(f"Ingrese la nota {contador + 1} (0 a 5): "))
    
    suma_notas += nota
    
    contador += 1

promedio = suma_notas / n_notas

print(f"El promedio de las notas es: {promedio:.2f}")
