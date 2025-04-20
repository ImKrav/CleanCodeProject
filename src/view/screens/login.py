from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
from src.model.classes.autenticador import Autenticador
from src.model.errors import UsuarioNoExistente, ErrorContrasenaIncorrecta, LoginEspacioVacio

class Login(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.autenticador = Autenticador()

    def iniciar_sesion(self, email, password):
        try:
            if self.autenticador.iniciar_sesion(email, password):
                self.ids.error_label.text = "Inicio de sesión exitoso"
                self.ids.error_label.color = (0, 1, 0, 1)
                self.manager.current = "main"
        except UsuarioNoExistente:
            self.ids.error_label.text = "Error: El usuario no existe"
        except ErrorContrasenaIncorrecta:
            self.ids.error_label.text = "Error: Contraseña incorrecta"
        except LoginEspacioVacio:
            self.ids.error_label.text = "Error: Faltan campos obligatorios"