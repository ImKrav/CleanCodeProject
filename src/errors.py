# Errores relacionados con el nombre
class ErrorNombreVacio(Exception):
    def __init__(self, mensaje="El nombre no puede estar vacío"):
        self.mensaje = mensaje
        super().__init__(self.mensaje)

# Errores relacionados con el teléfono
class ErrorTelefonoNoNumerico(Exception):
    def __init__(self, mensaje="El teléfono debe ser un valor numérico"):
        self.mensaje = mensaje
        super().__init__(self.mensaje)

class ErrorTelefonoMuyLargo(Exception):
    def __init__(self, mensaje="El número de teléfono es muy largo, debe tener como máximo 15 dígitos"):
        self.mensaje = mensaje
        super().__init__(self.mensaje)

# Errores relacionados con la contraseña
class ErrorContrasenaMuyLarga(Exception):
    def __init__(self, mensaje="La contraseña es muy larga, debe tener como máximo 15 caracteres"):
        self.mensaje = mensaje
        super().__init__(self.mensaje)

class ErrorContrasenaVacia(Exception):
    def __init__(self, mensaje="La contraseña no puede estar vacía"):
        self.mensaje = mensaje
        super().__init__(self.mensaje)

class ErrorContrasenaIncorrecta(Exception):
    def __init__(self, mensaje="La contraseña es incorrecta"):
        self.mensaje = mensaje
        super().__init__(self.mensaje)

# Errores relacionados con el correo electrónico
class ErrorCorreoInvalido(Exception):
    def __init__(self, mensaje="El email no tiene un formato válido"):
        self.mensaje = mensaje
        super().__init__(self.mensaje)

class EmailYaExistente(Exception):
    def __init__(self, mensaje="El email ya está registrado"):
        self.mensaje = mensaje
        super().__init__(self.mensaje)

# Errores relacionados con contactos
class ContactoNoExistente(Exception):
    def __init__(self, mensaje="El contacto no existe"):
        self.mensaje = mensaje
        super().__init__(self.mensaje)

class ErrorListaVaciaDeContactos(Exception):
    def __init__(self, mensaje="La lista de contactos está vacía"):
        self.mensaje = mensaje
        super().__init__(self.mensaje)

# Errores relacionados con la categoría
class CategoriaNoExistente(Exception):
    def __init__(self, mensaje="La categoría no existe"):
        self.mensaje = mensaje
        super().__init__(self.mensaje)

# Errores relacionados archivos
class ErrorPermisosDeEscritura(Exception):
    def __init__(self, mensaje="No tienes permisos de escritura en el directorio"):
        self.mensaje = mensaje
        super().__init__(self.mensaje)

class ErrorNoVCF(Exception):
    def __init__(self, mensaje="El archivo no es un archivo de extensión .vcf"):
        self.mensaje = mensaje
        super().__init__(self.mensaje)

class ErrorArchivoCorrupto(Exception):
    def __init__(self, mensaje="El archivo está corrupto o no se puede cargar"):
        self.mensaje = mensaje
        super().__init__(self.mensaje)

# Errores relacionados con el usuario
class UsuarioNoExistente(Exception):
    def __init__(self, mensaje="El usuario no existe"):
        self.mensaje = mensaje
        super().__init__(self.mensaje)

class LoginEspacioVacio(Exception):
    def __init__(self, mensaje="Faltan campos obligatorios por llenar"):
        self.mensaje = mensaje
        super().__init__(self.mensaje)

class IDYaExistente(Exception):
    def __init__(self, mensaje="El ID ya está registrado"):
        self.mensaje = mensaje
        super().__init__(self.mensaje)

class IDVacia(Exception):
    def __init__(self, mensaje="El ID no puede estar vacío"):
        self.mensaje = mensaje
        super().__init__(self.mensaje)

class IDNoEncontrado(Exception):
    def __init__(self, mensaje="ID no encontrado"):
        self.mensaje = mensaje
        super().__init__(self.mensaje)