while True:
    # Solicitar al usuario que ingrese un número
    num = input("Ingresa un número entero (o 'salir' para terminar): ")

    # Verificar si el usuario quiere salir
    if num.lower() == 'salir':
        print("¡Hasta luego!")
        break

    # Intentar convertir la entrada del usuario a un número entero
    try:
        num = int(num)
        # Determinar si el número es par o impar
        if num % 2 == 0:
            print(f"{num} es un número par.")
        else:
            print(f"{num} es un número impar.")
    except ValueError:
        print("Por favor, ingresa un número entero válido o escribe 'salir' para terminar.")