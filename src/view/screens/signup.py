from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
from src.model.classes.autenticador import Autenticador
from src.model.classes.usuario import Usuario

class Signup(Screen):
    """
    Pantalla de registro de nuevos usuarios.

    Hereda de kivy.uix.screenmanager.Screen. Permite a los usuarios
    crear una cuenta proporcionando nombre, correo electrónico y contraseña.
    """

    def __init__(self, **kwargs):
        """
        Inicializador de la pantalla de registro.

        Configura el autenticador y llama al constructor de la superclase.
        """
        super().__init__(**kwargs)
        self.autenticador = Autenticador()

    def registrarse(self, nombre, email, password):
        """
        Registra un nuevo usuario en el sistema.

        Parámetros:
            nombre (str): Nombre completo del usuario.
            email (str): Dirección de correo electrónico del usuario.
            password (str): Contraseña para la cuenta del usuario.

        Comportamiento:
            - Calcula un nuevo ID de usuario basado en la longitud
              de la lista actual de usuarios.
            - Crea una instancia de Usuario y la registra con el
              Autenticador.
            - Actualiza la etiqueta de error para mostrar éxito o
              cualquier excepción ocurrida.

        Excepciones capturadas:
            Exception: Cualquier error durante el proceso de registro,
            mostrando el mensaje de la excepción en la interfaz.
        """
        try:
            nuevo_id = len(self.autenticador.usuarios) + 1
            nuevo_usuario = Usuario(nuevo_id, nombre, email, password)
            
            self.autenticador.registrar_usuario(nuevo_usuario)
            
            self.ids.error_label.text = "Registro exitoso. Ahora puedes iniciar sesión."
            self.ids.error_label.color = (0, 1, 0, 1)
        except Exception as e:
            self.ids.error_label.text = f"Error al registrarse: {e}"
            self.ids.error_label.color = (1, 0, 0, 1)