CREATE TABLE tarea (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    descripcion VARCHAR(200) NOT NULL,
    fecha DATE NOT NULL
);


INSERT INTO tarea (name, descripcion, fecha) VALUES
('Preparar Presentación', 'Preparar diapositivas para la presentación de circuitos', '2024-08-15'),
('Estudiar factorizacion Matemática', 'Revisar y organizar apuntes de matemáticas para el examen final', '2024-08-20'),
('Completar Trabajo de Base de datos', 'Finalizar el informe de laboratorio para la clase de base de datos', '2024-08-25'),
('Estudiar para Examen de contabilidad', 'Estudiar los capítulos 5 a 8 del libro de contabilidad No.1', '2024-09-01'),
('Organizar Grupo de Estudio', 'Organizar un grupo de estudio para la preparación del examen de física', '2024-09-05'),
('Devolver Libros a la Biblioteca', 'Hacer un programa que devuelva los libros de la biblioteca de a la base de datos', '2024-09-10'),
('Preparar Exposición de Programacion', 'Preparar materiales y programas para la exposición de programacion', '2024-09-15'),
('Corregir Ensayo de Literatura', 'Corregir y mejorar el ensayo de literatura antes de la fecha de entrega', '2024-09-20'),
('Enviar Proyecto de Programación', 'Revisar y enviar el proyecto final de la clase de programación', '2024-09-25'),
('Resumen ejecutivo de Mercadotecnia', 'Hacer un resumen del tema visto en clase la semana pasada', '2024-09-30');