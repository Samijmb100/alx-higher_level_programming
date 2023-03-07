#Holberton School - 0x0C-SQL_introduction Introduction to SQL
Setup

    Install sql sudo apt-get install mysql-server-5.5
    Connect to your MySQL server
    ~> mysql -hlocalhost -uroot -p
    mysql> quit
    Bye

New commands / functions used:

mysql> help, DDL, DML, CREATE, ALTER, SELECT, INSERT, UPDATE, DELETE
Helpful Links

    Youtube primer on MySQL
    Basic MySQL tutorial
    Basic SQL Statements: DDL and DML
    Basic SQL Queries: SQL and RA
    SQL Technique: functions
    SQL Technique: subqueries
    Resource for SQL information: dev.mysql.com

Description of Files
0-list_databases.sql
Script that lists all databases of a MySQL server
1-create_database_if_missing.sql
Script that creates a database hbtn_0c_0 in the MySQL server
2-remove_database.sql
Deletes the database hbtn_0c_0 from the server. Should not fail if it doesn't exist.
3-list_tables.sql
Lists all tables of a database
4-first_table.sql
Creates a table called first_table in the database hbtn_0c_0
5-full_table.sql
Creates the full description of the table first_table in the hbtn_0c_0
6-list_values.sql
Lists all rows of the table first_table in the database hbtn_0c_0
7-insert_value.sql
Inserts a new row in the table first_table in the database hbtn_0c_0
8-count_89.sql
Displays the number of records with the ``id = 89`` in the table ``first_table`` in the database hbtn_0c_0
9-full_creation.sql
Creates a table second_table in the database hbtn_0c_0 and adds multiple rows
10-top_score.sql
Lists all records of the table second_table in the database hbtn_0c_0
11-best_score.sql
Lists all records with a score >= 10 in the table second table in the database hbtn_0c_0
12-no_cheating.sql
Updates the score of Bob to 10
13-change_class.sql
Removes all records with a score <= 5 in the table second_table in the database hbtn_0c_0
14-average.sql
Computes the average score of all records in the table second_table in the database hbtn_0c_0
15-groups.sql
Lists the number of records with the same score in the table second_table in the database hbtn_0c_0
16-no_link.sql
Lists all records of the table second_table in the database hbtn_0c_0
100-move_to_utf8.sql
Converts the table first_table field, name in hbtn_0c_0 database to UTF8 (utf8mb4, collate utf8mb4_unicode_ci)
101-avg_temperatures.sql
Import this [table dump](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/272/temperatures.sql) into the database hbtn_0c_0 and write a script that displays the average temperature by city, ordered by temperature, descending.
102-top_city.sql
Imports this [table dump](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-hig her-level_programming+/272/temperatures.sql) into the database hbtn_0c_0 and displays the top 3 city temperatures during July and August, ordered by temperature, descending.
103-max_state.sql
Imports this [table dump](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-hig her-level_programming+/272/temperatures.sql) into the database hbtn_0c_0 and displays the max temperature of each state. 

