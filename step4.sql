CREATE TABLE members (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    surname VARCHAR(100),
    contact VARCHAR(100),
    expirience VARCHAR(100),
    description VARCHAR(100)
);

CREATE TABLE projects(
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    status VARCHAR(100),
    description VARCHAR(100),
    date_start DATE,
    date_end DATE,
    link VARCHAR(100)
);

CREATE TABLE events(
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    description VARCHAR(100),
    date_start DATE,
    date_end DATE,
    link VARCHAR(100)
);