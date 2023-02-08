-- Store the avg(min temp) avg(max temp) sum(precipitation) in a new table
-- for each state.

-- create 5 tables for each state.
CREATE TABLE nebraska_stats_data(
    id INT PRIMARY KEY AUTO_INCREMENT,
    year INT NOT NULL,
    average_max_temp INT NOT NULL,
    average_min_temp INT NOT NULL,
    precipitation_sum INT NOT NULL
);

CREATE TABLE iowa_stats_data(
    id INT PRIMARY KEY AUTO_INCREMENT,
    year INT NOT NULL,
    average_max_temp INT NOT NULL,
    average_min_temp INT NOT NULL,
    precipitation_sum INT NOT NULL
);

CREATE TABLE ohio_stats_data(
    id INT PRIMARY KEY AUTO_INCREMENT,
    year INT NOT NULL,
    average_max_temp INT NOT NULL,
    average_min_temp INT NOT NULL,
    precipitation_sum INT NOT NULL

);

CREATE TABLE indiana_stats_data(
    id INT PRIMARY KEY AUTO_INCREMENT,
    year INT NOT NULL,
    average_max_temp INT NOT NULL,
    average_min_temp INT NOT NULL,
    precipitation_sum INT NOT NULL
);

CREATE TABLE illinois_stats_data(
    id INT PRIMARY KEY AUTO_INCREMENT,
    year INT NOT NULL,
    average_max_temp INT NOT NULL,
    average_min_temp INT NOT NULL,
    precipitation_sum INT NOT NULL
);

