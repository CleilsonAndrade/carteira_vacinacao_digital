DROP TABLE IF EXISTS criancas;

CREATE TABLE criancas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    created DATETIME DEFAULT CURRENT_TIMESTAMP,
    usuario TEXT NOT NULL,
    email TEXT NOT NULL,
    sexo TEXT NOT NULL,
    idade TEXT NOT NULL,
    vacina1 TEXT,
    vacina2 TEXT,
    vacina3 TEXT,
    vacina4 TEXT,
    vacina5 TEXT,
    vacina6 TEXT,
    vacina7 TEXT,
    vacina8 TEXT,
    vacina9 TEXT,
    vacina10 TEXT
);


DROP TABLE IF EXISTS adultos;

CREATE TABLE adultos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    created DATETIME DEFAULT CURRENT_TIMESTAMP,
    usuario TEXT NOT NULL,
    email TEXT NOT NULL,
    sexo TEXT NOT NULL,
    idade TEXT NOT NULL,
    vacina1 TEXT,
    vacina2 TEXT,
    vacina3 TEXT,
    vacina4 TEXT,
    vacina5 TEXT
);

DROP TABLE IF EXISTS idosos;

CREATE TABLE idosos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    created DATETIME DEFAULT CURRENT_TIMESTAMP,
    usuario TEXT NOT NULL,
    email TEXT NOT NULL,
    sexo TEXT NOT NULL,
    idade TEXT NOT NULL,
    vacina1 TEXT,
    vacina2 TEXT,
    vacina3 TEXT,
    vacina4 TEXT,
    vacina5 TEXT
);