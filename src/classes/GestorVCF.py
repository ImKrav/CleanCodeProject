from src.classes.Contacto import Contacto
from src.classes.Usuario import Usuario
from src.errors import ErrorListaVaciaDeContactos, ErrorArchivoCorrupto, ErrorNoVCF, ErrorPermisosDeEscritura

class GestorVCF:
    def __init__(self, usuario: Usuario):
        self.usuario = usuario

    def exportar_contactos(self, contactos: list[Contacto], archivo: str) -> None:
        if not contactos:
            raise ErrorListaVaciaDeContactos("La lista de contactos está vacía.")
        if not archivo.endswith(".vcf"):
            raise ErrorNoVCF("El archivo debe tener la extensión .vcf.")

        try:
            with open(archivo, "w", encoding="utf-8") as file:
                for contacto in contactos:
                    file.write(self._formatear_contacto_vcf(contacto))
            print(f"Contactos exportados exitosamente a '{archivo}'.")
        except PermissionError:
            raise ErrorPermisosDeEscritura("No tienes permisos de escritura en el directorio de destino.")
        except Exception as e:
            raise Exception(f"Error inesperado al exportar contactos: {e}")

    def importar_contactos(self, archivo: str) -> list[Contacto]:
        if not archivo.endswith(".vcf"):
            raise ErrorNoVCF("El archivo debe tener la extensión .vcf.")

        contactos_importados = []
        try:
            with open(archivo, "r", encoding="utf-8") as file:
                contenido = file.read()
                contactos_raw = contenido.split("END:VCARD")
                for contacto_raw in contactos_raw:
                    if contacto_raw.strip():
                        contacto = self._parsear_contacto_vcf(contacto_raw + "END:VCARD")
                        contactos_importados.append(contacto)
            print(f"Contactos importados exitosamente desde '{archivo}'.")
            return contactos_importados
        except FileNotFoundError:
            raise ErrorArchivoCorrupto("El archivo no existe o está corrupto.")
        except Exception as e:
            raise Exception(f"Error inesperado al importar contactos: {e}")

    def _formatear_contacto_vcf(self, contacto: Contacto) -> str:
        """Convierte un contacto en formato VCF."""
        return (
            "BEGIN:VCARD\n"
            "VERSION:3.0\n"
            f"FN:{contacto.nombre}\n"
            f"TEL:{contacto.telefono}\n"
            f"EMAIL:{contacto.email}\n"
            f"ADR:{contacto.direccion}\n"
            f"CATEGORY:{contacto.categoria}\n"
            "END:VCARD\n"
        )

    def _parsear_contacto_vcf(self, vcf_data: str) -> Contacto:
        """Convierte un bloque VCF en un objeto Contacto."""
        lines = vcf_data.split("\n")
        nombre = telefono = email = direccion = categoria = ""
        for line in lines:
            if line.startswith("FN:"):
                nombre = line[3:].strip()
            elif line.startswith("TEL:"):
                telefono = line[4:].strip()
            elif line.startswith("EMAIL:"):
                email = line[6:].strip()
            elif line.startswith("ADR:"):
                direccion = line[4:].strip()
            elif line.startswith("CATEGORY:"):
                categoria = line[9:].strip()

        id_contacto = len(self.usuario.contactos) + 1
        return Contacto(id_contacto, nombre, telefono, email, direccion, categoria)