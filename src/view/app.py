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
    """
    Gestor de pantallas personalizado que almacena el usuario actual.

    Atributos:
        usuario_actual (Usuario | None): Referencia al usuario
            que ha iniciado sesión; inicialmente None.
    """
    def __init__(self, **kwargs):
        """
        Inicializa el CustomScreenManager.

        Llama al constructor de la superclase y establece
        `usuario_actual` en None.
        """
        super().__init__(**kwargs)
        self.usuario_actual : Usuario = None

class MainApp(App):
    """
    Clase principal de la aplicación Kivy.

    Construye el gestor de pantallas, carga el archivo KV y
    gestiona excepciones no capturadas.
    """
    def build(self):
        """
        Construye la interfaz de usuario de la aplicación.

        Carga el archivo KV principal y añade las pantallas:
        - FirstScreen
        - Login
        - Signup
        - MainScreen

        Retorna:
            CustomScreenManager: Instancia configurada con todas
            las pantallas de la aplicación.
        """
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