#Alan Adrian Cordova Vazquez 250199
#Progreama que calcula la calificacion final 

#variables

c1 = int(input("Parcial 1: "))
c2 = int(input("Parcial 2: "))
c3 = int(input("Parcial 3: "))
ex = int(input("Calificacion final examen: "))
tf = int(input("Valor del trabajo final: "))

#promedios:

promedio = ((c1+c2+c3)/3)
parcial = (promedio*.55)
pexamn = (ex*.30)
ptf = (tf*.15) #ptf es promedio trabajo final
final = (parcial+pexamn+ptf) #calculo final

#impresion final

print(f"La calificacion final es: {final:.1f}")#cantidad de decimales

