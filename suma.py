num1 = input ("Introduce el primer numero: ")
num2 = input ("Introde el segundo numero: ")
num3 = input ("Introduce el tercer numero: ")
resultado = int(num1) + int(num2) + int(num3)
promedio = int(resultado) / 3 

print ("la suma de las notas es: ", resultado)
print ("el promedio es: ", promedio)
if promedio >= 7 :
    print ("usted pasa de año. ")
    print("siga asi ")
else:
    print("pierde el año. ") 
    print("usted va a supletorio")