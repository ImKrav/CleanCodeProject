from src.classes.Usuario import Usuario
from src.classes.Contacto import Contacto

class GestorDeContactos:
    def __init__(self, usuario: Usuario):
        self.usuario = usuario

    def agregar_contacto(self) -> None:
        pass

    def eliminar_contacto(self) -> None:
        pass

    def editar_contacto(self) -> None:
        pass

    def buscar_contacto(self) -> list[Contacto]:
        pass

    def filtrar_contacto(self) -> list[Contacto]:
        pass