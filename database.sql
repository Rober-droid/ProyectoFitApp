CREATE DATABASE IF NOT EXISTS zona_fit_db;
USE zona_fit_db;

CREATE TABLE IF NOT EXISTS cliente(
    id_categoria INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) ,
    apellido VARCHAR(50),
    membresia INT
);

