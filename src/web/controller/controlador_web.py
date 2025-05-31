from fastapi import APIRouter, HTTPException, UploadFile, File, Form
from fastapi.responses import Response
from pydantic import BaseModel
from typing import List, Optional

from src.model.classes.DB.usuario import Usuario
from src.model.classes.DB.contacto import Contacto
from src.model.classes.DB.gestor_de_contactos import GestorDeContactos
from src.model.classes.DB.gestor_vcf import GestorVCF
from src.model.classes.DB.database import SessionLocal

class ContactoSchema(BaseModel):
    id: int
    nombre: str
    telefono: str
    email: Optional[str] = None
    direccion: Optional[str] = None
    categoria: Optional[str] = "Sin asignar"

class ContactoCrearSchema(BaseModel):
    nombre: str
    telefono: str
    email: Optional[str] = None
    direccion: Optional[str] = None
    categoria: Optional[str] = "Sin asignar"

class UsuarioSchema(BaseModel):
    id: int
    nombre: str
    email: str

class UsuarioRegistroSchema(BaseModel):
    nombre: str
    email: str
    password: str

class UsuarioLoginSchema(BaseModel):
    email: str
    password: str

class EditarContactoSchema(BaseModel):
    id: int
    nombre: Optional[str] = None
    telefono: Optional[str] = None
    email: Optional[str] = None
    direccion: Optional[str] = None
    categoria: Optional[str] = None

class FiltrarContactoSchema(BaseModel):
    nombre: Optional[str] = None
    categoria: Optional[str] = None

