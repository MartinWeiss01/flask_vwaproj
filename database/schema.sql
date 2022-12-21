DROP TABLE IF EXISTS roles;
DROP TABLE IF EXISTS materials;
DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS addresses;
DROP TABLE IF EXISTS prices;
DROP TABLE IF EXISTS collections;

CREATE TABLE roles (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  title TEXT NOT NULL
);

CREATE TABLE materials (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL
);

CREATE TABLE users (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  email TEXT NOT NULL,
  password TEXT NOT NULL,
  phone TEXT NOT NULL,
  firstname TEXT NOT NULL,
  lastname TEXT NOT NULL,
  registration INTEGER DEFAULT CURRENT_TIMESTAMP,
  activation INTEGER,
  activated INTEGER DEFAULT 0,
  roles_id INTEGER NOT NULL,
  FOREIGN KEY (roles_id) REFERENCES roles (id)
);

CREATE TABLE addresses (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  main INTEGER DEFAULT 0 NOT NULL,
  street TEXT NOT NULL,
  city TEXT NOT NULL,
  postalcode INTEGER NOT NULL,
  users_id INTEGER NOT NULL,
  FOREIGN KEY (users_id) REFERENCES users (id)
);

CREATE TABLE prices (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  price REAL NOT NULL,
  added INTEGER DEFAULT CURRENT_TIMESTAMP NOT NULL,
  materials_id INTEGER NOT NULL,
  FOREIGN KEY (materials_id) REFERENCES materials (id)
);

CREATE TABLE collections (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  weight REAL NOT NULL,
  received INTEGER CURRENT_TIMESTAMP NOT NULL,
  description TEXT,
  users_id INTEGER NOT NULL,
  materials_id INTEGER NOT NULL,
  FOREIGN KEY (users_id) REFERENCES users (id),
  FOREIGN KEY (materials_id) REFERENCES materials (id)
);

-------- Insert initial data
INSERT INTO roles (title) VALUES ('default');
INSERT INTO roles (title) VALUES ('limited_admin');
INSERT INTO roles (title) VALUES ('employee');
INSERT INTO roles (title) VALUES ('admin');




INSERT INTO materials (name) VALUES ('Železo');
INSERT INTO materials (name) VALUES ('Ocel');
INSERT INTO materials (name) VALUES ('Hliník');
INSERT INTO materials (name) VALUES ('Měď');
INSERT INTO materials (name) VALUES ('Mosaz');
INSERT INTO materials (name) VALUES ('Stříbro');
INSERT INTO materials (name) VALUES ('Zlato');
INSERT INTO materials (name) VALUES ('Platina');




INSERT INTO users (email, password, phone, firstname, lastname, registration, activation, activated, roles_id) VALUES ('282367de@seznam45164.local', '55863a2db485cd281fa934bfff935bb3f689dd8775d3b9f3df95456867c02966', '+420733125243', 'Anna', 'Novotná', '1664624041', '1664710441', 1, 4);
INSERT INTO users (email, password, phone, firstname, lastname, registration, activation, activated, roles_id) VALUES ('09e8b2c1@seznam14441.local', '55863a2db485cd281fa934bfff935bb3f689dd8775d3b9f3df95456867c02966', '+421733126251', 'Aleš', 'Nový', '1664788932', '1664875332', 1, 3);
INSERT INTO users (email, password, phone, firstname, lastname, registration, activation, activated, roles_id) VALUES ('b7db49a4@seznam8641.local', '55863a2db485cd281fa934bfff935bb3f689dd8775d3b9f3df95456867c02966', '+420733125242', 'Boris', 'Starý', '1664980172', '1665066572', 1, 2);
INSERT INTO users (email, password, phone, firstname, lastname, registration, activation, activated, roles_id) VALUES ('570b615b@seznam44866.local', '55863a2db485cd281fa934bfff935bb3f689dd8775d3b9f3df95456867c02966', '+421733126252', 'Berta', 'Mladá', '1667409106', '1667495506', 1, 1);
INSERT INTO users (email, password, phone, firstname, lastname, registration, roles_id) VALUES ('bf41c779@seznam7942.local', '55863a2db485cd281fa934bfff935bb3f689dd8775d3b9f3df95456867c02966', '+420733125241', 'Karel', 'Dlouhý', '1667548925', 1);
INSERT INTO users (email, password, phone, firstname, lastname, registration, roles_id) VALUES ('5ca935a9@seznam21476.local', '55863a2db485cd281fa934bfff935bb3f689dd8775d3b9f3df95456867c02966', '+421733126253', 'Klára', 'Prokopová', '1667738649', 1);
---2022-10-01T11:34:01+00:00	1664624041	Sat, 01 Oct 2022 11:34:01 +0000   activation: +1 day (24*60*60) = 1664710441
---2022-10-03T09:22:12+00:00	1664788932	Mon, 03 Oct 2022 09:22:12 +0000   activation: +1 day (24*60*60) = 1664875332
---2022-10-05T14:29:32+00:00	1664980172	Wed, 05 Oct 2022 14:29:32 +0000   activation: +1 day (24*60*60) = 1665066572
---2022-11-02T17:11:46+00:00	1667409106	Wed, 02 Nov 2022 17:11:46 +0000   activation: +1 day (24*60*60) = 1667495506
---2022-11-04T08:02:05+00:00	1667548925	Fri, 04 Nov 2022 08:02:05 +0000   activation: +1 day (24*60*60) = 1667635325
---2022-11-06T12:44:09+00:00	1667738649	Sun, 06 Nov 2022 12:44:09 +0000   activation: +1 day (24*60*60) = 1667825049




