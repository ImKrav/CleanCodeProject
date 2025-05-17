from kivy.uix.screenmanager import Screen
from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

from src.model.classes.DB.contacto import Contacto
from src.model.classes.DB.gestor_de_contactos import GestorDeContactos
from src.model.classes.DB.gestor_vcf import GestorVCF
from src.model.errors import CategoriaNoExistente, ErrorListaVaciaDeContactos, ErrorArchivoCorrupto

class MainScreen(Screen):
    """
    Pantalla principal de la aplicación.

    Permite gestionar contactos (crear, editar, ver, buscar,
    filtrar) y realizar importación/exportación de VCF,
    registrando todas las acciones en una bitácora.
    """

    def on_enter(self):
        """
        Inicializa los gestores de contactos y VCF al entrar en pantalla.

        Comportamiento:
            - Crea instancias de GestorDeContactos y GestorVCF
              asociadas al usuario actual.
            - En caso de error, registra el mensaje de excepción.
        """
        try:
            self.gestor_contactos = GestorDeContactos(self.manager.usuario_actual)
            self.gestor_vcf = GestorVCF(self.manager.usuario_actual)
        except Exception as e:
            print(f"Error al inicializar gestores: {e}")

    def crear_contacto(self):
        """
        Abre un cuadro de diálogo para crear un nuevo contacto.

        Comportamiento:
            - Muestra campos: nombre, teléfono, email, dirección, categoría.
            - Al presionar 'Guardar', crea un nuevo Contacto y lo añade
              mediante GestorDeContactos.
            - Registra la acción o cualquier error en el log.
        """
        layout = BoxLayout(orientation="vertical", spacing=10, padding=10)
        nombre_input = TextInput(hint_text="Nombre")
        telefono_input = TextInput(hint_text="Teléfono")
        email_input = TextInput(hint_text="Email")
        direccion_input = TextInput(hint_text="Dirección")
        categoria_input = TextInput(hint_text="Categoría")

        layout.add_widget(nombre_input)
        layout.add_widget(telefono_input)
        layout.add_widget(email_input)
        layout.add_widget(direccion_input)
        layout.add_widget(categoria_input)

        guardar_btn = Button(text="Guardar", size_hint_y=None, height=40)
        cerrar_btn = Button(text="Cerrar", size_hint_y=None, height=40)

        layout.add_widget(guardar_btn)
        layout.add_widget(cerrar_btn)

        popup = Popup(title="Crear Contacto", content=layout, size_hint=(0.8, 0.8))

        def guardar_callback(instance):
            try:
                datos = {
                    "nombre": nombre_input.text,
                    "telefono": telefono_input.text,
                    "email": email_input.text,
                    "direccion": direccion_input.text,
                    "categoria": categoria_input.text,
                }
                contacto = Contacto(
                    nombre=datos["nombre"],
                    telefono=datos["telefono"],
                    email=datos["email"],
                    direccion=datos["direccion"],
                    categoria=datos["categoria"],
                    usuario_id=self.manager.usuario_actual.id
                )
                self.gestor_contactos.agregar_contacto(contacto)
                print(f"Contacto '{contacto.nombre}' creado exitosamente.")
                popup.dismiss()
            except Exception as e:
                print(f"Error al crear contacto: {e}")

        guardar_btn.bind(on_press=guardar_callback)
        cerrar_btn.bind(on_press=popup.dismiss)
        popup.open()

    def editar_contacto(self):
        """
        Abre un cuadro de diálogo para editar un contacto existente.

        Comportamiento:
            - Solicita el ID del contacto y los nuevos datos.
            - Al guardar, actualiza el contacto mediante GestorDeContactos.
            - Registra la acción o cualquier error en el log.
        """
        layout = BoxLayout(orientation="vertical", spacing=10, padding=10)
        id_input = TextInput(hint_text="ID del contacto a editar")
        nombre_input = TextInput(hint_text="Nuevo Nombre")
        telefono_input = TextInput(hint_text="Nuevo Teléfono")
        email_input = TextInput(hint_text="Nuevo Email")
        direccion_input = TextInput(hint_text="Nueva Dirección")
        categoria_input = TextInput(hint_text="Nueva Categoría")

        layout.add_widget(id_input)
        layout.add_widget(nombre_input)
        layout.add_widget(telefono_input)
        layout.add_widget(email_input)
        layout.add_widget(direccion_input)
        layout.add_widget(categoria_input)

        guardar_btn = Button(text="Guardar", size_hint_y=None, height=40)
        cerrar_btn = Button(text="Cerrar", size_hint_y=None, height=40)

        layout.add_widget(guardar_btn)
        layout.add_widget(cerrar_btn)

        popup = Popup(title="Editar Contacto", content=layout, size_hint=(0.8, 0.8))

        def guardar_callback(instance):
            try:
                id_contacto = int(id_input.text)
                datos = {
                    "id": id_contacto,
                    "nombre": nombre_input.text,
                    "telefono": telefono_input.text,
                    "email": email_input.text,
                    "direccion": direccion_input.text,
                    "categoria": categoria_input.text,
                }
                contacto_editado = Contacto(
                    id=datos["id"],
                    nombre=datos["nombre"],
                    telefono=datos["telefono"],
                    email=datos["email"],
                    direccion=datos["direccion"],
                    categoria=datos["categoria"],
                    usuario_id=self.manager.usuario_actual.id
                )
                self.gestor_contactos.editar_contacto(contacto_editado)
                print(f"Contacto con ID {id_contacto} actualizado exitosamente.")
                popup.dismiss()
            except ValueError:
                print("Error: El ID debe ser un número entero.")
            except Exception as e:
                print(f"Error al editar contacto: {e}")

        guardar_btn.bind(on_press=guardar_callback)
        cerrar_btn.bind(on_press=popup.dismiss)
        popup.open()

    def buscar_contacto(self):
        """
        Abre un cuadro de diálogo para buscar contactos por nombre.

        Comportamiento:
            - Solicita el nombre a buscar.
            - Registra en el log los resultados encontrados o un mensaje
              si no hay coincidencias.
        """
        layout = BoxLayout(orientation="vertical", spacing=10, padding=10)
        nombre_input = TextInput(hint_text="Nombre del contacto a buscar")
        layout.add_widget(nombre_input)

        buscar_btn = Button(text="Buscar", size_hint_y=None, height=40)
        cerrar_btn = Button(text="Cerrar", size_hint_y=None, height=40)
        layout.add_widget(buscar_btn)
        layout.add_widget(cerrar_btn)

        popup = Popup(title="Buscar Contacto", content=layout, size_hint=(0.8, 0.4))

        def buscar_callback(instance):
            try:
                nombre = nombre_input.text
                resultados = self.gestor_contactos.buscar_contacto(nombre)
                if resultados:
                    print(f"Resultados para '{nombre}':")
                    for contacto in resultados:
                        print(f"{contacto.id} | {contacto.nombre} | {contacto.telefono} | {contacto.email} | {contacto.direccion} | {contacto.categoria}")
                else:
                    print(f"No se encontraron contactos con el nombre '{nombre}'.")
            except Exception as e:
                print(f"Error al buscar contacto: {e}")
            finally:
                popup.dismiss()

        buscar_btn.bind(on_press=buscar_callback)
        cerrar_btn.bind(on_press=popup.dismiss)
        popup.open()

    def filtrar_contacto(self):
        """
        Abre un cuadro de diálogo para filtrar contactos por categoría.

        Comportamiento:
            - Solicita la categoría a filtrar.
            - Registra en el log los contactos encontrados o un mensaje
              si no existe la categoría o no hay resultados.
        Excepciones:
            CategoriaNoExistente: Si la categoría no existe.
        """
        layout = BoxLayout(orientation="vertical", spacing=10, padding=10)
        categoria_input = TextInput(hint_text="Categoría para filtrar")
        layout.add_widget(categoria_input)

        filtrar_btn = Button(text="Filtrar", size_hint_y=None, height=40)
        cerrar_btn = Button(text="Cerrar", size_hint_y=None, height=40)
        layout.add_widget(filtrar_btn)
        layout.add_widget(cerrar_btn)

        popup = Popup(title="Filtrar Contactos", content=layout, size_hint=(0.8, 0.4))

        def filtrar_callback(instance):
            try:
                categoria = categoria_input.text.strip()
                if not categoria:
                    raise ValueError("La categoría no puede estar vacía.")
                resultados = self.gestor_contactos.filtrar_contacto(categoria=categoria)
                if resultados:
                    print(f"Contactos en la categoría '{categoria}':")
                    for contacto in resultados:
                        print(f"{contacto.id} | {contacto.nombre} | {contacto.telefono} | {contacto.email} | {contacto.direccion}")
                else:
                    print(f"No se encontraron contactos en la categoría '{categoria}'.")
            except CategoriaNoExistente:
                print("Error: La categoría especificada no existe.")
            except Exception as e:
                print(f"Error al filtrar contactos: {e}")
            finally:
                popup.dismiss()

        filtrar_btn.bind(on_press=filtrar_callback)
        cerrar_btn.bind(on_press=popup.dismiss)
        popup.open()

    def exportar_contactos(self):
        """
        Exporta los contactos del usuario actual a un archivo VCF.

        Comportamiento:
            - Llama a GestorVCF.exportar_contactos con la lista de contactos.
            - Registra éxito o error en el log.
        Excepciones:
            ErrorListaVaciaDeContactos: Si no hay contactos para exportar.
        """
        try:
            self.gestor_vcf.exportar_contactos("contactos.vcf")
            print("Contactos exportados exitosamente a 'contactos.vcf'.")
        except ErrorListaVaciaDeContactos:
            print("Error: La lista de contactos está vacía.")
        except Exception as e:
            print(f"Error al exportar contactos: {e}")

    def importar_contactos(self):
        """
        Abre un cuadro de diálogo para importar contactos desde un archivo VCF.

        Comportamiento:
            - Solicita el nombre del archivo '.vcf'.
            - Agrega los contactos importados al usuario actual.
            - Registra éxito o cualquier error en el log.
        Excepciones:
            FileNotFoundError: Si el archivo no existe.
            ErrorArchivoCorrupto: Si el archivo está corrupto o no es válido.
        """
        layout = BoxLayout(orientation="vertical", spacing=10, padding=10)
        archivo_input = TextInput(hint_text="Nombre del archivo .vcf", multiline=False)
        layout.add_widget(archivo_input)

        importar_btn = Button(text="Importar", size_hint_y=None, height=40)
        cerrar_btn = Button(text="Cerrar", size_hint_y=None, height=40)
        layout.add_widget(importar_btn)
        layout.add_widget(cerrar_btn)

        popup = Popup(title="Importar Contactos", content=layout, size_hint=(0.8, 0.4))

        def importar_callback(instance):
            archivo = archivo_input.text.strip()
            if not archivo.endswith(".vcf"):
                print("Error: El archivo debe tener la extensión .vcf.")
            else:
                try:
                    contactos_importados = self.gestor_vcf.importar_contactos(archivo)
                    print(f"Contactos importados exitosamente desde '{archivo}'.")
                    popup.dismiss()
                except FileNotFoundError:
                    print(f"Error: El archivo '{archivo}' no existe.")
                except ErrorArchivoCorrupto:
                    print("Error: El archivo está corrupto o no se puede cargar.")
                except Exception as e:
                    print(f"Error al importar contactos: {e}")

        importar_btn.bind(on_press=importar_callback)
        cerrar_btn.bind(on_press=popup.dismiss)
        popup.open()

    def ver_contactos(self):
        """
        Muestra en el log la lista completa de contactos del usuario.

        Comportamiento:
            - Obtiene la lista de contactos del GestorDeContactos.
            - Registra cada contacto o un mensaje si la lista está vacía.
        """
        try:
            contactos = self.gestor_contactos.ver_contactos()
            if contactos:
                print("Lista de contactos:")
                for contacto in contactos:
                    print(f"{contacto.id} | {contacto.nombre} | {contacto.telefono} | {contacto.email} | {contacto.direccion} | {contacto.categoria}")
            else:
                print("No hay contactos disponibles.")
        except Exception as e:
            print(f"Error al ver contactos: {e}")

    def cerrar_sesion(self):
        """
        Cierra la sesión del usuario y retorna a la pantalla de login.

        Comportamiento:
            - Cambia la pantalla actual a 'login'.
            - Registra cualquier error en el log.
        """
        try:
            self.manager.current = "login"
        except Exception as e:
            print(f"Error al cerrar sesión: {e}")