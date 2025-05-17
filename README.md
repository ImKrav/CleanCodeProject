# Gestor de Contactos
El objetivo de este proyecto es desarrollar una aplicación para la gestión de contactos personales y profesionales, permitiendo almacenar, organizar y manipular información de manera eficiente.

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/ImKrav/CleanCodeProject?quickstart=1)

## Integrantes

- [Alejandro Bermudez Bedoya](https://github.com/ImKrav)
- [Juan David Mosquera Garcia](https://github.com/SHURECITO)

## Diagrama de Clases UML
![Diagrama de Clases](https://github.com/ImKrav/CleanCodeProject/blob/main/assets/DiagramaDeClases.png?raw=true)

## Diagrama ER
![Diagrama de ER](https://github.com/ImKrav/CleanCodeProject/blob/main/assets/DiagramaER.png?raw=true)

## Casos de Prueba

### **Funcionalidad 1:** Crear un contacto

#### ✅ Casos Normales
| # | Descripción | Resultado |
|---|------------|-----------|
| 1 | Crear contacto con nombre, teléfono, email, dirección y categoría válidos. | Contacto creado correctamente. |
| 2 | Crear contacto mínimo (solo con nombre y teléfono). | Contacto creado correctamente. |
| 3 | Crear contacto con categoría vacía. | Contacto creado correctamente (asignado automáticamente a "Sin asignar"). |

#### ⚠️ Casos Extremos
| # | Descripción | Resultado |
|---|------------|-----------|
| 1 | Crear contacto con un nombre de 100 caracteres. | Contacto creado correctamente. |
| 2 | Crear contacto con un número de teléfono con 20 dígitos. | Error: El número de teléfono es muy largo, debe tener como máximo 15 dígitos. |
| 3 | Crear contacto con un email extremadamente largo (más de 200 caracteres). | Contacto creado correctamente. |

#### ❌ Casos de Error
| # | Descripción | Resultado |
|---|------------|-----------|
| 1 | Crear contacto sin nombre. | Error: El nombre no puede estar vacío. |
| 2 | Crear contacto con un teléfono no numérico ("abc123"). | Error: El teléfono debe ser un valor numérico. |
| 3 | Crear contacto con un email sin "@" o con formato inválido. | Error: El email no tiene un formato válido. |

---

### **Funcionalidad 2:** Editar un contacto

#### ✅ Casos Normales
| # | Descripción | Resultado |
|---|------------|-----------|
| 1 | Editar el nombre de un contacto existente. | Contacto editado correctamente. |
| 2 | Editar el email de un contacto existente. | Contacto editado correctamente. |
| 3 | Editar la categoría de un contacto sin cambiar otros datos. | Contacto editado correctamente. |

#### ⚠️ Casos Extremos
| # | Descripción | Resultado |
|---|------------|-----------|
| 1 | Editar el nombre con 100 caracteres. | Contacto editado correctamente. |
| 2 | Editar el email con 200 caracteres. | Contacto editado correctamente. |
| 3 | Editar el teléfono con 20 dígitos. | Error: El número de teléfono es muy largo, debe tener como máximo 15 dígitos. |

#### ❌ Casos de Error
| # | Descripción | Resultado |
|---|------------|-----------|
| 1 | Editar un contacto que no existe. | Error: El contacto no existe |
| 2 | Editar un contacto con un teléfono no númerico. | Error: El teléfono debe ser un valor númerico. |
| 3 | Editar un contacto con un email inválido. | Error: El email no tiene un formato válido. |

---

### **Funcionalidad 3:** Filtrar contactos por nombre y categoría

#### ✅ Casos Normales
| # | Descripción | Resultado |
|---|------------|-----------|
| 1 | Filtrar contactos por nombre exacto. | Contactos filtrados correctamente. |
| 2 | Filtrar contactos por una categoría específica. | Contactos filtrados correctamente. |
| 3 | Filtrar contactos por un nombre parcial (búsqueda aproximada). | Contactos filtrados correctamente. |

#### ⚠️ Casos Extremos
| # | Descripción | Resultado |
|---|------------|-----------|
| 1 | Filtrar contactos con un nombre de 50 caracteres. | Contactos filtrados correctamente |
| 2 | Filtrar contactos con una categoría vacía. | Contactos filtrados correctamente |
| 3 | Filtrar contactos con un nombre con caracteres especiales. | Contactos filtrados correctamente. |

#### ❌ Casos de Error
| # | Descripción | Resultado |
|---|------------|-----------|
| 1 | Filtrar contactos con un nombre vacío. | Error: El nombre no puede estar vacío. |
| 2 | Filtrar contactos con una categoría inexistente. | Error: La categoría no existe. |
| 3 | Filtrar contactos con un tipo de dato incorrecto. | Error: Tipo de dato incorrecto. |

---

### **Funcionalidad 4:** Exportar e importar contactos en .vcf

#### ✅ Casos Normales
| # | Descripción | Resultado |
|---|------------|-----------|
| 1 | Exportar una lista con 5 contactos. | Contactos exportados correctamente |
| 2 | Importar un archivo `.vcf` válido con 3 contactos. | Contactos importados correctamente |
| 3 | Exportar contactos con nombres que contienen caracteres especiales. | Contactos exportados correctamente |


#### ⚠️ Casos Extremos
| # | Descripción | Resultado |
|---|------------|-----------|
| 1 | Exportar una lista con 1000 contactos. | Contactos exportados correctamente |
| 2 | Importar un `.vcf` con 500 contactos. | Contactos exportados correctamente |
| 3 | Exportar una lista vacía de contactos. | Error: La lista de contactos está vacía |


#### ❌ Casos de Error
| # | Descripción | Resultado |
|---|------------|-----------|
| 1 | Importar un archivo `.vcf` corrupto. | Error: El archivo está corrupto o no se puede cargar |
| 2 | Importar un archivo que no es `.vcf`. | Error: El archivo no es un archivo de extensión .vcf |
| 3 | Exportar contactos sin permisos de escritura en la carpeta destino. | Error: No tienes permisos de escritura en el directorio de destino |

---

### **Funcionalidad 5:** Crear un usuario

#### ✅ Casos Normales
| # | Descripción | Resultado |
|---|------------|-----------|
| 1 | Crear usuario con nombre, email y contraseña válidos. | Usuario creado correctamente |
| 2 | Crear usuario con un email corto pero válido. | Usuario creado correctamente |
| 3 | Crear usuario con una contraseña de 8 caracteres. | Usuario creado correctamente |

#### ⚠️ Casos Extremos
| # | Descripción | Resultado |
|---|------------|-----------|
| 1 | Crear usuario con un nombre de 50 caracteres. | Usuario creado correctamente |
| 2 | Crear usuario con una contraseña de 100 caracteres. | Error: La contraseña es muy larga, debe tener como máximo 20 caracteres |
| 3 | Crear usuario con un email extremadamente largo. | Usuario creado correctamente |

#### ❌ Casos de Error
| # | Descripción | Resultado |
|---|------------|-----------|
| 1 | Crear usuario con email inválido. | Error: El email no tiene un formato válido |
| 2 | Crear usuario con contraseña vacía. | Error: La contraseña no puede estar vacía |
| 3 | Crear usuario con un email ya registrado. | Error: El email ya está registrado |

---

### **Funcionalidad 6:** Iniciar sesión

#### ✅ Casos Normales
| # | Descripción | Resultado |
|---|------------|-----------|
| 1 | Iniciar sesión con credenciales correctas. | Sesión iniciada correctamente |
| 2 | Iniciar sesión con email en mayúsculas. | Sesión iniciada correctamente |
| 3 | Iniciar sesión inmediatamente después de registrarse. | Sesión iniciada correctamente |

#### ⚠️ Casos Extremos
| # | Descripción | Resultado |
|---|------------|-----------|
| 1 | Iniciar sesión con una contraseña de 50 caracteres. | Error: La contraseña es muy larga, debe tener como máximo 20 caracteres |
| 2 | Iniciar sesión después de haber creado 1000 usuarios en la base de datos. | Sesión iniciada correctamente |
| 3 | Iniciar sesión con una contraseña con caracteres especiales. | Sesión iniciada correctamente |

#### ❌ Casos de Error
| # | Descripción | Resultado |
|---|------------|-----------|
| 1 | Iniciar sesión con email inexistente. | Error: El usuario no existe |
| 2 | Iniciar sesión con contraseña incorrecta. | Error: La contraseña es incorrecta |
| 3 | Iniciar sesión con email vacío. | Error: Faltan campos obligatorios por llenar |
