-- Initialize the database.
-- Drop any existing data and create empty tables.

DROP TABLE IF EXISTS url_map;
DROP TABLE IF EXISTS unuse_codes;

CREATE TABLE url_map (
  id INT(20) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  code VARCHAR(10),
  `url` VARCHAR(750) UNIQUE,
  author VARCHAR(30) NOT NULL
);
CREATE TABLE unuse_codes (
  id INT(20) PRIMARY KEY,
  code VARCHAR(10) UNIQUE NOT NULL
);