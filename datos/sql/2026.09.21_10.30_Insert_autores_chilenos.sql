INSERT INTO autores (nombre, pseudonimo, nacionalidad, fecha_nacimiento, fecha_defuncion) VALUES

('Alonso de Ercilla', NULL, (SELECT id_pais FROM paises WHERE nombre = 'Chile'), STR_TO_DATE('07/08/1533', '%d/%m/%Y'), STR_TO_DATE('29/11/1594', '%d/%m/%Y')),
('Andres Bello', NULL, (SELECT id_pais FROM paises WHERE nombre = 'Chile'), STR_TO_DATE('29/11/1781', '%d/%m/%Y'), STR_TO_DATE('15/10/1865', '%d/%m/%Y')),
('Alberto Blest Gana', NULL, (SELECT id_pais FROM paises WHERE nombre = 'Chile'), STR_TO_DATE('04/05/1830', '%d/%m/%Y'), STR_TO_DATE('09/11/1920', '%d/%m/%Y')),
('Baldomero Lillo', NULL, (SELECT id_pais FROM paises WHERE nombre = 'Chile'), STR_TO_DATE('06/01/1867', '%d/%m/%Y'), STR_TO_DATE('10/09/1923', '%d/%m/%Y')),
-- ('Lucila de Maria del Perpetuo Socorro Godoy Alcayaga', 'Gabriela Mistral', (SELECT id_pais FROM paises WHERE nombre = 'Chile'), STR_TO_DATE('07/04/1889', '%d/%m/%Y'), STR_TO_DATE('10/01/1957', '%d/%m/%Y')),
('Ricardo Eliecer Neftali Reyes Basoalto', 'Pablo Neruda', (SELECT id_pais FROM paises WHERE nombre = 'Chile'), STR_TO_DATE('12/07/1904', '%d/%m/%Y'), STR_TO_DATE('23/09/1973', '%d/%m/%Y')),
('Vicente Huidobro', NULL, (SELECT id_pais FROM paises WHERE nombre = 'Chile'), STR_TO_DATE('10/01/1893', '%d/%m/%Y'), STR_TO_DATE('02/01/1948', '%d/%m/%Y')),
('Manuel Rojas', NULL, (SELECT id_pais FROM paises WHERE nombre = 'Chile'), STR_TO_DATE('08/01/1896', '%d/%m/%Y'), STR_TO_DATE('11/03/1973', '%d/%m/%Y')),
('Maria Luisa Bombal', NULL, (SELECT id_pais FROM paises WHERE nombre = 'Chile'), STR_TO_DATE('08/06/1910', '%d/%m/%Y'), STR_TO_DATE('06/05/1980', '%d/%m/%Y')),
('Nicanor Parra', NULL, (SELECT id_pais FROM paises WHERE nombre = 'Chile'), STR_TO_DATE('05/09/1914', '%d/%m/%Y'), STR_TO_DATE('23/01/2018', '%d/%m/%Y')),
('Jose Donoso', NULL, (SELECT id_pais FROM paises WHERE nombre = 'Chile'), STR_TO_DATE('05/10/1924', '%d/%m/%Y'), STR_TO_DATE('07/12/1996', '%d/%m/%Y')),
('Enrique Lafourcade', NULL, (SELECT id_pais FROM paises WHERE nombre = 'Chile'), STR_TO_DATE('14/10/1927', '%d/%m/%Y'), STR_TO_DATE('29/07/2019', '%d/%m/%Y')),
('Jorge Edwards', NULL, (SELECT id_pais FROM paises WHERE nombre = 'Chile'), STR_TO_DATE('29/06/1931', '%d/%m/%Y'), STR_TO_DATE('17/03/2023', '%d/%m/%Y')),
('Isabel Allende', NULL, (SELECT id_pais FROM paises WHERE nombre = 'Chile'), STR_TO_DATE('02/08/1942', '%d/%m/%Y'), NULL),
('Antonio Skarmeta', NULL, (SELECT id_pais FROM paises WHERE nombre = 'Chile'), STR_TO_DATE('07/11/1940', '%d/%m/%Y'), STR_TO_DATE('15/10/2024', '%d/%m/%Y')),
('Roberto Bolaño', NULL, (SELECT id_pais FROM paises WHERE nombre = 'Chile'), STR_TO_DATE('28/04/1953', '%d/%m/%Y'), STR_TO_DATE('15/07/2003', '%d/%m/%Y')),
('Esther Huneeus Salas', 'Marcela Paz', (SELECT id_pais FROM paises WHERE nombre = 'Chile'), STR_TO_DATE('28/02/1902', '%d/%m/%Y'), STR_TO_DATE('12/06/1985', '%d/%m/%Y'));
