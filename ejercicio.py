nombre = input ("¿Como te llamas?")
años = input ("¿cuantos años tienes?")
Pais = input ("¿De donde eres?")
edad = int(años)
if edad >= 18:
    print("usted puede estudiar python")
else:
    print("termine el colegio")
print (f"!hola, {nombre}, {edad} años, soy de  {Pais}  Bienvenido al mundo de Python. ")