-- Create the cats table
CREATE TABLE cats (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    breed VARCHAR(100),
    age INTEGER
);

-- Insert sample data into the cats table
INSERT INTO cats (name, breed, age) VALUES
('Whiskers', 'Siamese', 2),
('Shadow', 'Domestic Shorthair', 5),
('Luna', 'Maine Coon', 1),
('Oliver', 'British Shorthair', 3),
('Leo', 'Bengal', 4),
('Milo', 'Persian', 6),
('Cleo', 'Sphynx', 2),
('Simba', 'Abyssinian', 1),
('Nala', 'Ragdoll', 5),
('Jasper', 'Scottish Fold', 3),
('Mittens', 'Domestic Longhair', 7);
