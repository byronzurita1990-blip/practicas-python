# condicional for 

numeros = [4, 8, 15 ,23, 42]
buscado = input("Ingrese el numero a buscar: ")

for numero in numeros:
    if numero == buscado:
        
        print(f"!Encontrando! El {buscado} esta en la lista ")
        break
    print(f"Revisando {numero}.... no es ")

else:
    print(f"El {buscado} no esta en la lista")

