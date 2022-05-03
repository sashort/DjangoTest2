from django.db import models

# Create your models here.

class TaskItem(models.Model):
    user_pk = models.IntegerField()
    index = models.IntegerField()
    description = models.CharField(max_length = 500)
    complete = models.BooleanField()
    
    def __str__(self):
        return self.name