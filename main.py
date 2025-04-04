from usuarios import crear_usuario, listar_usuarios, actualizar_usuario, eliminar_usuario

def mostrar_menu():
    print("\n--- Menú CRUD de Usuarios ---")
    print("1. Crear usuario")
    print("2. Listar usuarios")
    print("3. Actualizar usuario")
    print("4. Eliminar usuario")
    print("5. Salir")

def iniciar():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            nombre = input("Nombre: ")
            correo = input("Correo: ")
            edad = input("Edad: ")
            crear_usuario(nombre, correo, edad)

        elif opcion == '2':
            listar_usuarios()

        elif opcion == '3':
            try:
                id_usuario = int(input("ID del usuario a actualizar: "))
                nombre = input("Nuevo nombre: ")
                correo = input("Nuevo correo: ")
                edad = input("Nueva edad: ")
                actualizar_usuario(id_usuario, nombre, correo, edad)
            except ValueError:
                print("❌ ID inválido.")

        elif opcion == '4':
            try:
                id_usuario = int(input("ID del usuario a eliminar: "))
                eliminar_usuario(id_usuario)
            except ValueError:
                print("❌ ID inválido.")

        elif opcion == '5':
            print("👋 Saliendo del programa. ¡Hasta luego!")
            break

        else:
            print("❌ Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    iniciar()
