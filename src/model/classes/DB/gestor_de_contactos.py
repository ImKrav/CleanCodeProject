from src.model.classes.DB.usuario import Usuario
from src.model.classes.DB.contacto import Contacto
from src.model.classes.DB.database import SessionLocal
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
        with SessionLocal() as db:
            return db.query(Contacto).filter(Contacto.usuario_id == self.usuario.id).all()

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

        contacto.usuario_id = self.usuario.id

        with SessionLocal() as db:
            db.add(contacto)
            db.commit()
            db.refresh(contacto)
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

        with SessionLocal() as db:
            contacto = db.query(Contacto).filter(
                Contacto.id == id,
                Contacto.usuario_id == self.usuario.id
            ).first()
            if not contacto:
                raise IDNoEncontrado(f"Contacto con ID {id} no encontrado.")
            db.delete(contacto)
            db.commit()

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
        
        with SessionLocal() as db:
            contacto = db.query(Contacto).filter(
                Contacto.id == contacto_editado.id,
                Contacto.usuario_id == self.usuario.id
            ).first()
            if not contacto:
                raise IDNoEncontrado(f"Contacto con ID {contacto_editado.id} no encontrado.")

            contacto.nombre = contacto_editado.nombre or contacto.nombre
            contacto.telefono = contacto_editado.telefono or contacto.telefono
            contacto.email = contacto_editado.email or contacto.email
            contacto.direccion = contacto_editado.direccion or contacto.direccion
            contacto.categoria = contacto_editado.categoria or contacto.categoria

            db.commit()
            db.refresh(contacto)
            return contacto

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
        
        with SessionLocal() as db:
            return db.query(Contacto).filter(
                Contacto.usuario_id == self.usuario.id,
                Contacto.nombre.ilike(f"%{nombre}%")
            ).all()


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
        
        with SessionLocal() as db:
            query = db.query(Contacto).filter(Contacto.usuario_id == self.usuario.id)
            if nombre:
                query = query.filter(Contacto.nombre.ilike(f"%{nombre}%"))
            if categoria:
                query = query.filter(Contacto.categoria == categoria)
            return query.all()