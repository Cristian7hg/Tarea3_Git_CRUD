from utils import leer_datos, guardar_datos

def crear_usuario(nombre, correo, edad):
    usuarios = leer_datos()
    nuevo_id = max([u['id'] for u in usuarios], default=0) + 1
    nuevo_usuario = {
        "id": nuevo_id,
        "nombre": nombre,
        "correo": correo,
        "edad": edad
    }
    usuarios.append(nuevo_usuario)
    guardar_datos(usuarios)
    print("✅ Usuario creado con éxito.")

def listar_usuarios():
    usuarios = leer_datos()
    if not usuarios:
        print("📭 No hay usuarios registrados.")
    else:
        for usuario in usuarios:
            print(f"ID: {usuario['id']} | Nombre: {usuario['nombre']} | Correo: {usuario['correo']} | Edad: {usuario['edad']}")

def actualizar_usuario(id_usuario, nombre, correo, edad):
    usuarios = leer_datos()
    for usuario in usuarios:
        if usuario['id'] == id_usuario:
            usuario['nombre'] = nombre
            usuario['correo'] = correo
            usuario['edad'] = edad
            guardar_datos(usuarios)
            print("✅ Usuario actualizado correctamente.")
            return
    print("❌ Usuario no encontrado.")

def eliminar_usuario(id_usuario):
    usuarios = leer_datos()
    usuarios_filtrados = [u for u in usuarios if u['id'] != id_usuario]
    if len(usuarios) == len(usuarios_filtrados):
        print("❌ Usuario no encontrado.")
    else:
        guardar_datos(usuarios_filtrados)
        print("🗑️ Usuario eliminado con éxito.")
