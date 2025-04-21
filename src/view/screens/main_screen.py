from kivy.uix.screenmanager import Screen
from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from src.model.classes.contacto import Contacto
from src.model.classes.gestor_de_contactos import GestorDeContactos
from src.model.classes.gestor_vcf import GestorVCF

class MainScreen(Screen):
    def on_enter(self):
        self.gestor_contactos = GestorDeContactos(self.manager.usuario_actual)
        self.gestor_vcf = GestorVCF(self.manager.usuario_actual)

    def crear_contacto(self):
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
            datos = {
                "nombre": nombre_input.text,
                "telefono": telefono_input.text,
                "email": email_input.text,
                "direccion": direccion_input.text,
                "categoria": categoria_input.text,
            }
            contacto = Contacto(
                id=len(self.manager.usuario_actual.contactos) + 1,
                nombre=datos["nombre"],
                telefono=datos["telefono"],
                email=datos["email"],
                direccion=datos["direccion"],
                categoria=datos["categoria"],
            )
            self.gestor_contactos.agregar_contacto(contacto)
            print(f"Contacto '{contacto.nombre}' creado exitosamente.")
            popup.dismiss()
    
        guardar_btn.bind(on_press=guardar_callback)
        cerrar_btn.bind(on_press=popup.dismiss)
        popup.open()
    
    def editar_contacto(self):
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
        # Mostrar un formulario para buscar un contacto por nombre
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
                        print(f"{contacto.id} - {contacto.nombre}")
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
        # Mostrar un formulario para filtrar contactos por categoría
        layout = BoxLayout(orientation="vertical", spacing=10, padding=10)
        categoria_input = TextInput(hint_text="Categoría para filtrar")
        layout.add_widget(categoria_input)

        filtrar_btn = Button(text="Filtrar", size_hint_y=None, height=40)
        cerrar_btn = Button(text="Cerrar", size_hint_y=None, height=40)
        layout.add_widget(filtrar_btn)
        layout.add_widget(cerrar_btn)

        popup = Popup(title="Filtrar Contactos", content=layout, size_hint=(0.8, 0.4))

        def filtrar_callback(instance):
            categoria = categoria_input.text
            resultados = self.gestor_contactos.filtrar_contacto(categoria)
            if resultados:
                print(f"Contactos en la categoría '{categoria}':")
                for contacto in resultados:
                    print(f"{contacto.id} - {contacto.nombre}")
            else:
                print(f"No se encontraron contactos en la categoría '{categoria}'.")
            popup.dismiss()

        filtrar_btn.bind(on_press=filtrar_callback)
        cerrar_btn.bind(on_press=popup.dismiss)
        popup.open()

    def exportar_contactos(self):
        self.gestor_vcf.exportar_contactos(self.manager.usuario_actual.contactos, "contactos.vcf")
        print("Contactos exportados exitosamente a 'contactos.vcf'.")

    def importar_contactos(self):
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
                    self.manager.usuario_actual.contactos.extend(contactos_importados)
                    print(f"Contactos importados exitosamente desde '{archivo}'.")
                    popup.dismiss()
                except FileNotFoundError:
                    print(f"Error: El archivo '{archivo}' no existe.")
                except Exception as e:
                    print(f"Error al importar contactos: {e}")
    
        importar_btn.bind(on_press=importar_callback)
        cerrar_btn.bind(on_press=popup.dismiss)
        popup.open()

    def ver_contactos(self):
        # Mostrar la lista de contactos en la consola
        contactos = self.gestor_contactos.ver_contactos()
        if contactos:
            print("Lista de contactos:")
            for contacto in contactos:
                print(f"{contacto.id} - {contacto.nombre}")
        else:
            print("No hay contactos disponibles.")

    def cerrar_sesion(self):
        self.manager.current = "login"

    def _guardar_contacto(self, datos):
        contacto = Contacto(
            id=len(self.manager.usuario_actual.contactos) + 1,
            nombre=datos["nombre"],
            telefono=datos["telefono"],
            email=datos["email"],
            direccion=datos["direccion"],
            categoria=datos["categoria"],
        )
        self.gestor_contactos.agregar_contacto(contacto)
        print(f"Contacto '{contacto.nombre}' creado exitosamente.")

    def _actualizar_contacto(self, datos):
        contactos = self.gestor_contactos.ver_contactos()
        if contactos:
            contacto = contactos[0]  # Por simplicidad, editar el primer contacto
            contacto.nombre = datos["nombre"]
            contacto.telefono = datos["telefono"]
            contacto.email = datos["email"]
            contacto.direccion = datos["direccion"]
            contacto.categoria = datos["categoria"]
            print(f"Contacto '{contacto.nombre}' actualizado exitosamente.")
        else:
            print("No hay contactos para editar.")