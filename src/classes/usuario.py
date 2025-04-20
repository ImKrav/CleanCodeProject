from src.classes.contacto import Contacto

class Usuario:
    """
    Representa un usuario de la aplicación.

    Atributos:
        id (int): Identificador único.
        nombre (str): Nombre de usuario.
        email (str): Correo electrónico.
        password (str): Contraseña.
        contactos (list[Contacto]): lista de contactos del usuario.
    """
    def __init__(self, id: int, nombre: str, email: str, password: str):
        """
        Inicializa un nuevo usuario a partir de un diccionario.

        Args:
            data (dict): {
                'id' (int): identificador único,
                'nombre' (str): nombre de usuario,
                'email' (str): correo electrónico,
                'password' (str): contraseña
            }
        """
        self.id = id
        self.nombre = nombre
        self.email = email
        self.password = password
        self.contactos : list[Contacto] = []

    def __repr__(self):
        """
        Devuelve una cadena representativa del usuario.

        Returns:
            str: formato "ID: {id} - Nombre: {nombre} - Email: {email}".
        """
        return f"ID: {self.id} - Nombre: {self.nombre} - Email: {self.email}"