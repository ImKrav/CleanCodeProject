from src.model.classes.DB.usuario import Usuario
from src.model.classes.DB.database import SessionLocal
from src.model.errors import ErrorContrasenaMuyLarga, ErrorContrasenaVacia, ErrorContrasenaIncorrecta, ErrorCorreoInvalido, EmailYaExistente, UsuarioNoExistente, LoginEspacioVacio

class Autenticador:
    """
    Gestiona el registro e inicio de sesión de usuarios. Variable global de usuarios.
    """

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
            raise ErrorContrasenaVacia('La contraseña no puede estar vacía')
        if len(usuario.password) > 15:
            raise ErrorContrasenaMuyLarga('La contraseña no puede tener más de 15 caracteres')
        if '@' not in usuario.email:
            raise ErrorCorreoInvalido('El email no tiene un formato válido')

        with SessionLocal() as db:
            existe = db.query(Usuario).filter(Usuario.email == usuario.email).first()
            if existe:
                raise EmailYaExistente('El email ya está registrado')
            db.add(usuario)
            db.commit()
            db.refresh(usuario)
            return usuario

    def iniciar_sesion(self, email, password) -> Usuario:
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
            Usuario: Usuario si la autenticación es exitosa, None si no es exitosa.
        """
        email = email.lower()
        if len(password) > 15:
            raise ErrorContrasenaMuyLarga('La contraseña no puede tener más de 15 caracteres')
        if password == '':
            raise ErrorContrasenaVacia('La contraseña no puede estar vacía')
        if email == '':
            raise LoginEspacioVacio('El email no puede estar vacío')

        with SessionLocal() as db:
            usuario = db.query(Usuario).filter(Usuario.email == email).first()
            if not usuario:
                raise UsuarioNoExistente('El usuario no existe')
            if usuario.password != password:
                raise ErrorContrasenaIncorrecta('La contraseña es incorrecta')
            return usuario