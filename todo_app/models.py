from django.db import models

class Task_Table(models.Model):
    title = models.CharField(max_length=52)
    status = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
