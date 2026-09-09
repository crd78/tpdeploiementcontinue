CREATE TABLE IF NOT EXISTS clients (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL
);

INSERT INTO clients (id, name) VALUES
    (1, 'Alice Martin'),
    (2, 'Bruno Durand'),
    (3, 'Chloé Bernard')
ON DUPLICATE KEY UPDATE name = VALUES(name);
