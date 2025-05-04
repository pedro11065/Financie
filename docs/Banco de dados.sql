/*To so anotando uns codigos SQL, ignore*/


/*

Table_users: user_id(UUID), user_fullname, user_email, user_password, user_birthday

Table_companies: company_id(UUID), user_id(table_users), company_name, company_email, company_cnpj, company_password)

table_user_companies: company_id(table_companies), user_id(table_users), user_access_level


table_log_all: log_time, log_description

*/
CREATE TABLE users 
(id UUID primary key, /*UUID*/
fullname varchar(255), 
email varchar(255) unique, 
password varchar(225), 
birthday varchar(10),
cpf varchar(11) unique);


