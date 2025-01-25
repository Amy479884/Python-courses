CREATE TABLE supplier (
 SNO TEXT PRIMARY KEY,
 SNAME TEXT,
 STATUS INTEGER,
 CITY TEXT
 );

INSERT INTO supplier (SNO, SNAME, STATUS, CITY) VALUES
 ('S2', 'Smith',20, 'London'),
 ('S2', 'Jones',10, 'Paris'),
 ('S3','Blake',30, 'Zurich'),
 ('S4', 'Clarke',20, 'New York'),
 ('S5', 'Adama', 30, 'Athens');

SELECT * FROM supplier;