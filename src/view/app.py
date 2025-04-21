import traceback
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager

from src.model.classes.usuario import Usuario
from src.view.screens.first_screen import FirstScreen
from src.view.screens.login import Login
from src.view.screens.signup import Signup
from src.view.screens.main_screen import MainScreen

class CustomScreenManager(ScreenManager):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.usuario_actual : Usuario = None

class MainApp(App):
    def build(self):
        Builder.load_file("src/view/kv/main.kv")

        sm = CustomScreenManager()
        sm.add_widget(FirstScreen(name="first"))
        sm.add_widget(Login(name="login"))
        sm.add_widget(Signup(name="signup"))
        sm.add_widget(MainScreen(name="main"))
        return sm

    def handle_exception(self, exc_type, exc_value, exc_traceback):
        """Manejador global de excepciones."""
        error_message = "".join(traceback.format_exception(exc_type, exc_value, exc_traceback))
        print(f"Error capturado:\n{error_message}")