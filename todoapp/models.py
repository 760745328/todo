from django.db import models
from datetime import date

# Create your models here.
class TODO(models.Model):
    things = models.CharField(max_length=20, verbose_name='待办事项')
    done = models.BooleanField(default=False, verbose_name='已完成')


    def __str__(self):
        return self.things
    class Meta():
        db_table = 'todoapp'
class Student(models.Model):
    number = models.IntegerField()
    name = models.CharField(max_length=10, null=False)
    apartment = models.TextField()
    birthdy = models.DateField(default=date.today)

