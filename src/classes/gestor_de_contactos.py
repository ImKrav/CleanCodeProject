from src.classes.usuario import Usuario
from src.classes.contacto import Contacto
from src.errors import ErrorNombreVacio, ErrorTelefonoMuyLargo, ErrorTelefonoNoNumerico, ErrorCorreoInvalido, IDVacia, IDNoEncontrado, CategoriaNoExistente

class GestorDeContactos:
    """
    Gestiona la lista de contactos de un usuario.
    """

    def __init__(self, usuario: Usuario):
        """
        Args:
            usuario (Usuario): instancia de Usuario con atributo "contactos" (lista).
        """
        self.usuario = usuario

    def ver_contactos(self) -> list[Contacto]:
        """
        Devuelve la lista de contactos del usuario.

        Returns:
            list[Contacto]: lista de instancias Contacto.
        """
        return self.usuario.contactos

    def agregar_contacto(self, id: int, nombre: str, telefono: str, email: str = '', direccion: str = '', categoria: str = 'Sin asignar') -> Contacto:
        """
        Valida y agrega un nuevo contacto.

        Args:
            data (dict): {
                'nombre': str,
                'telefono': str,
                'email' (opcional): str,
                'direccion' (opcional): str,
                'categoria' (opcional): str
            }

        Raises:
            ErrorNombreVacio, ErrorTelefonoNoNumerico, ErrorTelefonoMuyLargo,
            ErrorCorreoInvalido, CategoriaNoExistente

        Returns:
            Contacto: instancia creada y anexada a usuario.contactos.
        """
        if not nombre:
            raise ErrorNombreVacio()
        if not telefono.isdigit():
            raise ErrorTelefonoNoNumerico()
        if len(telefono) > 15:
            raise ErrorTelefonoMuyLargo()
        if email and "@" not in email:
            raise ErrorCorreoInvalido()
        if categoria not in ['Personal', 'Trabajo', 'Sin asignar']:
            raise CategoriaNoExistente()

        contacto = Contacto(id, nombre, telefono, email, direccion, categoria)
        self.usuario.contactos.append(contacto)
        return contacto

    def eliminar_contacto(self, id: int) -> None:
        """
        Elimina un contacto por su ID.

        Args:
            id (int): identificador del contacto a eliminar.

        Raises:
            IDVacia, IDNoEncontrado
        """
        if id == None or id == '':
            raise IDVacia(f'El ID no puede estar vacío')

        for contacto in self.usuario.contactos:
            if contacto.id == id:
                self.usuario.contactos.remove(contacto)
            return None
        else:
            raise IDNoEncontrado(f"Contacto con ID {id} no encontrado.")

    def editar_contacto(self, id: int, nombre: str, telefono: str, email: str, direccion: str, categoria: str) -> None:
        """
        Actualiza campos de un contacto existente.

        Args:
            id (int): identificador del contacto.
            updates (dict): campos a modificar {
                'nombre' (opcional): str,
                'telefono' (opcional): str,
                'email' (opcional): str,
                'direccion' (opcional): str,
                'categoria' (opcional): str
            }

        Raises:
            IDVacia, ErrorNombreVacio, ErrorTelefonoNoNumerico,
            ErrorTelefonoMuyLargo, ErrorCorreoInvalido, CategoriaNoExistente,
            IDNoEncontrado

        Returns:
            Contacto: instancia modificada.
        """
        if id == None or id == '':
            raise IDVacia(f'El ID no puede estar vacío')
        if nombre == '' or not nombre:
            raise ErrorNombreVacio()
        if not telefono.isdigit():
            raise ErrorTelefonoNoNumerico()
        if len(telefono) > 15:
            raise ErrorTelefonoMuyLargo()
        if email and "@" not in email:
            raise ErrorCorreoInvalido()
        if categoria not in ['Personal', 'Trabajo', 'Sin asignar']:
            raise CategoriaNoExistente()
        
        for contacto in self.usuario.contactos:
            if contacto.id == id:
                contacto.nombre = nombre if nombre else contacto.nombre
                contacto.telefono = telefono if telefono else contacto.telefono
                contacto.email = email if email else contacto.email
                contacto.direccion = direccion if direccion else contacto.direccion
                contacto.categoria = categoria if categoria else contacto.categoria
                return None
        else:
            raise IDNoEncontrado(f"Contacto con ID {id} no encontrado.")

    def buscar_contacto(self, nombre: str) -> list[Contacto]:
        """
        Busca contactos cuyo nombre contenga la cadena dada.

        Args:
            nombre (str): texto a buscar en el nombre.

        Raises:
            ErrorNombreVacio

        Returns:
            list[Contacto]: lista de coincidencias.
        """
        if not nombre:
            raise ErrorNombreVacio()
        
        return [contacto for contacto in self.usuario.contactos if nombre.lower() in contacto.nombre.lower()]


    def filtrar_contacto(self, nombre: str = None, categoria: str = None) -> list[Contacto]:
        """
        Filtra contactos por nombre y/o categoría.

        Args:
            nombre (str, opcional): subcadena del nombre.
            categoria (str, opcional): categoría exacta.

        Raises:
            TypeError, ValueError, CategoriaNoExistente

        Returns:
            list[Contacto]: lista filtrada.
        """
        if nombre is not None and not isinstance(nombre, str):
            raise TypeError("El argumento 'nombre' debe ser una cadena de texto (str).")
        if categoria is not None and not isinstance(categoria, str):
            raise TypeError("El argumento 'categoria' debe ser una cadena de texto (str).")
        
        if not nombre and not categoria:
            raise ValueError("Debes proporcionar al menos un argumento: nombre o categoría.")
        
        if categoria and categoria not in ['Personal', 'Trabajo', 'Sin asignar']:
            raise CategoriaNoExistente()
        
        return [
            contacto for contacto in self.usuario.contactos
            if (not nombre or nombre.lower() in contacto.nombre.lower()) and
                (not categoria or contacto.categoria == categoria)
        ]