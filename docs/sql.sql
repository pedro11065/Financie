/*To so anotando uns codigos SQL, ignore*/


/*

Table_users: user_id(UUID), user_fullname, user_email, user_password, user_birthday

Table_companies: company_id(UUID), user_id(table_users), company_name, company_email, company_cnpj, company_password)

table_user_companies: company_id(table_companies), user_id(table_users), user_access_level


table_log_all: log_time, log_description

*/

INSERT INTO table_users (id, fullname, email, password, birthday, cpf)
VALUES ('838b818c-5995-43e0-be05-bb5b89364efa','Pedro Henrique SIlva Quixabeira', 'pedrohenriquesilvaquixabeira@gmail.com','Pedro12504.','13/03/2006', '50774811803');

CREATE TABLE table_users 
(id UUID primary key, /*UUID*/
fullname varchar(255), 
email varchar(255) unique, 
password varchar(225), 
birthday varchar(10),
cpf varchar(11) unique);



CREATE TABLE table_companies 
(company_id UUID primary key, /*UUID*/
user_id UUID REFERENCES table_users(user_id), /*Faz a relação com o user_id na outra tabela. Está ai para indicar quem registrou a empresa*/
company_name varchar(255),
company_email varchar(255) unique, 
company_cnpj varchar(14) unique,
company_password varchar(225));

CREATE TYPE access_level AS ENUM ('viewer', 'checker', 'editor','creator'); /*Cria um tipo de registro chamado acess_level que só permite essas 3 opções, servindo como verificação no banco de dados*/

CREATE TABLE table_user_companies /*Só mandar o nivel de acesso do usuário ('viewer', 'checker', 'editor')*/
(company_id UUID REFERENCES table_companies(company_id), 
user_id UUID REFERENCES table_users(user_id),
user_access_level access_level); /*Faz a relação com o user_id na outra tabela. Está ai para indicar quem registrou a empresa*/

CREATE TABLE table_log_all /*Não é necessario enviar que horas são, já commita sozinho a data, só mandar a descrição*/
(log_time TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
log_description varchar(255));

CREATE TABLE table_assets
(asset_id UUID primary key,
company_id UUID REFERENCES table_companies(company_id),
user_id UUID REFERENCES table_users(user_id), 
name varchar(100), 
event varchar(50),
class varchar(50),
value double precision,
location varchar (100),
acquisition_date date, /*formato = xx-xx-xxxx*/ 
Description varchar (255),
status varchar(100),
creation_date DATE DEFAULT CURRENT_DATE,
creation_time TIME DEFAULT CURRENT_TIME);

CREATE TABLE table_liabilities
(liability_id UUID primary key,
company_id UUID REFERENCES table_companies(company_id),
user_id UUID REFERENCES table_users(user_id), 
name varchar(100), 
event varchar(50),
class varchar(50),
value double precision,
credit double precision,
debit double precision,
emission_date date, /*formato = xx-xx-xxxx*/ 
expiration_date date, /*formato = xx-xx-xxxx*/ 
payment_method varchar (50),
description varchar (255),
status varchar(100),
creation_date DATE DEFAULT CURRENT_DATE,
creation_time TIME DEFAULT CURRENT_TIME);

CREATE TABLE table_historic
(historic_id UUID primary key,
company_id UUID REFERENCES table_companies(company_id),
user_id UUID REFERENCES table_users(user_id),
patrimony_id UUID,
name varchar(100), 
event varchar(50),
class varchar(50),
value double precision,
credit double precision,
debit double precision,
date varchar(10),
type varchar(25),
creation_date DATE DEFAULT CURRENT_DATE,
creation_time TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP AT TIME ZONE 'America/Sao_Paulo'
);





