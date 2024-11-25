--creating a database
CREATE DATABASE Tech4Girls_DB;

USE Tech4Girls_DB;

--creating user table
CREATE TABLE users(
    id INT AUTO_INCREAMENT PRIMARY KEY,
    username VARCHAR(50),
    email VARCHAR(100),
    created_at TIMESTAMP DEFAULT
    CURRENT_TIMESTAMP
);

--inserting data into the user table
INSERT INTO users (username, email, created_at)
VALUES ('ama','ama@example.com',2024-11-01 10:30:00);

INSERT INTO users (username, email, created_at)
VALUES ('abena','abena@example.com',2024-11-02 12:00:00);

INSERT INTO users (username, email, created_at)
VALUES ('adjoa','adjoa@example.com',2024-11-03 14:15:00);