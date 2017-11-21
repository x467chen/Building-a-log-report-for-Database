#!/usr/bin/python
# A Log Analysis for a newspaper site database.
# Create all the views in your DB before running the programs
import psycopg2
import datetime
DBNAME = "news"


def get_logAnalysis(query):
    """Return corresponding log analysis from the 'database'
       depends on the order requirement."""
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute(query)
    logAnalysis = c.fetchall()
    db.close()
    return logAnalysis

# def print_result(input):
#   """Encapsulation the print function"""
#   for element in input:
#     print('"' + element[0] + '"'' -- ' + str(element[1]) + " views")
#   print("#########################################################")


if __name__ == '__main__':
    # 1. What are the most popular three articles of all time?
    print("TOP Three Article:")
    query1 = "select * from views"
    mostPopularArticle = get_logAnalysis(query1)
    # printArticle=print_result(mostPopularArticle);
    for article in mostPopularArticle:
        print('"' + article[0] +
              '"'' -- ' + str(article[1]) + " views")
    print("#########################################################")

    # 2. Who are the most popular article authors of all time?
    print("Most Popular authors:")
    query2 = """SELECT authors.name, sum(bestAuthor.num) as view
            FROM authors join bestAuthor
            on authors.id=bestAuthor.author
            Group by authors.name
            ORDER BY view desc
            LIMIT 4;"""
    mostPopularAuthor = get_logAnalysis(query2)
    # printAuthor=print_result(mostPopularAuthor);
    for author in mostPopularAuthor:
        print(author[0] + ' -- ' + str(author[1]) + " views")
    print("#########################################################")

    # 3. On which days did more than 1% of requests lead to errors?
    print("Days more than 1% of requests lead to errors:")
    query3 = """SELECT date,
                (CAST(errortime AS float)/CAST(requesttime AS float)*100)
                as ErrorPercent
            FROM TotalLog
            WHERE (CAST(errortime AS float)/
                    CAST(requesttime AS float)*100)>1;"""
    errorPercent = get_logAnalysis(query3)
    # printErrorInfo=print_result(errorPercent);
    for info in errorPercent:
        print(info[0].strftime('%b %d,%Y') +
              ' -- ' + str(round(info[1], 2)) + " errors")
    print("#########################################################")
