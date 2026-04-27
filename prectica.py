contraseña = "nandolike2010"

contraseña_input = input("Introduce tu contraseña: ")
   
if  contraseña_input != contraseña:
    print("Datos incorectos ")
    print("intentalo mas tarde")
    quit()
else:
    print("dotos correctos ")
    print("estas adentro: ")


# encontramos dos maneras de la condicon IF para permitri accesos y prosegir
# estamos elaborando el acceso con una contraseña para permitir que se siga registrando 
# tambien tiene un acceso de prohibicion si es menor de edad para mayor segurodad en el acceso



edad = int(input("ingresa tu edad: "))
if edad >= 18:
    print("mayor de edad segir preguntando")
    nombre = input("Ingresa tu nombre: ")
    pais = input("¿De donde eres:?")
    mensaje = ("hola mundo")
    print(f"!hola programador, {nombre} bienvenido a tu primera pagina {mensaje} {pais}")
else:
    print("menor de edad")
    
    
    
