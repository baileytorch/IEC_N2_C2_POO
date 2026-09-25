INSERT INTO autores (nombre,pseudonimo,nacionalidad,fecha_nacimiento,fecha_defuncion) VALUES
('John Ronald Reuel Tolkien', 
    NULL, 
    SELECT id_pais FROM paises WHERE nombre = 'Reino Unido',
    STR_TO_DATE('03/01/1892', '%d/%m/%Y'),
    STR_TO_DATE('02/11/1973', '%d/%m/%Y')),
('Lucila de María Del Perpetuo Socorro Godoy Alcayaga',
    'Gabriela Mistral', 
    SELECT id_pais FROM paises WHERE nombre = 'Chile',
    STR_TO_DATE('07/04/1889', '%d/%m/%Y'),
    STR_TO_DATE('10/01/1957', '%d/%m/%Y'));

