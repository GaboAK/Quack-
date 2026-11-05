-- =============================================
-- Base de datos para la aplicación Monedero
-- =============================================

-- 1. Crear la base de datos si no existe
CREATE DATABASE IF NOT EXISTS monedero_db 
CHARACTER SET utf8mb4 
COLLATE utf8mb4_unicode_ci;

-- 2. Usar la base de datos
USE monedero_db;

-- 3. Crear la tabla 'cajas' para almacenar la información
CREATE TABLE IF NOT EXISTS cajas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    categoria VARCHAR(100) NOT NULL,
    nombre_moneda VARCHAR(100) NOT NULL,
    cantidad INT NOT NULL,
    fecha_creacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 4. Datos de prueba iniciales (opcional)
INSERT INTO cajas (categoria, nombre_moneda, cantidad) VALUES
('Caja 1', 'Peso Colombiano', 50),
('Caja 1', 'Dólar Estadounidense', 20),
('Caja 2', 'Euro', 15),
('Caja 2', 'Libra Esterlina', 10);

-- 5. Consulta para obtener los registros organizados alfanuméricamente
-- SELECT * FROM cajas ORDER BY categoria ASC, nombre_moneda ASC;

