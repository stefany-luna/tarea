N = int(input("Ingrese el valor de N: "))

suma_impares = 0
n = 1

while n <= N:
    
    if n % 2 != 0:
        
        suma_impares += n
    
    
    n += 1

print(f"La suma de los números impares entre 1 y {N} es {suma_impares}.")
