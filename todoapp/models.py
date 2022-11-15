from django.db import models

# Create your models here.
class List(models.Model):
  name = models.CharField(max_length=50, unique=True, blank=False, null=False)
  password = models.CharField(max_length=50, blank=False, null=False)
  
  def __str__(self):
    return self.name
  
class Task(models.Model):
  list = models.ForeignKey(List, on_delete=models.CASCADE)
  task_name = models.CharField(max_length=50, blank=False, null=False)
  important = models.BooleanField(default=False)
  done = models.BooleanField(default = False)
  
  def __str__(self):
    return self.task_name