INSERT INTO addresses (street, city, postalcode, users_id) VALUES ('Adamcova 23', 'Brno', 62378, 1);
INSERT INTO addresses (street, city, postalcode, users_id) VALUES ('Dlouhá 31', 'Praha', 62007, 2);
INSERT INTO addresses (street, city, postalcode, users_id) VALUES ('Husova 32', 'Liberec', 62252, 3);
INSERT INTO addresses (street, city, postalcode, users_id) VALUES ('Smetanova 37', 'Třinec', 62035, 4);
INSERT INTO addresses (main, street, city, postalcode, users_id) VALUES (0, 'Aloise Havla 45', 'Brno', 62833, 5);
INSERT INTO addresses (main, street, city, postalcode, users_id) VALUES (0, 'Bakalovo nábřeží 61', 'Brno', 62730, 6);
INSERT INTO addresses (main, street, city, postalcode, users_id) VALUES (1, 'Bohatcova 15', 'Brno', 62514, 1);
INSERT INTO addresses (main, street, city, postalcode, users_id) VALUES (1, 'Celní 21', 'Brno', 62953, 5);
INSERT INTO addresses (main, street, city, postalcode, users_id) VALUES (1, 'Divišova 54', 'Brno', 62228, 3);




-- 2022-09-01T08:10:00+00:00	1662019800	Thu, 01 Sep 2022 08:10:00 +0000
INSERT INTO prices (price, added, materials_id) VALUES ('317', '1662019800', 1);
INSERT INTO prices (price, added, materials_id) VALUES ('481', '1662019800', 2);
INSERT INTO prices (price, added, materials_id) VALUES ('6', '1662019800', 3);
INSERT INTO prices (price, added, materials_id) VALUES ('297', '1662019800', 4);
INSERT INTO prices (price, added, materials_id) VALUES ('349', '1662019800', 5);
INSERT INTO prices (price, added, materials_id) VALUES ('290', '1662019800', 6);
INSERT INTO prices (price, added, materials_id) VALUES ('336', '1662019800', 7);
INSERT INTO prices (price, added, materials_id) VALUES ('494', '1662019800', 8);
-- 2022-09-19T08:10:00+00:00	1663575000	Mon, 19 Sep 2022 08:10:00 +0000
INSERT INTO prices (price, added, materials_id) VALUES ('233', '1663575000', 1);
INSERT INTO prices (price, added, materials_id) VALUES ('84', '1663575000', 2);
INSERT INTO prices (price, added, materials_id) VALUES ('577', '1663575000', 3);
INSERT INTO prices (price, added, materials_id) VALUES ('278', '1663575000', 4);
INSERT INTO prices (price, added, materials_id) VALUES ('347', '1663575000', 5);
INSERT INTO prices (price, added, materials_id) VALUES ('318', '1663575000', 6);
INSERT INTO prices (price, added, materials_id) VALUES ('96', '1663575000', 7);
INSERT INTO prices (price, added, materials_id) VALUES ('380', '1663575000', 8);
-- 2022-10-07T08:10:00+00:00	1665130200	Fri, 07 Oct 2022 08:10:00 +0000
INSERT INTO prices (price, added, materials_id) VALUES ('219', '1665130200', 1);
INSERT INTO prices (price, added, materials_id) VALUES ('103', '1665130200', 2);
INSERT INTO prices (price, added, materials_id) VALUES ('526', '1665130200', 6);
INSERT INTO prices (price, added, materials_id) VALUES ('263', '1665130200', 7);
INSERT INTO prices (price, added, materials_id) VALUES ('233', '1665130200', 8);
-- 2022-10-12T09:10:00+00:00	1665565800	Wed, 12 Oct 2022 09:10:00 +0000
INSERT INTO prices (price, added, materials_id) VALUES ('184', '1665565800', 3);
INSERT INTO prices (price, added, materials_id) VALUES ('544', '1665565800', 4);
INSERT INTO prices (price, added, materials_id) VALUES ('494', '1665565800', 5);
INSERT INTO prices (price, added, materials_id) VALUES ('403', '1665565800', 6);
INSERT INTO prices (price, added, materials_id) VALUES ('112', '1665565800', 7);
INSERT INTO prices (price, added, materials_id) VALUES ('608', '1665565800', 8);
-- 2022-11-15T08:10:00+00:00	1668499800	Tue, 15 Nov 2022 08:10:00 +0000
INSERT INTO prices (price, added, materials_id) VALUES ('322', '1668499800', 1);
INSERT INTO prices (price, added, materials_id) VALUES ('287', '1668499800', 2);
INSERT INTO prices (price, added, materials_id) VALUES ('251', '1668499800', 3);
INSERT INTO prices (price, added, materials_id) VALUES ('616', '1668499800', 7);
INSERT INTO prices (price, added, materials_id) VALUES ('632', '1668499800', 8);
-- 2022-11-20T08:10:00+00:00	1668931800	Sun, 20 Nov 2022 08:10:00 +0000
INSERT INTO prices (price, added, materials_id) VALUES ('574', '1668931800', 1);
INSERT INTO prices (price, added, materials_id) VALUES ('333', '1668931800', 2);
INSERT INTO prices (price, added, materials_id) VALUES ('431', '1668931800', 3);
INSERT INTO prices (price, added, materials_id) VALUES ('593', '1668931800', 4);
INSERT INTO prices (price, added, materials_id) VALUES ('113', '1668931800', 8);




