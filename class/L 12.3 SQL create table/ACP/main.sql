CREATE TABLE IF NOT EXISTS cats (
  cat_name TEXT PRIMARY KEY,
  cat_age REAL,
  cat_breed TEXT,
  cat_color TEXT 
);

INSERT INTO cats (cat_name, cat_age, cat_breed, cat_color) VALUES
  ('Honey', 4, 'Maine Coon', 'Brown'),
  ('Tiger', 2, 'Siamese', 'Ginger'),
  ('Andy', 12, 'Ragdoll', 'Black and white'),
  ('Sweety', 1.5, 'Scottish Fold', 'Brown and white'),
  ('Shadow', 10, 'British longhair', 'Black'),
  ('Rose', 8, 'British longhair', 'Black');

SELECT * FROM cats;

SELECT cat_name, cat_age FROM cats;