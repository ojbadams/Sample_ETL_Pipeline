CREATE DATABASE Staging;
CREATE DATABASE Core;

CREATE TABLE Staging.locations(
    commonName VARCHAR(250),
    lat VARCHAR(250),
    lon VARCHAR(250),
    id  VARCHAR(250) PRIMARY KEY
);

CREATE TABLE Core.locations(
    commonName VARCHAR(250),
    lat FLOAT,
    lon FLOAT,
    id  VARCHAR(250) PRIMARY KEY
);

CREATE USER `python`@`%` IDENTIFIED BY '12345';
GRANT ALL PRIVILEGES ON *.* TO `python`@`%` WITH GRANT OPTION;
FLUSH PRIVILEGES;
