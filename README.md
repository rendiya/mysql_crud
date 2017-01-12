testing db with class like orm

for using
```
query = Query()
print query.select(table_name="hello",table_column="No",table_filter="1")
```

this is inheritance class in db.connect, so you dont make new connection if you want to connect mysql

you can use standart query with :

```
query = Query()
print query.query("SELECT VERSION()")
```