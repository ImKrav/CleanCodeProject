from src.classes.Usuario import Usuario
from src.errors import ErrorContrasenaMuyLarga, ErrorContrasenaVacia, ErrorContrasenaIncorrecta, ErrorCorreoInvalido, EmailYaExistente

class Autenticador:
    def __init__(self):
        self.usuarios = [] 

    def registrar_usuario(self, usuario : Usuario):
        if usuario.password == '':
            raise ErrorContrasenaVacia(f'La contraseña no puede estar vacía')
        if len(usuario.password) > 15:
            raise ErrorContrasenaMuyLarga(f'La contraseña no puede tener más de 15 caracteres')
        if usuario.email in [u.email for u in self.usuarios]:
            raise EmailYaExistente(f'El email ya está registrado')
        if '@' not in usuario.email:
            raise ErrorCorreoInvalido(f'El email no tiene un formato válido')

        self.usuarios.append(usuario)

    def iniciar_sesion(self, email, password):
        for usuario in self.usuarios:
            if '@' not in email:
                raise ErrorCorreoInvalido(f'El email no tiene un formato válido')
            if usuario.password != password:
                raise ErrorContrasenaIncorrecta(f'La contraseña es incorrecta')
            
            if usuario.email == email and usuario.password == password:
                return True
        return False