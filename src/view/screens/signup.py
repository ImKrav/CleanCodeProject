from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
from src.model.classes.autenticador import Autenticador
from src.model.classes.usuario import Usuario

class Signup(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.autenticador = Autenticador()

    def registrarse(self, nombre, email, password):
        try:
            nuevo_id = len(self.autenticador.usuarios) + 1
            nuevo_usuario = Usuario(nuevo_id, nombre, email, password)
            
            self.autenticador.registrar_usuario(nuevo_usuario)
            
            self.ids.error_label.text = "Registro exitoso. Ahora puedes iniciar sesión."
            self.ids.error_label.color = (0, 1, 0, 1)
        except Exception as e:
            self.ids.error_label.text = f"Error al registrarse: {e}"
            self.ids.error_label.color = (1, 0, 0, 1)