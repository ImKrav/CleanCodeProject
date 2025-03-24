from src.classes.Autenticador import Autenticador
from src.classes.GestorDeContactos import GestorDeContactos
from src.classes.Usuario import Usuario
from src.classes.Contacto import Contacto
from src.classes.GestorVCF import GestorVCF
from src.errors import ErrorListaVaciaDeContactos, ErrorArchivoCorrupto, ErrorNoVCF, ErrorPermisosDeEscritura, ErrorNombreVacio, CategoriaNoExistente, IDNoEncontrado

def mostrar_menu_principal():
    print("\n--- Menú Principal ---")
    print("1. Registrarse")
    print("2. Iniciar sesión")
    print("3. Salir")

def mostrar_menu_funcionalidades():
    print("\n--- Menú de Funcionalidades ---")
    print("1. Crear un contacto")
    print("2. Editar un contacto")
    print("3. Ver la lista de contactos")
    print("4. Buscar un contacto")
    print("5. Filtrar contactos")
    print("6. Exportar contactos")
    print("7. Importar contactos")
    print("8. Cerrar sesión")

def main():
    autenticador = Autenticador()
    gestor_contactos = None
    usuario_actual = None

    while True:
        if not usuario_actual:
            mostrar_menu_principal()
            opcion = input("Seleccione una opción: ")

            if opcion == "1":  # Registrarse
                nombre = input("Nombre de usuario: ")
                email = input("Email: ")
                password = input("Contraseña: ")
                try:
                    nuevo_usuario = Usuario(len(autenticador.usuarios) + 1, nombre, email, password)
                    autenticador.registrar_usuario(nuevo_usuario)
                    usuario_actual = nuevo_usuario  # Solo se asigna si no hay errores
                    gestor_contactos = GestorDeContactos(usuario_actual)
                    print(f"Usuario '{nombre}' registrado exitosamente.")
                except Exception as e:
                    print(f"Error al registrarse: {e}")

            elif opcion == "2":  # Iniciar sesión
                email = input("Email: ")
                password = input("Contraseña: ")
                try:
                    usuario_actual = autenticador.iniciar_sesion(email, password)
                    gestor_contactos = GestorDeContactos(usuario_actual)
                    print(f"Inicio de sesión exitoso. Bienvenido, {usuario_actual.nombre}.")
                except Exception as e:
                    print(f"Error al iniciar sesión: {e}")

            elif opcion == "3":  # Salir
                print("Saliendo del sistema. ¡Hasta luego!")
                break

            else:
                print("Opción no válida. Intente nuevamente.")
        else:
            mostrar_menu_funcionalidades()
            opcion = input("Seleccione una opción: ")

            if opcion == "1":  # Crear un contacto
                try:
                    id_contacto = len(usuario_actual.contactos) + 1
                    nombre = input("Nombre: ")
                    telefono = input("Teléfono: ")
                    email = input("Email: ")
                    direccion = input("Dirección: ")
                    categoria = input("Categoría (Personal, Trabajo, Sin asignar): ")
                    contacto = gestor_contactos.agregar_contacto(id_contacto, nombre, telefono, email, direccion, categoria)
                    print(f"Contacto '{contacto.nombre}' creado exitosamente.")
                except Exception as e:
                    print(f"Error al crear contacto: {e}")

            elif opcion == "2":  # Editar un contacto
                try:
                    id_contacto = int(input("ID del contacto a editar: "))
                    nombre = input("Nuevo nombre (dejar vacío para no cambiar): ")
                    telefono = input("Nuevo teléfono (dejar vacío para no cambiar): ")
                    email = input("Nuevo email (dejar vacío para no cambiar): ")
                    direccion = input("Nueva dirección (dejar vacío para no cambiar): ")
                    categoria = input("Nueva categoría (dejar vacío para no cambiar): ")
                    gestor_contactos.editar_contacto(id_contacto, nombre, telefono, email, direccion, categoria)
                    print("Contacto actualizado exitosamente.")
                except IDNoEncontrado:
                    print("Error: Contacto no encontrado.")
                except Exception as e:
                    print(f"Error al editar contacto: {e}")

            elif opcion == "3":  # Ver la lista de contactos
                try:
                    contactos = gestor_contactos.ver_contactos()
                    if not contactos:
                        print("No tienes contactos en tu lista.")
                    else:
                        print("\n--- Lista de Contactos ---")
                        for contacto in contactos:
                            print(f"ID: {contacto.id} | Nombre: {contacto.nombre} | Teléfono: {contacto.telefono} | Email: {contacto.email} | Dirección: {contacto.direccion} | Categoría: {contacto.categoria}")
                except Exception as e:
                    print(f"Error al mostrar la lista de contactos: {e}")

            elif opcion == "4":  # Buscar un contacto
                try:
                    nombre = input("Ingrese el nombre exacto del contacto a buscar: ")
                    contacto = gestor_contactos.buscar_contacto(nombre)
                    if contacto:
                        print("\n--- Contacto Encontrado ---")
                        print(f"ID: {contacto.id} | Nombre: {contacto.nombre} | Teléfono: {contacto.telefono} | Email: {contacto.email} | Dirección: {contacto.direccion} | Categoría: {contacto.categoria}")
                    else:
                        print("No se encontró un contacto con ese nombre.")
                except ErrorNombreVacio:
                    print("Error: El nombre no puede estar vacío.")
                except Exception as e:
                    print(f"Error al buscar contacto: {e}")

            elif opcion == "5":  # Filtrar contactos por nombre y categoría
                try:
                    nombre = input("Nombre (dejar vacío para no filtrar por nombre): ")
                    categoria = input("Categoría (dejar vacío para no filtrar por categoría): ")
                    contactos_filtrados = gestor_contactos.filtrar_contacto(categoria) if categoria else gestor_contactos.buscar_contacto(nombre)
                    print("\nContactos filtrados:")
                    for contacto in contactos_filtrados:
                        print(f"- {contacto.nombre} ({contacto.categoria})")
                except Exception as e:
                    print(f"Error al filtrar contactos: {e}")

            elif opcion == "6":  # Exportar contactos a .vcf
                archivo = input("Nombre del archivo .vcf para exportar: ")
                try:
                    gestor_vcf = GestorVCF(usuario_actual)
                    gestor_vcf.exportar_contactos(usuario_actual.contactos, archivo)
                    print(f"Contactos exportados exitosamente a '{archivo}'.")
                except ErrorListaVaciaDeContactos:
                    print("Error: La lista de contactos está vacía.")
                except ErrorPermisosDeEscritura:
                    print("Error: No tienes permisos de escritura en el directorio de destino.")
                except Exception as e:
                    print(f"Error al exportar contactos: {e}")

            elif opcion == "7":  # Importar contactos desde .vcf
                archivo = input("Nombre del archivo .vcf para importar: ")
                try:
                    gestor_vcf = GestorVCF(usuario_actual)
                    contactos_importados = gestor_vcf.importar_contactos(archivo)
                    usuario_actual.contactos.extend(contactos_importados)
                    print(f"Contactos importados exitosamente desde '{archivo}'.")
                except ErrorArchivoCorrupto:
                    print("Error: El archivo está corrupto o no se puede cargar.")
                except ErrorNoVCF:
                    print("Error: El archivo no tiene la extensión .vcf.")
                except Exception as e:
                    print(f"Error al importar contactos: {e}")

            elif opcion == "8":  # Cerrar sesión
                print(f"Sesión cerrada. Hasta luego, {usuario_actual.nombre}.")
                usuario_actual = None
                gestor_contactos = None

            else:
                print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    main()