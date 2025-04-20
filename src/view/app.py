from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager
from src.view.screens.first_screen import FirstScreen
from src.view.screens.login import Login
from src.view.screens.signup import Signup
from src.view.screens.main_screen import MainScreen

from src.model.classes.autenticador import Autenticador

class MainApp(App):
    def build(self):
        # Carga el archivo .kv pero no crea automáticamente las pantallas
        Builder.load_file("src/view/kv/main.kv")

        # Crea el ScreenManager y añade las pantallas manualmente
        sm = ScreenManager()
        sm.add_widget(FirstScreen(name="first"))
        sm.add_widget(Login(name="login"))  # Pasa el autenticador
        sm.add_widget(Signup(name="signup"))  # Pasa el autenticador
        sm.add_widget(MainScreen(name="main"))
        return sm