class ControladorWeb:
    def __init__(self):
        self.router = APIRouter(prefix="/api/v1")
        self.usuarios = []
        self.sesiones = {}

        @self.router.post("/signup", response_model=UsuarioSchema)
        def signup(usuario: UsuarioRegistroSchema):
            with SessionLocal() as db:
                existe = db.query(Usuario).filter(Usuario.email == usuario.email).first()
                if existe:
                    raise HTTPException(status_code=400, detail="El email ya está registrado")
                nuevo = Usuario(nombre=usuario.nombre, email=usuario.email, password=usuario.password)
                db.add(nuevo)
                db.commit()
                db.refresh(nuevo)
                return UsuarioSchema(id=nuevo.id, nombre=nuevo.nombre, email=nuevo.email)

        @self.router.post("/login", response_model=UsuarioSchema)
        def login(datos: UsuarioLoginSchema):
            with SessionLocal() as db:
                user = db.query(Usuario).filter(Usuario.email == datos.email).first()
                if not user or user.password != datos.password:
                    raise HTTPException(status_code=401, detail="Credenciales incorrectas")
                return UsuarioSchema(id=user.id, nombre=user.nombre, email=user.email)

        @self.router.get("/contactos", response_model=List[ContactoSchema])
        def listar_contactos(usuario_id: int = 1):
            usuario = self._get_usuario_db(usuario_id)
            gestor = GestorDeContactos(usuario)
            contactos = gestor.ver_contactos()
            return [ContactoSchema(
                id=c.id,
                nombre=c.nombre,
                telefono=c.telefono,
                email=c.email,
                direccion=c.direccion,
                categoria=c.categoria
            ) for c in contactos]

        @self.router.post("/contactos", response_model=ContactoSchema)
        def crear_contacto(contacto: ContactoCrearSchema, usuario_id: int = 1):
            usuario = self._get_usuario_db(usuario_id)
            gestor = GestorDeContactos(usuario)
            nuevo = Contacto(
                nombre=contacto.nombre,
                telefono=contacto.telefono,
                email=contacto.email,
                direccion=contacto.direccion,
                categoria=contacto.categoria,
                usuario_id=usuario_id
            )
            gestor.agregar_contacto(nuevo)
            return ContactoSchema(
                id=nuevo.id,
                nombre=nuevo.nombre,
                telefono=nuevo.telefono,
                email=nuevo.email,
                direccion=nuevo.direccion,
                categoria=nuevo.categoria
            )

        @self.router.put("/contactos/{contacto_id}", response_model=ContactoSchema)
        def editar_contacto(contacto_id: int, datos: EditarContactoSchema, usuario_id: int = 1):
            usuario = self._get_usuario_db(usuario_id)
            gestor = GestorDeContactos(usuario)
            contacto_editado = Contacto(
                id=contacto_id,
                nombre=datos.nombre,
                telefono=datos.telefono,
                email=datos.email,
                direccion=datos.direccion,
                categoria=datos.categoria,
                usuario_id=usuario_id
            )
            actualizado = gestor.editar_contacto(contacto_editado)
            return ContactoSchema(
                id=actualizado.id,
                nombre=actualizado.nombre,
                telefono=actualizado.telefono,
                email=actualizado.email,
                direccion=actualizado.direccion,
                categoria=actualizado.categoria
            )

        @self.router.delete("/contactos/{contacto_id}")
        def eliminar_contacto(contacto_id: int, usuario_id: int = 1):
            usuario = self._get_usuario_db(usuario_id)
            gestor = GestorDeContactos(usuario)
            gestor.eliminar_contacto(contacto_id)
            return {"ok": True}

        @self.router.get("/buscar_contacto", response_model=List[ContactoSchema])
        def buscar_contacto(nombre: str, usuario_id: int = 1):
            usuario = self._get_usuario_db(usuario_id)
            gestor = GestorDeContactos(usuario)
            resultados = gestor.buscar_contacto(nombre)
            return [ContactoSchema(
                id=c.id,
                nombre=c.nombre,
                telefono=c.telefono,
                email=c.email,
                direccion=c.direccion,
                categoria=c.categoria
            ) for c in resultados]

        @self.router.post("/filtrar_contacto", response_model=List[ContactoSchema])
        def filtrar_contacto(filtro: FiltrarContactoSchema, usuario_id: int = 1):
            usuario = self._get_usuario_db(usuario_id)
            gestor = GestorDeContactos(usuario)
            resultados = gestor.filtrar_contacto(nombre=filtro.nombre, categoria=filtro.categoria)
            return [ContactoSchema(
                id=c.id,
                nombre=c.nombre,
                telefono=c.telefono,
                email=c.email,
                direccion=c.direccion,
                categoria=c.categoria
            ) for c in resultados]

        @self.router.post("/importar_contactos")
        def importar_contactos(usuario_id: int = 1, archivo: UploadFile = File(...)):
            usuario = self._get_usuario_db(usuario_id)
            gestor_vcf = GestorVCF(usuario)
            ruta = f"temp_{usuario_id}.vcf"
            with open(ruta, "wb") as f:
                contenido = archivo.file.read()
                if not contenido:
                    raise HTTPException(status_code=400, detail="El archivo está vacío o no se pudo leer.")
                f.write(contenido)
            try:
                contactos_importados = gestor_vcf.importar_contactos(ruta)
                if not contactos_importados:
                    raise HTTPException(status_code=400, detail="No se importó ningún contacto. Verifica el archivo o que no haya duplicados.")
                return {"importados": len(contactos_importados)}
            except Exception as e:
                raise HTTPException(status_code=400, detail=f"Error al importar contactos: {str(e)}")

        @self.router.get("/exportar_contactos")
        def exportar_contactos(usuario_id: int = 1):
            usuario = self._get_usuario_db(usuario_id)
            gestor_vcf = GestorVCF(usuario)
            ruta = f"export_{usuario_id}.vcf"
            gestor_vcf.exportar_contactos(ruta)
            with open(ruta, "rb") as f:
                contenido = f.read()
            return Response(content=contenido, media_type="text/vcard", headers={"Content-Disposition": f"attachment; filename=contactos_{usuario_id}.vcf"})

    def _get_usuario_db(self, usuario_id: int) -> Usuario:
        with SessionLocal() as db:
            user = db.query(Usuario).filter(Usuario.id == usuario_id).first()
            if not user:
                raise HTTPException(status_code=404, detail="Usuario no encontrado")
            return user