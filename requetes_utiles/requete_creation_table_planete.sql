DROP TABLE Planete;
CREATE TABLE Planete(
     id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
     name TEXT,
     population INTERGER,
     metal INTERGER,
     metal_max INTERGER,
     cristal INTERGER,
     cristal_max INTERGER,
     gaz INTERGER,
     gaz_max INTERGER,
     energie INTERGER,
     type INTERGER,
     armure INTERGER,
     attaque INTERGER,
     id_proprio INTERGER,
     systeme INTERGER,
     galaxie INTERGER,
     x FLOAT,
     y FLOAT
)
