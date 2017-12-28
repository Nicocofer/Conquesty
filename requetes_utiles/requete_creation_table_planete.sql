DROP TABLE Planete;
CREATE TABLE Planete(
     id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
     name TEXT,
     population INTEGER,
     population_max INTEGER,
     metal INTEGER,
     metal_max INTEGER,
     cristal INTEGER,
     cristal_max INTEGER,
     gaz INTEGER,
     gaz_max INTEGER,
     energie INTEGER,
     type INTEGER,
     armure INTEGER,
     attaque INTEGER,
     id_proprio INTEGER,
     systeme INTEGER,
     galaxie INTEGER,
     x FLOAT,
     y FLOAT
)
