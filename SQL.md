# SQL

* **Entities**, anything about which data can be stored in a database

  * Tables store data that represents on type of entity.

* **Relationships**, relation or links between entities that have something to do with each other

* **Table**, a collection of data in an organized manner in form of rows and columns

* **Field**, the number of columns in a table

* <mark>**JOINS**</mark>, combine rows from two or more tables, based on a related column between them

  <img style="float: left;" src="https://d1jnx9ba8s6j9r.cloudfront.net/blog/wp-content/uploads/2017/11/Joins-SQL-interview-Questions-Edureka.png" width="500"/>

  * **Inner Join**: return all the rows from multiple tables where the join condition is satisfied.
  * **Outer Join**: returns all the records when there is a match in any of the tables, returns all the rows from the left-hand side table and all the rows from the right-hand side table.
  * **Cross Join** vs. **Natural Join**
    * Cross join produces the cross product or Cartesian product of two tables.
    * Natural join is based on all the columns having the same name and data types in both the table.

* **Primary Key**, a column or a set of columns that uniquely identified each row in the table

* **Foreign Key**, maintains referential integrity by enforcing a link between the data in two tables.

* **Constraints**, used to specify the limit on the data type of the table

  * E.g. NOT NULL, CHECK, DEFAULT, UNIQUE, PRIMARY KEY, FOREIGN KEY

* **Subquery**
  * **Correlated subquery**, select the data from a table referenced in the outer query
  * **Non-Correlated subquery**, an independent query where the output of subquery is substituted in the main query
* **Group Functions**
  * AVG, COUNT, MAX, MIN, SUM, VARIANCE

* **HAVING vs. WHERE**
  * HAVING clause can be used only with SELECT statement, usually used in a GROUP BY clause
    * Whenever GROUP BY is not used, HAVING behaves like a WHERE clause
  * WHERE clause is applied to each row before they are a part of the GROUP BY function in a query



* **ACID property: *Atomicity*, *Consistency*, *Isolation*, *Durability***
  * used to ensure that the data transactions are processed reliably in a database system
  * ***Atomicity***, the transactions that are completely done or failed where transation refers to a single logical operation of data.
  * ***Consistency***, ensures that the data must meet all the validation rules. Your transaction never leaves the database without completing its state.
  * ***Isolation***, concurrency control
  * ***Durability***, if a transaction has been committed, it will occur whatever may come in between such as power loss, crash or any sort of error



* **Normalization**, the process of organizing data to avoid duplication and redundancy.
  * better database organization, more tables with smaller rows, efficient data access, ...
  * ***First Normal Form (1NF)***, no repeating groups within rows
  * ***Second Normal Form (2NF)***, every non-key (supporting) column value is dependent on the whole primary key
  * ***Third Normal Form (3NF)***, dependent solely on the primary key and no other non-key (supporting) column value (no transitive functional dependencies)
  * ***Boyce-Codd Nornal Form (BCNF)***, 3NF
    * based on functional dependencies that take into account all candidate keys in a relation
    * A relation is in BCNF, in and only if, every determinant is a Form (BCNF) candidate key.
  * <img style="float: left;" src="https://media.geeksforgeeks.org/wp-content/uploads/20200120023225/Capture323-300x275.png" width="300"/>



* **Trigger**, a special type of stored procedures that are defined to execute automatically in place or after data modifications

* **Data Integrity**
  * Defines the accuracy as well as the consistency of the data stored in a database
  * Defines integrity constraints to enforce business rules on the data when it is entered into an application or a database

* **DELETE vs. TRUNCATE vs. DROP**
  * DELETE command is used to delete a row in a table, and it can be rolled back.
  * TRUNCATE is used to delete all the rows from a table, and it can not be rolled back.
  * DROP command removes a table, and it cannot be rolled back.

* **Case manipulation functions**: LOWER, UPPER, INITCSP

* **Set Operations**

  <img style="float: left;" src="https://d1jnx9ba8s6j9r.cloudfront.net/blog/wp-content/uploads/2019/01/Set-Operations-MySQL-Interview-Questions-Edureka.png" width="700"/>

  * UNION, MINUS, INTERSECT (distinct rows)
  * UNION ALL (include all duplicate rows)



* **View**, a logical snapshot based on a table or another view, used for:
  * restrcting access to data
  * making complex queries simple
  * ensuring data independence
  * providing different views of same data



