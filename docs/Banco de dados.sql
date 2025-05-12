
CREATE TABLE users 
(id UUID primary key, /*UUID*/
fullname varchar(150), 
email varchar(150) unique, 
password varchar(60), 
birthday varchar(10),
cpf BYTEA unique,
phone BYTEA unique,
lgpd_consent boolean default false,
created_at timestamp,
updated_at timestamp ,
deleted_at timestamp) ;


