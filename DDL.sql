-- CREAR TABLAS
CREATE TABLE Usuarios (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password VARCHAR(100) NOT NULL
);

CREATE TABLE Contactos (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    telefono VARCHAR(15) NOT NULL,
    email VARCHAR(100),
    direccion VARCHAR(255),
    categoria VARCHAR(50) DEFAULT 'Sin asignar',
    usuario_id INTEGER REFERENCES Usuarios(id) ON DELETE CASCADE
);

-- CONSULTAS
SELECT * FROM Usuarios;

SELECT * FROM Contactos;