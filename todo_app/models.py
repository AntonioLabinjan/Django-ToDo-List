# definiranje klase task...imamo tipove podataka koji imaju određene parametre
from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    # identifikacija po title-u I guess
    def __str__(self):
        return self.title
