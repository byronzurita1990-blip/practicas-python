while True:
    print("\n=== MENU===")
    print("1. Ver Saldo")
    print("2. Depositar")
    print("3. salir")

    opciones = input("Elije una opcion: ")

    if opciones == "1" :
        print("Tu saldo es: ")
    elif opciones == "2" :
        monto = input("Ingrese el valor que desea depositar: ")
        print(f"Su deposito se a realizado correctamente {monto} $")
    elif opciones == "3" :
        print ("gracias por visitarnos ")
        break
    else: 
        print("numero no existe gracias")
        exit()