from django.db import models

# Create your models here.

class UserDetails(models.Model):
    name = models.CharField(max_length =  20)
    username =  models.CharField(max_length =  20)
    email =  models.CharField(max_length =  50)
    password = models.CharField(max_length = 20)


class Meta:
    db_table = 'todo_db'

class TaskList(models.Model):
    title = models.CharField(max_length = 20)
    description = models.CharField(max_length = 200)
    due_date = models.DateField()

    class Meta:
        db_table = 'tasklist_db'