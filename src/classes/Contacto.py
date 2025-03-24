class Contacto:
    def __init__(self, id: int, nombre: str, telefono: str, email: str, direccion: str, categoria: str):
        self.id = id
        self.nombre = nombre
        self.telefono = telefono
        self.email = email
        self.direccion = direccion
        self.categoria = categoria

    def __repr__(self):
        return f"ID: {self.id} - Nombre: {self.nombre} - Teléfono: {self.telefono} - Email: {self.email} - Dirección: {self.direccion} - Categoría: {self.categoria}"