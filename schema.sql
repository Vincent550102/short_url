-- Initialize the database.
-- Drop any existing data and create empty tables.

-- DROP TABLE IF EXISTS `url_map`;
-- DROP TABLE IF EXISTS `unuse_codes`;

CREATE TABLE IF NOT EXISTS url_map (
  id INT(20) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  code VARCHAR(10) UNIQUE NOT NULL,
  `url` VARCHAR(750) NOT NULL,
  author VARCHAR(30) NOT NULL,
  clicked INT(20) NOT NULL
);
CREATE TABLE IF NOT EXISTS unuse_codes (
  id INT(20) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  code VARCHAR(10) NOT NULL
);