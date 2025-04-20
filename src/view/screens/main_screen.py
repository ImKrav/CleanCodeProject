from kivy.uix.screenmanager import Screen

class MainScreen(Screen):
    def crear_contacto(self):
        print("Función para crear un contacto")

    def editar_contacto(self):
        print("Función para editar un contacto")

    def ver_contactos(self):
        print("Función para ver la lista de contactos")

    def buscar_contacto(self):
        print("Función para buscar un contacto")

    def filtrar_contactos(self):
        print("Función para filtrar contactos")

    def exportar_contactos(self):
        print("Función para exportar contactos")

    def importar_contactos(self):
        print("Función para importar contactos")

    def cerrar_sesion(self):
        self.manager.current = "login"  # Regresa a la pantalla de inicio de sesión