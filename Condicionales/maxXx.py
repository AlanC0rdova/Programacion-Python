#Alan Adrian 250199
#maximo de dos numeros 

n1 = float(input("Ingresa un valor: "))
n2 = float(input("Ingresa un segundo valor: "))
n3 = float(input("Ingresa un tercer valor: "))

#----------------------------------------------

#proceso
if n1>n2:
    if n1>n3:
        max = n1
    else:
        max=n3
else:
    if n2>n3:
        max=n2
    else:
        max=n3

        #impremir   

print(f"El numero mayor es: {max}")



    
    
