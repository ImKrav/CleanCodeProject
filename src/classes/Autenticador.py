from src.classes.Usuario import Usuario

class Autenticador:
    def __init__(self):
        pass

    def registrar_usuario(self, nombre: str, email: str, password: str) -> Usuario:
        pass

    def iniciar_sesion(self, email: str, password: str) -> Usuario | None:
        pass