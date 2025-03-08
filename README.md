# Gestor de Contactos
El objetivo de este proyecto es desarrollar una aplicación para la gestión de contactos personales y profesionales, permitiendo almacenar, organizar y manipular información de manera eficiente.

## Casos de Prueba

### **Funcionalidad 1:** Crear un contacto

#### ✅ Casos Normales
| # | Descripción |
|---|------------|
| 1 | Crear contacto con nombre, teléfono, email, dirección y categoría válidos. |
| 2 | Crear contacto minimo (solo con nombre y teléfono). |
| 3 | Crear contacto con categoría vacía. |

#### 🚀 Casos Extremos
| # | Descripción |
|---|------------|
| 1 | Crear contacto con un nombre de 100 caracteres. |
| 2 | Crear contacto con un número de teléfono con 20 dígitos. |
| 3 | Crear contacto con un email extremadamente largo (más de 200 caracteres). |

#### ❌ Casos de Error
| # | Descripción |
|---|------------|
| 1 | Crear contacto sin nombre. |
| 2 | Crear contacto con un teléfono no numérico ("abc123"). |
| 3 | Crear contacto con un email sin "@" o con formato inválido. |

---

### **Funcionalidad 2:** Editar un contacto

#### ✅ Casos Normales
| # | Descripción |
|---|------------|
| 1 | Editar el nombre de un contacto existente. |
| 2 | Editar el email de un contacto existente. |
| 3 | Editar la categoría de un contacto sin cambiar otros datos. |

#### 🚀 Casos Extremos
| # | Descripción |
|---|------------|
| 1 | Editar el nombre con 100 caracteres. |
| 2 | Editar el email con 200 caracteres. |
| 3 | Editar el teléfono con 20 dígitos. |

#### ❌ Casos de Error
| # | Descripción |
|---|------------|
| 1 | Editar un contacto que no existe. |
| 2 | Editar un contacto dejando el nombre vacío. |
| 3 | Editar un contacto con un email inválido. |

---

### **Funcionalidad 3:** Filtrar contactos por nombre y categoría

#### ✅ Casos Normales
| # | Descripción |
|---|------------|
| 1 | Filtrar contactos por nombre exacto. |
| 2 | Filtrar contactos por una categoría específica. |
| 3 | Filtrar contactos por un nombre parcial (búsqueda aproximada). |

#### 🚀 Casos Extremos
| # | Descripción |
|---|------------|
| 1 | Filtrar contactos con un nombre de 50 caracteres. |
| 2 | Filtrar contactos con una categoría inexistente. |
| 3 | Filtrar contactos con un nombre con caracteres especiales. |

#### ❌ Casos de Error
| # | Descripción |
|---|------------|
| 1 | Filtrar contactos con un nombre vacío. |
| 2 | Filtrar contactos con una categoría vacía. |
| 3 | Filtrar contactos con un tipo de dato incorrecto (número en vez de string). |

---

### **Funcionalidad 4:** Exportar e importar contactos en .vcf

#### ✅ Casos Normales
| # | Descripción |
|---|------------|
| 1 | Exportar una lista con 5 contactos. |
| 2 | Importar un archivo `.vcf` válido con 3 contactos. |
| 3 | Exportar una lista vacía de contactos. |

#### 🚀 Casos Extremos
| # | Descripción |
|---|------------|
| 1 | Exportar una lista con 1000 contactos. |
| 2 | Importar un `.vcf` con 500 contactos. |
| 3 | Exportar un contacto con nombre y teléfono muy largos. |

#### ❌ Casos de Error
| # | Descripción |
|---|------------|
| 1 | Importar un archivo `.vcf` corrupto. |
| 2 | Importar un archivo que no es `.vcf`. |
| 3 | Exportar contactos sin permisos de escritura en la carpeta destino. |

---

### **Funcionalidad 5:** Crear un usuario

#### ✅ Casos Normales
| # | Descripción |
|---|------------|
| 1 | Crear usuario con nombre, email y contraseña válidos. |
| 2 | Crear usuario con un email corto pero válido. |
| 3 | Crear usuario con una contraseña de 8 caracteres. |

#### 🚀 Casos Extremos
| # | Descripción |
|---|------------|
| 1 | Crear usuario con un nombre de 50 caracteres. |
| 2 | Crear usuario con una contraseña de 100 caracteres. |
| 3 | Crear usuario con un email extremadamente largo. |

#### ❌ Casos de Error
| # | Descripción |
|---|------------|
| 1 | Crear usuario con email inválido. |
| 2 | Crear usuario con contraseña vacía. |
| 3 | Crear usuario con un email ya registrado. |

---

### **Funcionalidad 6:** Iniciar sesión

#### ✅ Casos Normales
| # | Descripción |
|---|------------|
| 1 | Iniciar sesión con credenciales correctas. |
| 2 | Iniciar sesión con email en mayúsculas (debe ser insensible a mayúsculas/minúsculas). |
| 3 | Iniciar sesión inmediatamente después de registrarse. |

#### 🚀 Casos Extremos
| # | Descripción |
|---|------------|
| 1 | Iniciar sesión con una contraseña de 50 caracteres. |
| 2 | Iniciar sesión después de haber creado 1000 usuarios en la base de datos. |
| 3 | Iniciar sesión con una contraseña con caracteres especiales. |

#### ❌ Casos de Error
| # | Descripción |
|---|------------|
| 1 | Iniciar sesión con email inexistente. |
| 2 | Iniciar sesión con contraseña incorrecta. |
| 3 | Iniciar sesión con email vacío. |