* **Manipulating Data**, [link](https://www.pluralsight.com/guides/manipulating-data-using-insert-update-delete-sql-server)

  * <u>Inserting Data</u>, insert new records to a table

    ```sql
    INSERT INTO table_name (field1, field2, ...)
    VALUES (value3, value4, ...),
    (value5, value6, ...),
    (value7, value8, ...);
    ```

    ```sql
    INSERT INTO table_name (field1, field2, ...)
    SELECT fieldX, fieldY FROM other_table;
    ```

    ```sql
    INSERT INTO books
    (book_name, book_isbn, book_edition, author_id, publisher_id)
    SELECT 'Kicking in the wall' AS book_name, '9781608681563' AS book_isbn, 1 AS book_edition, a.author_id, p.publisher_id
    FROM authors AS a, publishers p
    WHERE a.author_name = 'Barbara Abercrombie' AND p.publisher_name = 'Harper Collins'; 
    ```

  * <u>Updating Data</u>, change the value of certain fields in one or more rows

    ```sql
    UPDATE table_name
    SET field1 = X, field2 = Y
    WHERE field1 = Z;
    ```

    ```sql
    UPDATE customers
    SET customer_name = 'Jack and Jill Devera', customer_address = '62 Fillmore Ave'
    WHERE customer_name = 'Jill Devera';
    ```

  * <u>Deleting Data</u>, delete records

    ```sql
    DELETE FROM table_name
    WHERE field1 = Z;
    ```

    







* <mark>Working with date</mark>

  * **NOW()**, shows the current date and time of the server

  * **CURRENT_DATE()**, shows only the date of the server

  * **CURRENT_TIME()**, shows only the time of the server

  * **MONTH(), DAY(), YEAR(), WEEK(), WEEKDAY()**, extracts the given data from a date value

  * **HOUR(), MINUTE(), SECOND()**, extracts the given data from a time value

  * **DATEDIFF()**, deteermines the difference between two dates and it is commonly used to calculate age

  * **SUBTIMES(A, B)**, determines the difference between two times

  * **FROMDAYS(INT)**, converts an integer number of days into a date value

  * **TOCHAR() in PostgreSQL = date_format() in MySQL**, converts datetime to string

    ```date_format(t.the_date, '%m-%d-%Y')```

    ```to_char(request_date::date, 'YYYY-MM') AS request_mnth```

* **LIKE vs. REGEXP**

  * LIKE, NOT LIKE, *pattern matching* [link](https://dev.mysql.com/doc/refman/8.0/en/pattern-matching.html)
    * ```_```  matches any single character
    * ```%```  matches an arbitrary number of characters (including zero characters)
  * REGEXP = RLIKE = REGEXP_LIKE(), [link](https://dev.mysql.com/doc/refman/8.0/en/regexp.html#operator_regexp) [examples](https://www.geeksforgeeks.org/mysql-regular-expressions-regexp/)

* **Rounding Functions**, [link](https://www.mssqltips.com/sqlservertip/1589/sql-server-rounding-functions-round-ceiling-and-floor/)

  * **ROUND()**, rounds a positive or negative value to a specific length
  * **CEILING()**
  * **FLOOR()**,  

* Common SQL Functions

  * **CONCAT()**, concatenates two or more string values to create a single string output

  * <mark>**CASE WHEN**</mark>, [link](https://www.w3schools.com/mysql/func_mysql_case.asp)

    * ```mysql
      CASE
        WHEN condition1 THEN result1
        WHEN condition2 THEN result2
        WHEN conditionN THEN resultN
        ELSE result
      END;

  * **FORMAT(X, D)**, formats the number X to D significant digits

* Test **NULL** values
  * NULL value cannot be compared to any other NULL values.
  * IS NULL, IS NOT NULL

#### Index

* **Index**, a performance tuning method of allowing faster retrieval of records from the table.
  * An index creates an entry for each value and hence it will be faster to retrieve data.

* **3 Types of Index: Unique vs. Clustered vs. Non-clustered Index**
  * Unique index: if a primary key is defined, a unique index can be applied automatically.
  * One table can only have one clustered index, but many non-clustered index.
  * Clustered index
    * used for easy retrieval of data from the database, faster read
    * alters the way records are stored in a database as it sorts out rows by the column which is set to be clustered index
  * Non-clustered index
    * slower read
    * does not alter the way it was stored but it creates a separate object within a table which points back to the original table rows after searching



#### <mark>Window Functions</mark>

* 4 Types of Window Functions in SQL

  * ***Regular Aggregate Functions***, e.g. AVG, MIN/MAX, COUNT, SUM

    * [Avg() function example, PostgreSQL](https://platform.stratascratch.com/coding-question?id=10302&python=)

    * Answer 1: 

      ```sql
      SELECT u.request_date, u.distance_to_travel / u.monetary_cost AS dist_to_cost, u2.avg_dist_to_cost
      FROM uber_request_logs u, 
        (SELECT EXTRACT(YEAR FROM request_date) AS year, EXTRACT(MONTH FROM request_date) AS month, AVG(distance_to_travel / monetary_cost) AS avg_dist_to_cost
      FROM uber_request_logs
      GROUP BY EXTRACT(YEAR FROM request_date), EXTRACT(MONTH FROM request_date)) u2
      WHERE EXTRACT(YEAR FROM u.request_date) = u2.year AND EXTRACT(MONTH FROM u.request_date) = u2.month
      ORDER BY u.request_date
      ```

    * Answer 2:

      ```sql
      SELECT u.request_date, u.dist_to_cost, 
      	AVG(u.dist_to_cost) OVER (PARTITION BY u.request_mnth) AS avg_dist_to_cost
      FROM (SELECT request_date, to_char(request_date, 'YYYY-MM') AS request_mnth,
          distance_to_travel / monetary_cost AS dist_to_cost
          FROM uber_request_logs) u
      ORDER BY u.request_date
      ```

  * ***Ranking Functions***, e.g. ROW_NUMBER, RANK, DENSE_RANK [link](https://codingsight.com/similarities-and-differences-among-rank-dense_rank-and-row_number-functions/)

    * extremely useful to generate ranking indexes within groups

    * When combined with a PARTITION BY clause, all of these functions reset the returned integer value to 1 as we have seen.

    * If there are no duplicated values in the column used by the ORDER BY clause, these functions return the same output.

    * **RANK**, retrieves ranked rows based on the condition of the ORDER BY clause

      * tie: skip the next positions before incrementing the counter

    * **DENSE_RANK**, similar to RANK

      * tie: no skips

    * **ROW_NUMBER**, returns the row number of the sorted records starting with 1

      * tie: assign values 1 and 2 to without taking the fact that they are equal into account

      <img style="float: left;" src="https://codingsight.com/wp-content/uploads/2018/08/RankD_pic8.png" width="500"/>

    * [Rank() fucntion example, PostgreSQL](https://platform.stratascratch.com/coding/9898-unique-salaries?python=), find the Top N distinct xx values by xx

      * <u><mark>Regarding tie: DENSE_RANK + DISTINCT = RANK with DISTINCT data</mark></u>
      * Answer 1:

      ```sql
      SELECT *
      FROM (SELECT DISTINCT department, salary, DENSE_RANK() OVER (PARTITION BY department ORDER BY salary DESC) AS rank_id 
      FROM twitter_employee
      ORDER BY department, salary desc) t
      WHERE rank_id <= 3
      ```

      * Answer 2:

      ```sql
      SELECT *
      FROM (SELECT t1.department, t1.salary, rank() OVER (PARTITION BY t1.department ORDER BY t1.salary DESC) AS rank_id
      FROM (SELECT DISTINCT department, salary FROM twitter_employee) t1
      ORDER BY department, rank_id) t
      WHERE rank_id <= 3
      ```

  * ***Generating Statistics***, e.g. NTILE (percentiles, quartiles, medians)

    * can be used for the entire dataset or by group, useful for data analysts, business analysts, and data scientist

    * NTILE function takes an argument of the number of bins (or basically how many buckets you want to split your data into), and then creates this number of bins by dividing your data into that many number of bins. You set how the data is ordered and partitioned, if you want additional groupings.

    * **NTILE()**, distribute rows of an ordered partition into a specified number of buckets, [link](https://www.sqlservertutorial.net/sql-server-window-functions/sql-server-ntile-function/)

      ```sql
      NTILE(buckets) OVER (
          [PARTITION BY partition_expression, ... ]
          ORDER BY sort_expression [ASC | DESC], ...
      )
      ```

    * **PERCENTILE_CONT()**, calculates a percentile based on a continuous distribution of the column value, [link](https://docs.microsoft.com/en-us/sql/t-sql/functions/percentile-cont-transact-sql?view=sql-server-ver15)

      ```sql
      PERCENTILE_CONT ( numeric_literal )   
          WITHIN GROUP ( ORDER BY order_by_expression [ ASC | DESC ] )  
          OVER ( [ <partition_by_clause> ] )
      ```

    * [NTILE(100) example, PostgreSQL](https://platform.stratascratch.com/coding/10303-top-percentile-fraud?python=)

      * <mark><u>PERCENTILE_CONT() + GROUP BY + cutoff = NTILE(100) + cutoff</u></mark>
      * Answer 1: find the cutoff, then filter

      ```sql
      SELECT policy_num, f1.state, claim_cost, fraud_score 
      FROM fraud_score f1, 
      	(SELECT state, 
         PERCENTILE_CONT(0.05) within GROUP (ORDER BY fraud_score DESC) AS cutoff 		FROM fraud_score 
        GROUP BY state) f2
      WHERE fraud_score >= cutoff AND f1.state = f2.state
      ```

      * Answer 2: add percentile as a seperate field, then filter

      ```sql
      SELECT policy_num, state, claim_cost, fraud_score
      FROM
        (SELECT *, NTILE(100) OVER (PARTITION BY state
                                ORDER BY fraud_score DESC) AS percentile
         FROM fraud_score) a
      WHERE percentile <= 5
      ```

  * ***Handling Time Series Data***, e.g. LAG, LEAD (positional functions), [link](https://learnsql.com/blog/lead-and-lag-functions-in-sql/)

    * used to calculate trends like a month-over-month rolling average or a growth metric

    * **LAG()**, allows access to a value stored in a different row above the current row, the row above may be adjacent or some number of rows above, as sorted by a specified column or set of columns

      ```sql
      LAG(expression [, offset[, default_value]]) 
      	OVER ([ <partition_by_clause> ] ORDER BY columns)
      -- offset: the number of rows to skip
      -- default_value: NULL by default, can specify if offset is specified
      ```

    * **LEAD()**, similar to LAG(), allows access to a value below

      ```sql
      LEAD(expression [, offset[, default_value]]) 
      	OVER ([ <partition_by_clause> ] ORDER BY columns)
      ```

    * [Lag() Example](https://platform.stratascratch.com/coding-question?id=9637&python=)

      * <mark>CAST(  AS numeric) can handle NULL exceptions</mark>

      * Answer 1: create a lookup table for yearly stats, then populate the growth ratio table

        ```sql
        SELECT reg_year, num_host_reg, 
        	LAG(num_host_reg) OVER (order by reg_year) AS prev_num_host_reg, 
        	100 * (num_host_reg - LAG(num_host_reg) OVER (order by reg_year)) / LAG(num_host_reg) OVER (order by reg_year) AS growth_rate
        FROM (
          SELECT COUNT(*) AS num_host_reg, EXTRACT(year FROM host_since) as reg_year
          FROM airbnb_search_details
          GROUP BY EXTRACT(year FROM host_since)
          ORDER BY reg_year) a
        ORDER BY reg_year
        ```

      * Answer 2: first group by year, then calculate yearly stats, and finally populate the growth ratio table

        ```sql
        SELECT year, current_year_host, prev_year_host,
               ROUND(((current_year_host - prev_year_host)
               /(CAST(prev_year_host AS numeric)))*100) estimated_growth
        FROM
          (SELECT year,
                  current_year_host,
                  LAG(current_year_host, 1) OVER (ORDER BY year)
                  AS prev_year_host
           FROM
             (SELECT extract(year
                             FROM host_since::date) AS year,
                     count(id) current_year_host
              FROM airbnb_search_details
              WHERE host_since IS NOT NULL
              GROUP BY extract(year
                               FROM host_since::date)
              ORDER BY year) t1) t2
        ```

    

__Checklist__

- [ ] More on index
- [ ] DBMS



__Reference__

[Top 65 SQL Interview Questions You Must Prepare in 2021](https://www.edureka.co/blog/interview-questions/sql-interview-questions#joinsinsql)

[Top 50 MySQL Questions You Must Prepare in 2021](https://www.edureka.co/blog/interview-questions/mysql-interview-questions/)

[Top 40 Best MySQL Interview Questions And Answers (2021 Questions)](https://www.softwaretestinghelp.com/mysql-interview-questions/)

[Top 50 MySQL Interview Questions & Answers (2021 Update)](https://career.guru99.com/top-50-mysql-interview-questions-answers/)

[10 Top Data Mart Interview Questions](https://srinimf.com/2016/12/07/top-10-best-informatica-absolutely-new-questions-for-freshers/)





**[Types of Window Functions in SQL and Questions Asked by Airbnb, Netflix, Twitter, and Uber](https://www.stratascratch.com/blog/types-of-window-functions-in-sql-and-questions-asked-by-airbnb-netflix-twitter-and-uber/), *with example questions and answers***

**[Top 10 SQL Window Functions Interview Questions](https://learnsql.com/blog/sql-window-functions-interview-questions/)**

[SQL Window Functions Cheat Sheet](https://learnsql.com/blog/sql-window-functions-cheat-sheet/)



[StrateScratch](https://www.stratascratch.com), practice Python/SQL questions, coding + non-coding
