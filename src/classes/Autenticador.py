from src.classes.Usuario import Usuario
from src.errors import ErrorContrasenaMuyLarga, ErrorContrasenaVacia, ErrorContrasenaIncorrecta, ErrorCorreoInvalido, EmailYaExistente, UsuarioNoExistente, LoginEspacioVacio

class Autenticador:
    def __init__(self):
        self.usuarios = []

    def registrar_usuario(self, usuario : Usuario) -> Usuario:
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