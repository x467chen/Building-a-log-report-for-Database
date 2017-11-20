# Building-a-log-report-for-Database


### Installation
1.Preparation<br />
Install Python3<br />
Install [Vagrant](https://www.vagrantup.com/) and [VirtualBox](https://www.virtualbox.org/wiki/Download_Old_Builds_5_1).<br />
Download or Clone [fullstack-nanodegree-vm repository]( https://github.com/udacity/fullstack-nanodegree-vm.)<br />
Download the data[here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip).<br />
Find and Copy the newsdata.sql file into your work repo.<br />
To load the data, cd into the vagrant directory and use the command 
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
\d articles
\d author
\d log
```
