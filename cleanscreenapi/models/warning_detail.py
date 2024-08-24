from django.db import models

class WarningDetail(models.Model):
    name = models.CharField(max_length=50)
    tag = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.name} ({self.tag})'