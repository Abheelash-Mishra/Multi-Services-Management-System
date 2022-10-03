# Multi-Services Management System

This is a database-type project which has Python as its front-end and MySQL as the back-end.

The main highlight of this project is that the MySQL query that needs to be run is built "on the go" as per the search requirements of the user. For example, if the user wants to search for a caterer with a "4 star" rating or enter a specific location, the code will automatically build the MySQL query as per the requirement!

Let us take this as the input.

```
caterers in chennai
```

The resultant query would end up being as follows.

```
select * from caterers where location = chennai
```


You can search specifically search for these parameters!

- Ratings
- Location
- Type of Service
