-- Nebraska, Iowa, Illinois, Indiana, or Ohio.

CREATE TABLE nebraska_weather(
    id INT PRIMARY KEY AUTO_INCREMENT,
    the_date DATE NOT NULL,
    max_temp INT NOT NULL,
    min_temp INT NOT NULL,
    precipitation INT NOT NULL
);

CREATE TABLE iowa_weather(
    id INT PRIMARY KEY AUTO_INCREMENT,
    the_date DATE NOT NULL,
    max_temp INT NOT NULL,
    min_temp INT NOT NULL,
    precipitation INT NOT NULL
);

CREATE TABLE illinois_weather(
    id INT PRIMARY KEY AUTO_INCREMENT,
    the_date DATE NOT NULL,
    max_temp INT NOT NULL,
    min_temp INT NOT NULL,
    precipitation INT NOT NULL
);

CREATE TABLE indiana_weather(
    id INT PRIMARY KEY AUTO_INCREMENT,
    the_date DATE NOT NULL,
    max_temp INT NOT NULL,
    min_temp INT NOT NULL,
    precipitation INT NOT NULL
);

CREATE TABLE ohio_weather(
    id INT PRIMARY KEY AUTO_INCREMENT,
    the_date DATE NOT NULL,
    max_temp INT NOT NULL,
    min_temp INT NOT NULL,
    precipitation INT NOT NULL
);

/* -- SQL statements to insert data from csv files */
/* LOAD DATA INFILE '/home/ephantus/kevinfiles/coding/nebraska.csv' */
/* INTO TABLE nebraska_weather */
/* FIELDS TERMINATED BY ',' */
/* LINES TERMINATED BY '\n' */
/* (the_date, max_temp, min_temp, precipitation); */
/*  */
/* LOAD DATA INFILE '/home/ephantus/kevinfiles/coding/iowa.csv' */
/* INTO TABLE iowa_weather */
/* FIELDS TERMINATED BY ',' */
/* LINES TERMINATED BY '\n' */
/* (the_date, max_temp, min_temp, precipitation); */
/*  */
/* LOAD DATA INFILE '/home/ephantus/kevinfiles/coding/illinois.csv' */
/* INTO TABLE illinois_weather */
/* FIELDS TERMINATED BY ',' */
/* LINES TERMINATED BY '\n' */
/* (the_date, max_temp, min_temp, precipitation); */
/*  */
/* LOAD DATA INFILE '/home/ephantus/kevinfiles/coding/indiana.csv' */
/* INTO TABLE indiana_weather */
/* FIELDS TERMINATED BY ',' */
/* LINES TERMINATED BY '\n' */
/* (the_date, max_temp, min_temp, precipitation); */
/*  */
/* LOAD DATA INFILE '/home/ephantus/kevinfiles/coding/iowa.csv' */
/* INTO TABLE iowa_weather */
/* FIELDS TERMINATED BY ',' */
/* LINES TERMINATED BY '\n' */
/* (the_date, max_temp, min_temp, precipitation); */

CREATE UNIQUE INDEX weather_index ON nebraska_weather (id, the_date, max_temp, min_temp, precipitation);
CREATE UNIQUE INDEX weather_index ON iowa_weather (id, the_date, max_temp, min_temp, precipitation);
CREATE UNIQUE INDEX weather_index ON indiana_weather (id, the_date, max_temp, min_temp, precipitation);
CREATE UNIQUE INDEX weather_index ON illinois_weather (id, the_date, max_temp, min_temp, precipitation);
CREATE UNIQUE INDEX weather_index ON ohio_weather (id, the_date, max_temp, min_temp, precipitation);
