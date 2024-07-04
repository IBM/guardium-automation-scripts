drop database if exists demo_db;
create database demo_db;
use demo_db;
create table if not exists testTable (text varchar(100), id int);
insert into testTable (text) values ('xxx');
insert into testTable (text) values ('yyy');
insert into testTable (id) values (5);
