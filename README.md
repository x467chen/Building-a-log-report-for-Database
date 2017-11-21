# Building-a-log-report-for-Database
## Synopsis
Building a reporting tool depending on the logs in database. Use information from the database to discover bunch of question such as what kind of articles the site's readers like.

## Installation
1.Preparation<br />
Install Python3<br />
Install [Vagrant](https://www.vagrantup.com/) and [VirtualBox](https://www.virtualbox.org/wiki/Download_Old_Builds_5_1).<br />
Download or Clone [fullstack-nanodegree-vm repository]( https://github.com/udacity/fullstack-nanodegree-vm.)<br />
Download the data[here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip).<br />
Find and Copy the newsdata.sql file into your work repo.<br />
To load the data, cd into the vagrant directory and use the cmd: 
``` xml
psql -d news -f newsdata.sql
```
2.Explore the Database:<br />
Looking at the schema for Database
``` xml
\dt
```
Looking at the schema for each tables
``` xml
\d articles
\d author
\d log
```
Looking inside each table
``` xml
select * from articles limit 2;
select * from authors limit 2;
select * from log limit 2;
```
3.Create View:<br />
create view views (title, number of view)
``` xml
CREATE VIEW views
AS SELECT articles.title, count(*) as view
FROM articles join log
on log.path LIKE CONCAT('/article/', articles.slug) 
GROUP BY articles.title
ORDER BY num desc;
```
create view bestAuthor (authorID, number of view)
``` xml
CREATE VIEW bestAuthor
AS SELECT articles.author, count(*) as num
FROM articles join log
on log.path LIKE CONCAT('/article/', articles.slug) 
GROUP BY articles.id
ORDER BY num desc;
```
#create view requestLog(date, requesttime)
``` xml
CREATE VIEW requestLog
AS SELECT date(log.time) AS date, count(*) as requestTime
FROM log
Group by date;
```
create view errorLog(date, errortime)
``` xml
CREATE VIEW errorLog
AS SELECT date(log.time) AS date, count(*) as errorTime
FROM log
WHERE log.status != '200 OK'
GROUP BY date;
```
create view TotalLog(date, errortime, requesttime)
``` xml
CREATE VIEW TotalLog
AS SELECT errorLog.date, errortime, requesttime
FROM requestLog, errorLog
WHERE requestLog.date=errorLog.date;
```