INSERT INTO collections (weight, received, users_id, materials_id) VALUES ('7.23', '1662336452', '4', '4');
INSERT INTO collections (weight, received, users_id, materials_id) VALUES ('62.35', '1662372550', '5', '3');
INSERT INTO collections (weight, received, users_id, materials_id) VALUES ('41.53', '1662378178', '5', '8');
INSERT INTO collections (weight, received, users_id, materials_id) VALUES ('64.28', '1662373852', '2', '6');
INSERT INTO collections (weight, received, users_id, materials_id) VALUES ('15.19', '1662363478', '3', '6');
INSERT INTO collections (weight, received, users_id, materials_id) VALUES ('27.26', '1662384766', '3', '1');
INSERT INTO collections (weight, received, users_id, materials_id) VALUES ('18.1', '1662372156', '5', '5');
INSERT INTO collections (weight, received, users_id, materials_id) VALUES ('23.56', '1662385293', '5', '7');
INSERT INTO collections (weight, received, users_id, materials_id) VALUES ('32.65', '1663691719', '5', '5');
INSERT INTO collections (weight, received, users_id, materials_id) VALUES ('13.61', '1663611709', '4', '6');
INSERT INTO collections (weight, received, users_id, materials_id) VALUES ('61.15', '1663622063', '2', '6');
INSERT INTO collections (weight, received, users_id, materials_id) VALUES ('46.5', '1663690284', '3', '6');
INSERT INTO collections (weight, received, users_id, materials_id) VALUES ('54.11', '1663645320', '5', '5');
INSERT INTO collections (weight, received, users_id, materials_id) VALUES ('49.47', '1665273748', '4', '4');
INSERT INTO collections (weight, received, users_id, materials_id) VALUES ('5.57', '1665259313', '3', '8');
INSERT INTO collections (weight, received, users_id, materials_id) VALUES ('9.55', '1665259864', '3', '3');
INSERT INTO collections (weight, received, users_id, materials_id) VALUES ('43.9', '1665280383', '2', '2');
INSERT INTO collections (weight, received, users_id, materials_id) VALUES ('4.34', '1665827411', '5', '8');
INSERT INTO collections (weight, received, users_id, materials_id) VALUES ('14.60', '1665814380', '4', '1');
INSERT INTO collections (weight, received, description, users_id, materials_id) VALUES ('25.26', '1665840426', 'Popis ed33ee55-6fce-5b3b-aa28-6fbebdb317be', '4', '5');
INSERT INTO collections (weight, received, description, users_id, materials_id) VALUES ('34.24', '1665821262', 'Popis 549c3362-3eb9-504a-a284-c70d492d9145', '3', '3');
INSERT INTO collections (weight, received, description, users_id, materials_id) VALUES ('1.55', '1665864743', 'Popis 7741eeab-95a5-507a-9c54-751ca186fefb', '3', '1');
INSERT INTO collections (weight, received, description, users_id, materials_id) VALUES ('51.31', '1668790032', 'Popis 92d97c40-5213-5652-806e-378949b2253a', '6', '7');
INSERT INTO collections (weight, received, description, users_id, materials_id) VALUES ('16.25', '1668794112', 'Popis bf824ec3-59f5-5650-a421-c5369709ac1f', '3', '7');
INSERT INTO collections (weight, received, description, users_id, materials_id) VALUES ('51.24', '1668767141', 'Popis cd22dedf-a6f1-5658-8ed4-4ce452ab90e0', '3', '4');
INSERT INTO collections (weight, received, description, users_id, materials_id) VALUES ('28.11', '1668743695', 'Popis cd3ff6f0-ce9d-5bd6-8dea-d3d2df17d3b3', '5', '6');
INSERT INTO collections (weight, received, description, users_id, materials_id) VALUES ('33.34', '1668730031', 'Popis 37eac29a-0471-54a2-9d48-e421dfba992d', '2', '6');
INSERT INTO collections (weight, received, description, users_id, materials_id) VALUES ('60.42', '1668724378', 'Popis 47262876-e576-596c-82cc-008861160e32', '3', '5');
INSERT INTO collections (weight, received, description, users_id, materials_id) VALUES ('13.29', '1668723479', 'Popis 1735bbae-2b41-5c3c-89fa-d65a93026b68', '4', '4');
INSERT INTO collections (weight, received, description, users_id, materials_id) VALUES ('62.25', '1668731294', 'Popis 9c0eab2d-50a0-5701-8d33-db21f693cdc1', '3', '4');
INSERT INTO collections (weight, received, description, users_id, materials_id) VALUES ('34.16', '1669177674', 'Popis 06f89af5-e6e0-5cc7-9e75-3b7657c85ead', '2', '4');
INSERT INTO collections (weight, received, description, users_id, materials_id) VALUES ('47.53', '1669182650', 'Popis 767b5567-4eb5-5e6e-b947-d1baaa180ea2', '2', '1');
INSERT INTO collections (weight, received, description, users_id, materials_id) VALUES ('58.1', '1669148851', 'Popis 231dc65f-1533-5030-9bf6-ca93cf7c095e', '5', '6');
INSERT INTO collections (weight, received, description, users_id, materials_id) VALUES ('14.31', '1669116650', 'Popis fa08332e-3b60-5a81-8f01-3f76af8a3eda', '3', '4');
INSERT INTO collections (weight, received, description, users_id, materials_id) VALUES ('61.60', '1669129398', 'Popis 528615f7-0caa-5606-b35e-0d308f9af05c', '5', '6');
INSERT INTO collections (weight, received, description, users_id, materials_id) VALUES ('13.3', '1669164235', 'Popis f173389f-5f64-5173-9082-3b509e5b1c4b', '3', '6');
INSERT INTO collections (weight, received, description, users_id, materials_id) VALUES ('36.3', '1669110457', 'Popis 7e2c50cb-b95b-5cb1-a7a0-a9f95000935f', '4', '5');
INSERT INTO collections (weight, received, description, users_id, materials_id) VALUES ('4.53', '1669151603', 'Popis 3ee50e11-59cb-5a1b-a9a3-8c3ee59755c7', '6', '3');

