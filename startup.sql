CREATE DATABASE IF NOT EXISTS startupsupport ;
USE  startupsupport;


CREATE TABLE IF NOT EXISTS startup_login (
username varchar(59)  NOT NULL,
password varchar(255)  NOT NULL,
PRIMARY KEY(username)
);


CREATE TABLE IF NOT EXISTS startupdetails (
id int(11) NOT NULL AUTO_INCREMENT primary key,
username varchar(59) NOT NULL ,
comp_name varchar(59)  NOT NULL,
address varchar(255) ,
company_email varchar(100) NOT NULL,
phone int(11) NOT NULL,
product_desc varchar(255) NOT NULL,
contact_person_email varchar(100) NOT NULL,
Support_needed varchar(100) NOT NULL,
Website varchar(100) ,
FOREIGN KEY (username) REFERENCES startup_login(username)
);





desc startup_login;
desc startupdetails;