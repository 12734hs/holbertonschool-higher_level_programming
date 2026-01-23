-- Hello popl
SELECT name FROM cities WHERE cities.id = (SELECT id FROM states) ORDER BY cities.id ASC;
