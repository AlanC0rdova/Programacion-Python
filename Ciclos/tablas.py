#alan
#tablas de multiplicar

n = int(input("Ingresa de que numero quieres saber sus tablas "))
print(f"la tabla de multiplicar de {n} es: ")

for j in range(n):
 print(" ")
 for i in range(10):#da el rango de mult
    mul =(j+1)*(i+1)
    print(f"{j+1} X {i+1} = {mul}")
    i=0


