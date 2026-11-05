
CREATE DATABASE IF NOT EXISTS monedero_db 
CHARACTER SET utf8mb4 
COLLATE utf8mb4_unicode_ci;

USE monedero_db;

CREATE TABLE IF NOT EXISTS cajas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    categoria VARCHAR(100) NOT NULL,
    nombre_moneda VARCHAR(100) NOT NULL,
    cantidad INT NOT NULL,
    fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO cajas (categoria, nombre_moneda, cantidad) VALUES
('Caja 1', 'Peso Colombiano', 50),
('Caja 1', 'Dólar Estadounidense', 20),
('Caja 2', 'Euro', 15),
('Caja 2', 'Libra Esterlina', 10);

