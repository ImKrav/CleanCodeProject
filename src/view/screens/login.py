from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
from src.model.classes.autenticador import Autenticador
from src.model.errors import UsuarioNoExistente, ErrorContrasenaIncorrecta, LoginEspacioVacio

class Login(Screen):
    """
    Pantalla de inicio de sesión de la aplicación.

    Hereda de kivy.uix.screenmanager.Screen. Se encarga de recopilar
    las credenciales del usuario y delegar la validación en Autenticador.
    """
    def __init__(self, **kwargs):
        """
        Inicializador de la pantalla de login.

        Configura el autenticador y llama al constructor de la superclase.
        """
        super().__init__(**kwargs)
        self.autenticador = Autenticador()

    def iniciar_sesion(self, email, password):
        """
        Intenta iniciar sesión con el email y la contraseña proporcionados.

        Parámetros:
            email (str): Dirección de correo del usuario.
            password (str): Contraseña del usuario.

        Comportamiento:
            - Si el inicio es exitoso, muestra un mensaje de éxito,
              actualiza el usuario actual en el ScreenManager y cambia
              a la pantalla principal.
            - Si el usuario no existe, muestra un mensaje de error.
            - Si la contraseña es incorrecta, muestra un mensaje de error.
            - Si faltan campos, muestra un mensaje de error.

        Excepciones capturadas:
            UsuarioNoExistente
            ErrorContrasenaIncorrecta
            LoginEspacioVacio
        """
        try:
            usuario = self.autenticador.iniciar_sesion(email, password)
            self.ids.error_label.text = "Inicio de sesión exitoso"
            self.ids.error_label.color = (0, 1, 0, 1)
            self.manager.usuario_actual = usuario
            self.manager.current = "main"
        except UsuarioNoExistente:
            self.ids.error_label.text = "Error: El usuario no existe"
        except ErrorContrasenaIncorrecta:
            self.ids.error_label.text = "Error: Contraseña incorrecta"
        except LoginEspacioVacio:
            self.ids.error_label.text = "Error: Faltan campos obligatorios"