#!/usr/bin/env python
import psycopg2

# Connect to the database using connect function
conn = psycopg2.connect("dbname=news")
db = conn.cursor()


def execute_query(query):
    """Function To Execute Different Queries """
    db.execute(query)
    return db.fetchall()


query1 = '''Select title,views from articles,reports
               where articles.slug = reports.slug
               order by views desc limit 3;'''

query2 = '''Select name,SUM(views) as views from
               authors,articles,reports where
               articles.author = authors.id And
               articles.slug = reports.slug group by
               name order by views desc; '''

query3 = '''Select to_char(time,'YYYY-MON-DD') as day,round((count(case when status
             like '404%' then 1 else Null End)::numeric/
             count(*)::numeric)*100,2)
             as error_percentage from log group by day
             order by error_percentage desc limit 1; '''


print('What are the most popular three articles of all time ?')
for data in execute_query(query1):
    print str(data[0]), " ---- ", str(data[1]), " views"
    # data[0] => represent title column , data[1] => represent views column

print("\n")

print("Who are the most popular article authors of all time ?")
for data in execute_query(query2):
    print str(data[0]), " ---- ", str(data[1]), " views"
    # data[0] => represent name column , data[1] => represent Sum of views column

print("\n")

print("On which days did more than 1% of requests lead to errors ?")
for data in execute_query(query3):
    print str(data[0]), " ---- ", str(data[1]), "% errors"
    # data[0] => represent day , data[1] => represent percentage of error

conn.close()
