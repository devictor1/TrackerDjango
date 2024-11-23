from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    completed = models.BooleanField(default=False)
    horario = models.TimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)

    def _str_(self):
        return self.title