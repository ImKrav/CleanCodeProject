from src.model.classes.usuario import Usuario
from src.model.classes.contacto import Contacto
from src.model.errors import ErrorNombreVacio, ErrorTelefonoMuyLargo, ErrorTelefonoNoNumerico, ErrorCorreoInvalido, IDVacia, IDNoEncontrado, CategoriaNoExistente

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

    def agregar_contacto(self, contacto: Contacto) -> Contacto:
        """
        Valida y agrega un nuevo contacto.

        Args:
           contacto (Contacto): instancia a agregar.

        Raises:
            ErrorNombreVacio, ErrorTelefonoNoNumerico, ErrorTelefonoMuyLargo,
            ErrorCorreoInvalido, CategoriaNoExistente

        Returns:
            Contacto: instancia creada y anexada a usuario.contactos.
        """
        if not contacto.nombre:
            raise ErrorNombreVacio()
        if not str(contacto.telefono).isdigit():
            raise ErrorTelefonoNoNumerico()
        if len(contacto.telefono) > 15:
            raise ErrorTelefonoMuyLargo()
        if (contacto.email != '') and (contacto.email and "@" not in contacto.email):
            raise ErrorCorreoInvalido()
        if (contacto.categoria != '') and (contacto.categoria not in ['Personal', 'Trabajo', 'Sin asignar']):
            raise CategoriaNoExistente()

        if contacto.categoria == '':
            contacto.categoria = 'Sin asignar'

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

    def editar_contacto(self, contacto_editado: Contacto) -> Contacto:
        """
        Actualiza campos de un contacto existente.

        Args:
            contacto_editado (Contacto): instancia con los campos a modificar.

        Raises:
            IDVacia, ErrorNombreVacio, ErrorTelefonoNoNumerico,
            ErrorTelefonoMuyLargo, ErrorCorreoInvalido, CategoriaNoExistente,
            IDNoEncontrado

        Returns:
            Contacto: instancia editada.
        """
        if (contacto_editado.telefono != '') and (not contacto_editado.telefono.isdigit()):
            raise ErrorTelefonoNoNumerico()
        if (contacto_editado.id == None) or (contacto_editado.id == ''):
            raise IDVacia(f'El ID no puede estar vacío')
        if len(contacto_editado.telefono) > 15:
            raise ErrorTelefonoMuyLargo()
        if contacto_editado.email and "@" not in contacto_editado.email:
            raise ErrorCorreoInvalido()
        if (contacto_editado.categoria !='') and (contacto_editado.categoria not in ['Personal', 'Trabajo', 'Sin asignar']):
            raise CategoriaNoExistente()
        
        for contacto_buscado in self.usuario.contactos:
            if contacto_buscado.id == contacto_editado.id:
                contacto_buscado.nombre = contacto_editado.nombre if contacto_editado.nombre else contacto_buscado.nombre
                contacto_buscado.telefono = contacto_editado.telefono if contacto_editado.telefono else contacto_buscado.telefono
                contacto_buscado.email = contacto_editado.email if contacto_editado.email else contacto_buscado.email
                contacto_buscado.direccion = contacto_editado.direccion if contacto_editado.direccion else contacto_buscado.direccion
                contacto_buscado.categoria = contacto_editado.categoria if contacto_editado.categoria else contacto_buscado.categoria
                return contacto_buscado
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