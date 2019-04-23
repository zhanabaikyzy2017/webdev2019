from django.db import models
from datetime import datetime

class TaskList(models.Model):
    name = models.CharField(max_length = 255)

    def __str__(self):
        return self.name
    def to_json(self):
        return{
            'id' : self.id,
            'name':self.name
        }

class Task(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    due_on = models.DateTimeField()
    status = models.CharField(max_length=255)
    task_list = models.ForeignKey(TaskList,on_delete=models.CASCADE)

    def __str__(self):
        return '{}:{}'.format(self.name, self.created_at)

    def to_json(self):
        return {
            'id':self.id,
            'name':self.name,
            'created_at':self.created_at,
            'status':self.status
        }