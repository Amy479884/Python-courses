CREATE TABLE BOOK_KEEPING (
    NAME TEXT,
    LANGUAGE TEXT,
    GENRE TEXT,
    AUTHOR TEXT,
    YEAR INTEGER
);

INSERT INTO BOOK_KEEPING (NAME, LANGUAGE, GENRE, AUTHOR, YEAR)
VALUES
    ('MAGIC FOUNTAIN', 'GERMAN', 'FANTASY', 'THOMAS MANN', 1924),
    ('GERMINAL', 'FRENCH', 'FICTION', 'EMILE ZOLA', 1885),
    ('THE WHITE CASTLE', 'TURKISH', 'ROMANCE', 'ORHAN PAMUK', 1985),
    ('JANE EYRE', 'ENGLISH', 'CLASSICAL', 'CHARLOTTE BRONTE', 1847),
    ('PRIDE AND PREJUDICE', 'ENGLISH', 'CLASSICAL', 'JANE AUSTIN', 1797);

SELECT *
FROM BOOK_KEEPING
WHERE AUTHOR NOT LIKE 'C%';