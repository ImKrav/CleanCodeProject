# Errores relacionados con el nombre
class ErrorNombreVacio(Exception):
    """Se lanza cuando el nombre proporcionado está vacío."""
    def __init__(self, mensaje="El nombre no puede estar vacío"):
        super().__init__(mensaje)

# Errores relacionados con el teléfono
class ErrorTelefonoNoNumerico(Exception):
    """Se lanza cuando el teléfono contiene caracteres no numéricos."""
    def __init__(self, mensaje="El teléfono debe ser un valor numérico"):
        super().__init__(mensaje)

class ErrorTelefonoMuyLargo(Exception):
    """Se lanza cuando el teléfono excede 15 dígitos."""
    def __init__(self, mensaje="El número de teléfono es muy largo, debe tener como máximo 15 dígitos"):
        super().__init__(mensaje)

# Errores relacionados con la contraseña
class ErrorContrasenaMuyLarga(Exception):
    """Se lanza cuando la contraseña excede 15 caracteres."""
    def __init__(self, mensaje="La contraseña es muy larga, debe tener como máximo 15 caracteres"):
        super().__init__(mensaje)

class ErrorContrasenaVacia(Exception):
    """Se lanza cuando la contraseña está vacía."""
    def __init__(self, mensaje="La contraseña no puede estar vacía"):
        super().__init__(mensaje)

class ErrorContrasenaIncorrecta(Exception):
    """Se lanza cuando la contraseña no coincide con la registrada."""
    def __init__(self, mensaje="La contraseña es incorrecta"):
        super().__init__(mensaje)

# Errores relacionados con el correo electrónico
class ErrorCorreoInvalido(Exception):
    """Se lanza cuando el formato del correo no es válido."""
    def __init__(self, mensaje="El email no tiene un formato válido"):
        super().__init__(mensaje)

class EmailYaExistente(Exception):
    """Se lanza cuando el email ya está registrado."""
    def __init__(self, mensaje="El email ya está registrado"):
        super().__init__(mensaje)

# Errores relacionados con contactos
class ContactoNoExistente(Exception):
    """Se lanza cuando se intenta operar sobre un contacto inexistente."""
    def __init__(self, mensaje="El contacto no existe"):
        super().__init__(mensaje)

class ErrorListaVaciaDeContactos(Exception):
    """Se lanza cuando la lista de contactos está vacía."""
    def __init__(self, mensaje="La lista de contactos está vacía"):
        super().__init__(mensaje)

# Errores relacionados con la categoría
class CategoriaNoExistente(Exception):
    """Se lanza cuando la categoría no está entre las permitidas."""
    def __init__(self, mensaje="La categoría no existe"):
        super().__init__(mensaje)

# Errores relacionados con archivos
class ErrorPermisosDeEscritura(Exception):
    """Se lanza cuando no hay permisos de escritura en el destino."""
    def __init__(self, mensaje="No tienes permisos de escritura en el directorio"):
        super().__init__(mensaje)

class ErrorNoVCF(Exception):
    """Se lanza cuando el archivo no tiene extensión .vcf."""
    def __init__(self, mensaje="El archivo no es un archivo de extensión .vcf"):
        super().__init__(mensaje)

class ErrorArchivoCorrupto(Exception):
    """Se lanza cuando el archivo está corrupto o no se puede cargar."""
    def __init__(self, mensaje="El archivo está corrupto o no se puede cargar"):
        super().__init__(mensaje)

# Errores relacionados con el usuario
class UsuarioNoExistente(Exception):
    """Se lanza cuando el usuario no está registrado."""
    def __init__(self, mensaje="El usuario no existe"):
        super().__init__(mensaje)

class LoginEspacioVacio(Exception):
    """Se lanza cuando faltan campos obligatorios en login."""
    def __init__(self, mensaje="Faltan campos obligatorios por llenar"):
        super().__init__(mensaje)

# Errores relacionados con el ID
class IDYaExistente(Exception):
    """Se lanza cuando el ID ya está registrado."""
    def __init__(self, mensaje="El ID ya está registrado"):
        super().__init__(mensaje)

class IDVacia(Exception):
    """Se lanza cuando el ID proporcionado está vacío."""
    def __init__(self, mensaje="El ID no puede estar vacío"):
        super().__init__(mensaje)

class IDNoEncontrado(Exception):
    """Se lanza cuando no se encuentra un objeto con el ID dado."""
    def __init__(self, mensaje="ID no encontrado"):
        super().__init__(mensaje)