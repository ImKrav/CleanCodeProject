from src.model.classes.autenticador import Autenticador
from src.model.classes.gestor_de_contactos import GestorDeContactos
from src.model.classes.usuario import Usuario
from src.model.classes.contacto import Contacto
from src.model.classes.gestor_vcf import GestorVCF
from src.model.errors import (
    ErrorListaVaciaDeContactos,
    ErrorArchivoCorrupto,
    ErrorNoVCF,
    ErrorPermisosDeEscritura,
    ErrorNombreVacio,
    ErrorTelefonoNoNumerico,
    IDNoEncontrado,
    ErrorCorreoInvalido,
    CategoriaNoExistente,
)

def mostrar_menu_principal():
    """
    Muestra por pantalla las opciones del menú principal:
      1. Registrarse
      2. Iniciar sesión
      3. Salir
    """
    print("\n--- Menú Principal ---")
    print("1. Registrarse")
    print("2. Iniciar sesión")
    print("3. Salir")

def mostrar_menu_funcionalidades():
    """
    Muestra por pantalla las opciones del menú de funcionalidades
    para el usuario autenticado:
      1. Crear un contacto
      2. Editar un contacto
      3. Ver la lista de contactos
      4. Buscar un contacto
      5. Filtrar contactos
      6. Exportar contactos
      7. Importar contactos
      8. Cerrar sesión
    """
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
    """
    Punto de entrada de la aplicación.
    Controla el flujo de navegación entre el menú principal y el de funcionalidades,
    maneja registro, login y operaciones sobre contactos.
    """
    autenticador = Autenticador()
    gestor_contactos = None
    usuario_actual = None

    while True:
        if not usuario_actual:
            mostrar_menu_principal()
            opcion = input("Seleccione una opción: ")

            if opcion == "1":  # Registrarse
                print("\n--- Registro de Usuario ---")
                nombre = input("Nombre de usuario: ")
                email = input("Email: ")
                password = input("Contraseña: ")
                try:
                    nuevo_usuario = Usuario(len(autenticador.usuarios) + 1, nombre, email, password)
                    autenticador.registrar_usuario(nuevo_usuario)
                    usuario_actual = nuevo_usuario
                    gestor_contactos = GestorDeContactos(usuario_actual)
                    print(f"Usuario '{nombre}' registrado exitosamente.")
                except ErrorCorreoInvalido as e:
                    print(f"Error: {e}")
                except Exception as e:
                    print(f"Error al registrarse: {e}")

            elif opcion == "2":  # Iniciar sesión
                print("\n--- Iniciar Sesión ---")
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
                print("\n--- Crear Contacto ---")
                try:
                    nombre = input("Nombre: ")
                    telefono = input("Teléfono: ")
                    email = input("Email: ")
                    direccion = input("Dirección: ")
                    categoria = input("Categoría (Personal, Trabajo, Sin asignar): ")
                    if categoria == "":
                        categoria = "Sin asignar"
                    contacto = gestor_contactos.agregar_contacto(Contacto(len(usuario_actual.contactos) + 1, nombre, telefono, email, direccion, categoria))
                    print(f"Contacto '{contacto.id} - {contacto.nombre}' creado exitosamente.")
                except Exception as e:
                    print(f"Error al crear contacto: {e}")

            elif opcion == "2":  # Editar un contacto
                print("\n--- Editar Contacto ---")
                try:
                    id_contacto = int(input("ID del contacto a editar: "))
                    nombre = input("Nuevo nombre (dejar vacío para no cambiar): ")
                    telefono = input("Nuevo teléfono (dejar vacío para no cambiar): ")
                    email = input("Nuevo email (dejar vacío para no cambiar): ")
                    direccion = input("Nueva dirección (dejar vacío para no cambiar): ")
                    categoria = input("Nueva categoría (dejar vacío para no cambiar): ")
                    contacto = gestor_contactos.editar_contacto(Contacto(id_contacto, nombre, telefono, email, direccion, categoria))
                    print(f"Contacto '{contacto.id} - {contacto.nombre}' actualizado exitosamente.")
                except IDNoEncontrado:
                    print("Error: Contacto no encontrado.")
                except ErrorCorreoInvalido as e:
                    print(f"Error: {e}")
                except CategoriaNoExistente as e:
                    print(f"Error: {e}")
                except Exception as e:
                    print(f"Error al editar contacto: {e}")

            elif opcion == "3":  # Ver la lista de contactos
                print("\n--- Lista de Contactos ---")
                try:
                    contactos = gestor_contactos.ver_contactos()
                    if not contactos:
                        print("No tienes contactos en tu lista.")
                    else:
                        for contacto in contactos:
                            print(f"ID: {contacto.id} | Nombre: {contacto.nombre} | Teléfono: {contacto.telefono} | Email: {contacto.email} | Dirección: {contacto.direccion} | Categoría: {contacto.categoria}")
                except Exception as e:
                    print(f"Error al mostrar la lista de contactos: {e}")

            elif opcion == "4":  # Buscar un contacto
                print("\n--- Buscar Contacto ---")
                try:
                    nombre = input("Ingrese el nombre exacto del contacto a buscar: ")
                    contactos = gestor_contactos.buscar_contacto(nombre)
                    if contactos:
                        for contacto in contactos:
                            print(f"ID: {contacto.id} | Nombre: {contacto.nombre} | Teléfono: {contacto.telefono} | Email: {contacto.email} | Dirección: {contacto.direccion} | Categoría: {contacto.categoria}")
                    else:
                        print("No se encontró un contacto con ese nombre.")
                except ErrorNombreVacio:
                    print("Error: El nombre no puede estar vacío.")
                except Exception as e:
                    print(f"Error al buscar contacto: {e}")

            elif opcion == "5":  # Filtrar contactos por nombre y categoría
                print("\n--- Filtrar Contactos ---")
                try:
                    nombre = input("Nombre (dejar vacío para no filtrar por nombre): ")
                    categoria = input("Categoría (dejar vacío para no filtrar por categoría): ")
                    contactos_filtrados = gestor_contactos.filtrar_contacto(nombre=nombre, categoria=categoria)
                    print("\nContactos filtrados:")
                    for contacto in contactos_filtrados:
                        print(f"- {contacto.nombre} ({contacto.categoria})")
                except CategoriaNoExistente as e:
                    print(f"Error: {e}")
                except Exception as e:
                    print(f"Error al filtrar contactos: {e}")

            elif opcion == "6":  # Exportar contactos a .vcf
                print("\n--- Exportar Contactos ---")
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
                print("\n--- Importar Contactos ---")
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
                print("\n--- Cerrar Sesión ---")
                print(f"Sesión cerrada. Hasta luego, {usuario_actual.nombre}.")
                usuario_actual = None
                gestor_contactos = None

            else:
                print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    main()