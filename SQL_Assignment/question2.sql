--using existing database
USE Tech4Girls_DB;

--creating post table
CREATE TABLE IF NOT EXISTS Posts(
    id INT AUTO_INCREAMENT PRIMARY KEY,
    user_id INT,
    title VARCHAR(255),
    content TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

--inserting data into post table to establish a one-to many relationship 
INSERT INTO posts (user_id, title, content, created_at)
VALUES (1, 'first post', 'content of ama', '2024-11-01 10:45:00'),
       (1, 'second post', 'more content from ama', '2024-11-01 11:30:00'),
       (2, 'first post', 'content of abena', '2024-11-02 12:45:00'),
       (3, 'first post', 'content of adjoa', '2024-11-03 14:20:00');
