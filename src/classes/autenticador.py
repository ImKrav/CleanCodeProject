from src.classes.usuario import Usuario
from src.errors import ErrorContrasenaMuyLarga, ErrorContrasenaVacia, ErrorContrasenaIncorrecta, ErrorCorreoInvalido, EmailYaExistente, UsuarioNoExistente, LoginEspacioVacio

class Autenticador:
    """
    Gestiona el registro e inicio de sesión de usuarios.
    """
    def __init__(self):
        """
        Inicializa la lista interna de usuarios registrados.
        """
        self.usuarios = []

    def registrar_usuario(self, usuario: Usuario) -> Usuario:
        """
        Valida y registra un nuevo usuario.

        Args:
            usuario (Usuario): instancia de Usuario a registrar.

        Raises:
            ErrorContrasenaVacia: si la contraseña está vacía.
            ErrorContrasenaMuyLarga: si la contraseña excede 15 caracteres.
            EmailYaExistente: si el email ya está registrado.
            ErrorCorreoInvalido: si el email no contiene '@'.

        Return:
            Usuario: el usuario registrado.
        """

        usuario.email = usuario.email.lower() 
        if usuario.password == '':
            raise ErrorContrasenaVacia(f'La contraseña no puede estar vacía')
        if len(usuario.password) > 15:
            raise ErrorContrasenaMuyLarga(f'La contraseña no puede tener más de 15 caracteres')
        if usuario.email in [u.email for u in self.usuarios]:
            raise EmailYaExistente(f'El email ya está registrado')
        if '@' not in usuario.email:
            raise ErrorCorreoInvalido(f'El email no tiene un formato válido')

        self.usuarios.append(usuario)
        return usuario

    def iniciar_sesion(self, email, password) -> bool:
        """
        Autentica un usuario existente.

        Args:
            email (str): correo electrónico del usuario.
            password (str): contraseña proporcionada.

        Raises:
            ErrorContrasenaMuyLarga: si la contraseña excede 15 caracteres.
            ErrorContrasenaVacia: si la contraseña está vacía.
            LoginEspacioVacio: si el email está vacío.
            ErrorContrasenaIncorrecta: si la contraseña no coincide.
            UsuarioNoExistente: si no se encuentra el email.

        Return:
            bool: True si la autenticación es exitosa, false si no es exitoda.
        """
        email = email.lower()

        if len(password) > 15:
            raise ErrorContrasenaMuyLarga(f'La contraseña no puede tener más de 15 caracteres')
        if password == '':
            raise ErrorContrasenaVacia(f'La contraseña no puede estar vacía')
        if email == '':
            raise LoginEspacioVacio(f'El email no puede estar vacío')

        for usuario in self.usuarios:
            if usuario.email == email:
                if usuario.password != password:
                    raise ErrorContrasenaIncorrecta(f'La contraseña es incorrecta')
                if usuario.password == password:
                    return True
        raise UsuarioNoExistente(f'El usuario no existe')