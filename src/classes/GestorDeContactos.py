from src.classes.Usuario import Usuario
from src.classes.Contacto import Contacto

class GestorDeContactos:
    def __init__(self, usuario: Usuario):
        self.usuario = usuario

    def agregar_contacto(self, id: int, nombre: str, telefono: str, email: str = '', direccion: str = '', categoria: str = 'Sin asignar') -> None:
        pass

    def eliminar_contacto(self, id: int) -> None:
        pass

    def editar_contacto(self, id: int, nombre: str, telefono: str, email: str, direccion: str, categoria: str) -> None:
        pass

    def buscar_contacto(self) -> list[Contacto]:
        pass

    def filtrar_contacto(self) -> list[Contacto]:
        pass