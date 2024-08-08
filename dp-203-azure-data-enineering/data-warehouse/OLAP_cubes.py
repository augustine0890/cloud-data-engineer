#!/usr/bin/env python
# coding: utf-8

"""
Exercise 02 - OLAP Cubes - Solution

All the database tables in this demo are based on public database samples and transformations:
- `Sakila` is a sample database created by `MySql` [Link](https://dev.mysql.com/doc/sakila/en/sakila-structure.html)
- The PostgreSQL version of it is called `Pagila` [Link](https://github.com/devrimgunduz/pagila)
- The facts and dimension tables design is based on O'Reilly's public dimensional modelling tutorial schema [Link](http://archive.oreilly.com/oreillyschool/courses/dba3/index.html)
"""

import psycopg2
import pandas as pd

def create_database():
    import subprocess
    subprocess.run(['createdb', '-h', '127.0.0.1', '-U', 'student', 'pagila_star'], check=True)
    subprocess.run(['psql', '-q', '-h', '127.0.0.1', '-U', 'student', '-d', 'pagila_star', '-f', 'Data/pagila-star.sql'], check=True)

def get_connection():
    conn_string = "postgresql://student:student@127.0.0.1:5432/pagila_star"
    return psycopg2.connect(conn_string)

def run_query(query):
    with get_connection() as conn:
        df = pd.read_sql_query(query, conn)
        return df

def main():
    # Uncomment these lines if you need to create and load the database
    # create_database()

    queries = {
        "simple_cube": """
            SELECT dimDate.day, dimMovie.rating, dimCustomer.city, SUM(sales_amount) AS revenue
            FROM factSales
            JOIN dimMovie ON (dimMovie.movie_key = factSales.movie_key)
            JOIN dimDate ON (dimDate.date_key = factSales.date_key)
            JOIN dimCustomer ON (dimCustomer.customer_key = factSales.customer_key)
            GROUP BY CUBE(dimDate.day, dimMovie.rating, dimCustomer.city)
            ORDER BY revenue DESC
            LIMIT 20;
        """,
        "slicing": """
            SELECT dimDate.day, dimMovie.rating, dimCustomer.city, SUM(sales_amount) AS revenue
            FROM factSales
            JOIN dimMovie ON (dimMovie.movie_key = factSales.movie_key)
            JOIN dimDate ON (dimDate.date_key = factSales.date_key)
            JOIN dimCustomer ON (dimCustomer.customer_key = factSales.customer_key)
            WHERE dimMovie.rating = 'PG-13'
            GROUP BY dimDate.day, dimCustomer.city, dimMovie.rating
            ORDER BY revenue DESC
            LIMIT 20;
        """,
        "dicing": """
            SELECT dimDate.day, dimMovie.rating, dimCustomer.city, SUM(sales_amount) AS revenue
            FROM factSales
            JOIN dimMovie ON (dimMovie.movie_key = factSales.movie_key)
            JOIN dimDate ON (dimDate.date_key = factSales.date_key)
            JOIN dimCustomer ON (dimCustomer.customer_key = factSales.customer_key)
            WHERE dimMovie.rating IN ('PG-13', 'PG')
            AND dimCustomer.city IN ('Bellevue', 'Lancaster')
            AND dimDate.day IN ('1', '15', '30')
            GROUP BY dimDate.day, dimCustomer.city, dimMovie.rating
            ORDER BY revenue DESC
            LIMIT 20;
        """,
        "roll_up": """
            SELECT dimDate.day, dimMovie.rating, dimCustomer.country, SUM(sales_amount) AS revenue
            FROM factSales
            JOIN dimMovie ON (dimMovie.movie_key = factSales.movie_key)
            JOIN dimDate ON (dimDate.date_key = factSales.date_key)
            JOIN dimCustomer ON (dimCustomer.customer_key = factSales.customer_key)
            GROUP BY dimDate.day, dimMovie.rating, dimCustomer.country
            ORDER BY revenue DESC
            LIMIT 20;
        """,
        "drill_down": """
            SELECT dimDate.day, dimMovie.rating, dimCustomer.district, SUM(sales_amount) AS revenue
            FROM factSales
            JOIN dimMovie ON (dimMovie.movie_key = factSales.movie_key)
            JOIN dimDate ON (dimDate.date_key = factSales.date_key)
            JOIN dimCustomer ON (dimCustomer.customer_key = factSales.customer_key)
            GROUP BY dimDate.day, dimCustomer.district, dimMovie.rating
            ORDER BY revenue DESC
            LIMIT 20;
        """,
        "grouping_sets": """
            SELECT dimDate.month, dimStore.country, SUM(sales_amount) AS revenue
            FROM factSales
            JOIN dimDate ON (dimDate.date_key = factSales.date_key)
            JOIN dimStore ON (dimStore.store_key = factSales.store_key)
            GROUP BY GROUPING SETS ((), dimDate.month, dimStore.country, (dimDate.month, dimStore.country))
            ORDER BY revenue DESC;
        """,
        "cube": """
            SELECT dimDate.month, dimStore.country, SUM(sales_amount) AS revenue
            FROM factSales
            JOIN dimDate ON (dimDate.date_key = factSales.date_key)
            JOIN dimStore ON (dimStore.store_key = factSales.store_key)
            GROUP BY CUBE(dimDate.month, dimStore.country)
            ORDER BY revenue DESC;
        """
    }

    for query_name, query in queries.items():
        print(f"Running query: {query_name}")
        df = run_query(query)
        print(df.head(20))

if __name__ == "__main__":
    main()
