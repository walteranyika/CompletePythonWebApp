from peewee import *

db=MySQLDatabase('complete',user='postgres',host='localhost',password='lydia@2010')

class Project(Model):
    title = CharField()
    client =CharField()
    start_date=DateField()
    end_date=DateField()
    desc =TextField()
    status=BooleanField(default=False)
    class Meta:
        db_table="projects"
        database=db

Project.create_table(fail_silently=True)
