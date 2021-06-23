-- Initialize the database.
-- Drop any existing data and create empty tables.

DROP TABLE IF EXISTS url_map;
DROP TABLE IF EXISTS unuse_codes;


CREATE TABLE url_map (
  id INT(20) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  author VARCHAR(30) NOT NULL,
  origin_url UNIQUE VARCHAR(2000),
  code VARCHAR(10),
);
CREATE TABLE unuse_codes (
  id INT(20) PRIMARY KEY,
  code UNIQUE VARCHAR(10) NOT NULL,
);