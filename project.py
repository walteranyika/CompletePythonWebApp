from peewee import *

db=PostgresqlDatabase('complete',user='postgres',host='localhost',password='lydia@2010')

class Project(Model):
    title = CharField()
    client =CharField()
    start_date=DateField()
    end_date=DateField()
    desc =TextField()
    status=BooleanField(default=False)
    user_id = IntegerField()
    class Meta:
        table_name="projects"
        database=db

Project.create_table(fail_silently=True)
