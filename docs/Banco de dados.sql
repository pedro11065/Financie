/*To so anotando uns codigos SQL, ignore*/


/*

Table_users: user_id(UUID), user_fullname, user_email, user_password, user_birthday

Table_companies: company_id(UUID), user_id(table_users), company_name, company_email, company_cnpj, company_password)

table_user_companies: company_id(table_companies), user_id(table_users), user_access_level


table_log_all: log_time, log_description

*/
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


