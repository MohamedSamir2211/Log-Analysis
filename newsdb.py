import psycopg2

# Connect to the database using connect function
conn = psycopg2.connect("dbname=news")
db = conn.cursor()


def get_popular_three_articles():
    """Return most popular three articles."""
    query = '''Select title,views from articles,reports
               where articles.slug = reports.slug
               order by views desc limit 3;'''
    db.execute(query)
    return db.fetchall()


def get_most_popular_article_authors():
    """Return most popular article authors."""
    query = '''Select name,SUM(views) as views from
               authors,articles,reports where
               articles.author = authors.id And
               articles.slug = reports.slug group by
               name order by views desc;'''
    db.execute(query)
    return db.fetchall()


def get_day_with_more_request_errors():
    """ Return the day with more request errors """
    query = '''Select to_char(time,'YYYY-MON-DD') as day,round((count(case when status
             like '404%' then 1 else Null End)::numeric/
             count(*)::numeric)*100,2)
             as error_precentage from log group by day
             order by error_precentage desc limit 1;'''
    db.execute(query)
    return db.fetchall()


print('Top Three Articles in all time:')
for data in get_popular_three_articles():
    print(str(data[0]), str(data[1])+" views") # data[0] => represent title coulmn , data[1] => represent views coulmn

print("\n")

print("most popular article authors:")
for data in get_most_popular_article_authors():
    print(str(data[0]), str(data[1]) + " views") # data[0] => represent name coulmn , data[1] => represent Sum of views coulmn

print("\n")

print("day with more errors")
for data in get_day_with_more_request_errors():
    print(str(data[0]), str(data[1]) + " % errors") # data[0] => represent day , data[1] => represent precentage of error


    conn.close()
