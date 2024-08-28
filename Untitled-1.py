n1 = int(input("Ingrese el primer número entero:"))
n2 = int(input("Ingrese el segundo número entero:"))

producto = 0
contador = 0

while contador < n2:
    if contador == n2:
        break
    producto+= n1
    print(producto)
    contador+= 1

print(f"La multiplicación de {n1} y {n2} es {producto}.")
