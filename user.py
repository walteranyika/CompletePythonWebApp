from peewee import *

db=PostgresqlDatabase('complete',user='postgres',host='localhost',password='lydia@2010')

class User(Model):
    names = CharField()
    email =CharField(unique=True)
    password=CharField()
    class Meta:
        db_table="users"
        database=db

User.create_table(fail_silently=True)
