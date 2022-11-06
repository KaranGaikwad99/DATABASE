## DATABASES:
# https://www.programiz.com/sql/online-compiler/
# https://www.youtube.com/watch?v=1dWCqjhvF58

## Change in Table Structure
/* alter table Customers add column description int(64); */
/* alter table Customers rename column description to details; */
/* alter table Customers drop column details; */
/* alter table Customers modify column details char(20); */

# /-

## Tbl clear 
/* truncate table Orders; */
/* drop table Orders; */
# /-

## CRUD Operations
create table Orders(
    order_id int not null,
    description varchar(20),
    status boolean,
    primary key(order_id)
);

insert into Orders(order_id, description, status) values(6,'nokia',1);

update Customers set country='CANADA' where first_name='Raaaviii';

delete from Orders where order_id in (3); 
# /- 

## WHERE clause and Comparison Operator ([and, or, not,]  [>, <, =,] !(not), [>=, <=, ==])
select * from Customers where age > 25 or age=25; --> anyone True 
select * from Customers where age > 25 and age=25; --> both True else False
select * from Customers where not age > 25; --> (NOT) show below 25 records
select * from Customers where age != 25; --> (NOT) all records rather than 25 only

## Logical Operator ( [between, like, null, is null, in, disctinct] )
select * from Customers where age between 20 and 25;   --> between <> and <> 
select * from Customers where last_name like 'r%';   --> like '<string>' / '<character>%'
select * from Customers where country is null;  --> all null records only in country column
select * from Customers where age is not null; --> only not null records
select * from Customers where country in ('UK', 'USA');   --> perticular values in ()
select distinct(age) from Customers;  --> disctinct(<columnName>) ## Unique Values

## Aggregations Operator ([avg, min, max, sum, count])   --> It works on Numerical Values.
select avg(amount) from Orders where salary between 10000 and 20000; # where condition on only numerical value
select min(amount) from Orders;
select max(amount) from Orders;
select sum(amount) from Orders;
select count() from Orders; # count(*)

## SQL Group Clause ([group by]) :- with respect to table.
# arrange identical data into groups
select first_name, max(salary), department from Orders group by department;
# group by with [having clause] 
select first_name, avg(salary), dept from Orders group by dept having count(dept)>1;  ## count of dept >1 ## having <condition of (group by value)> 
select first_name, avg(salary), dept from Orders group by dept having sum(customer_id) > 5;
                                    //-------------------------//--- <avg,sum,min,max,count>() <condition> ;
    
# order by 
select * from Orders order by custumer_id asc;  // desc;

## UNION , UNION ALL
select product_name from Prodcut1
union
select product_name from Product2;   ## --> union remove duplicates and combine

select prod_name from Product1
union all 
select prod_name from Product2;      ## --> union all keeps duplicates and combine

### JOINS ([ 1.INNER Join, 2.LEFT Join, 3.Right Join, 4.Self Outer Join, 5.Cross Join // Cartetian Join ])

# 1. INNER Join --------> both table common records
select c.first_name, c.age, c.country, o.amount,o.item
from Customers c
inner join Orders o
on c.customer_id=o.customer_id; -- # (on <common_fields> = <common_fields>)

# 2. LEFT Join --------> left table all rec and right where my matched found
select c.first_name, c.age, o.amount, o.item
from Customers c
left join Orders o
on c.customer_id=o.customer_id;  

# 3. Right Join --------> Right table all rec and right where my matched found
select c.first_name, c.age, o.amount, o.item
from Customer c
right join Orders o
on c.customer_id = o.customer_id;

# 4. Self Outer Join --------> Left and Right Union
select c.first_name, o.amount
from Customers c
left join Orders o
on c.customer_id = o.customer_id

union

select c.first_name, o.amount
from Customers c
right join Orders o
on o.customer_id = c.customer_id;

# 5. Cross Join // Cartetian Join -------->  A=[a, b, c] B=[1,2,3,4] Cross= [(a,1)(a,2)(a,3)(a,4),(b,1),(b,2),....] Total 12 rec 
select * from Customers cross join Orders;

########  //-------------Done

