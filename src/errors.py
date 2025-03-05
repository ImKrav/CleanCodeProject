class ErrorNombreVacio(Exception):
    def __init__(self, mensaje="El nombre no puede estar vacío"):
        self.mensaje = mensaje
        super().__init__(self.mensaje)

class ErrorTelefonoNoNumerico(Exception):
    def __init__(self, mensaje="El teléfono debe ser un valor numérico"):
        self.mensaje = mensaje
        super().__init__(self.mensaje)

class ErrorCorreoInvalido(Exception):
    def __init__(self, mensaje="El email no tiene un formato válido"):
        self.mensaje = mensaje
        super().__init__(self.mensaje)

class ErrorContrasenaVacia(Exception):
    def __init__(self, mensaje="La contraseña no puede estar vacía"):
        self.mensaje = mensaje
        super().__init__(self.mensaje)

class ContactoNoExistente(Exception):
    def __init__(self, mensaje="El contacto no existe"):
        self.mensaje = mensaje
        super().__init__(self.mensaje)

class CategoriaNoExistente(Exception):
    def __init__(self, mensaje="La categoría no existe"):
        self.mensaje = mensaje
        super().__init__(self.mensaje)

class ErrorCategoriaVacia(Exception):
    def __init__(self, mensaje="La categoría no puede estar vacía"):
        self.mensaje = mensaje
        super().__init__(self.mensaje)

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

class EmailYaExistente(Exception):
    def __init__(self, mensaje="El email ya está registrado"):
        self.mensaje = mensaje
        super().__init__(self.mensaje)

class IDYaExistente(Exception):
    def __init__(self, mensaje="El ID ya está registrado"):
        self.mensaje = mensaje
        super().__init__(self.mensaje)
