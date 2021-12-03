DROP TABLE bookings;
DROP TABLE members;
DROP TABLE fitnessclasses;

CREATE TABLE members (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    age INT
);

CREATE TABLE fitnessclasses (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    type VARCHAR(255),
    date INT,
    duration INT
);

CREATE TABLE bookings (
    id SERIAL PRIMARY KEY,
    member_id INT REFERENCES members(id) ON DELETE CASCADE,
    fitnessclass_id INT REFERENCES fitnessclasses(id) ON DELETE CASCADE
);