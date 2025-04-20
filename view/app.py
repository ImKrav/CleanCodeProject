from kivy.app import App
from kivy.lang import Builder
from view.screens.login import Login

class MainApp(App):  # Cambiado de App a MainApp
    def build(self):
        Builder.load_file("view/kv/login.kv")
        return Login()