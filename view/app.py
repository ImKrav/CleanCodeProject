from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager
from view.screens.first_screen import FirstScreen
from view.screens.login import Login
from view.screens.signup import Signup
from view.screens.main_screen import MainScreen

class MainApp(App):
    def build(self):
        Builder.load_file("view/kv/ScreenManager.kv")  # Asegúrate de que el archivo .kv esté correctamente cargado
        sm = ScreenManager()
        sm.add_widget(FirstScreen(name="first"))
        sm.add_widget(Login(name="login"))
        sm.add_widget(Signup(name="signup"))
        sm.add_widget(MainScreen(name="main"))
        return sm