--- 2022-09-05T08:10:00+00:00	16623_65400	Mon, 05 Sep 2022 08:10:00 +0000 | nechat prvních 5 číslíc z timestampu 16xxx, zbytek doplnit random short-em
--- 2022-09-20T08:10:00+00:00	16636_61400	Tue, 20 Sep 2022 08:10:00 +0000 | nechat prvních 5 číslíc z timestampu 16xxx, zbytek doplnit random short-em
--- 2022-10-08T08:10:00+00:00	16652_16600	Sat, 08 Oct 2022 08:10:00 +0000 | nechat prvních 5 číslíc z timestampu 16xxx, zbytek doplnit random short-em
--- 2022-10-15T09:10:00+00:00	16658_25000	Sat, 15 Oct 2022 09:10:00 +0000 | nechat prvních 5 číslíc z timestampu 16xxx, zbytek doplnit random short-em
--- 2022-11-18T08:10:00+00:00	16687_59000	Fri, 18 Nov 2022 08:10:00 +0000 | nechat prvních 5 číslíc z timestampu 16xxx, zbytek doplnit random short-em
--- 2022-11-23T08:10:00+00:00	16691_91000	Wed, 23 Nov 2022 08:10:00 +0000 | nechat prvních 5 číslíc z timestampu 16xxx, zbytek doplnit random short-em
