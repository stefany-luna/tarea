a=int(input("entero"))
n=int(input("cantidad de sumas"))
i=1
suma = 0
while i <=n:
    suma += (1/a)**i
    print(suma)
    i+= 1
print(f"la sumatoria para {n} terminos es {suma}")