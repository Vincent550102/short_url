DROP TABLE IF EXISTS url_map;
DROP TABLE IF EXISTS codes;
CREATE TABLE url_map (
  id bigint NOT NULL AUTO_INCREMENT,
  author varchar(255) NOT NULL,
  origin_url varchar(2083),
  code varchar(10),
  PRIMARY KEY (id)
);
CREATE TABLE codes (
  id bigint NOT NULL,
  code varchar(10) NOT NULL,
  PRIMARY KEY (id)
);