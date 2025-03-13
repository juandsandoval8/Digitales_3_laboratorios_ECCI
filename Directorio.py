# Lista para almacenar los datos de las personas
directorio = []

# Mensajes que se mostrarán en pantalla
mensajes = {
    "bienvenida": "Bienvenido al directorio telefónico",
    "nombre": "Digite el nombre completo (nombre y apellido): ",
    "telefono": "Digite el teléfono celular: ",
    "cumpleanos": "Digite la fecha de cumpleaños (DD/MM): ",
    "correo": "Digite el correo electrónico: ",
    "despedida": "Gracias por usar el directorio telefónico. ¡Hasta luego!",
    "opcion_invalida": "Opción no válida. Intente de nuevo."
}

# Mensaje de bienvenida
print(mensajes["bienvenida"])

# Bucle principal del programa
while True:
    # Mostrar el menú
    print("\n--- Menú ---")
    print("1. Agregar un nuevo registro")
    print("2. Buscar una persona por teléfono celular")
    print("3. Borrar un registro")
    print("4. Salir de la aplicación")

    # Pedir al usuario que seleccione una opción
    opcion = input("Seleccione una opción: ")

    # Opción 1: Agregar un nuevo registro
    if opcion == "1":
        print(mensajes["nombre"])
        nombre = input()
        print(mensajes["telefono"])
        telefono = int(input())
        print(mensajes["cumpleanos"])
        cumpleanos = input()
        print(mensajes["correo"])
        correo = input()

        # Crear un diccionario con los datos de la persona
        persona = {
            "nombre": nombre,
            "telefono": telefono,
            "cumpleanos": cumpleanos,
            "correo": correo
        }

        # Agregar la persona al directorio
        directorio.append(persona)
        print("Registro agregado con éxito.")

    # Opción 2: Buscar una persona por teléfono
    elif opcion == "2":
        telefono = int(input("Digite el teléfono celular a buscar: "))
        encontrado = False  # Variable para saber si se encontró la persona
        for i in directorio:
            if i["telefono"] == telefono:
                print(f"Nombre: {i['nombre']}, Teléfono: {i['telefono']}, Cumpleaños: {i['cumpleanos']}, Correo: {i['correo']}")
                encontrado = True
                break
        if not encontrado:
            print("No se encontró ninguna persona con ese teléfono.")

    # Opción 3: Borrar un registro
    elif opcion == "3":
        telefono = int(input("Digite el teléfono celular del registro a borrar: "))
        encontrado = False  # Variable para saber si se encontró la persona
        for i in directorio:
            if i["telefono"] == telefono:
                directorio.remove(i)
                print("Registro borrado con éxito.")
                encontrado = True
                break
        if not encontrado:
            print("No se encontró ninguna persona con ese teléfono.")

    # Opción 4: Salir de la aplicación
    elif opcion == "4":
        print(mensajes["despedida"])
        break

    # Opción no válida
    else:
        print(mensajes["opcion_invalida"])
