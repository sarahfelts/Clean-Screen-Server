from django.db import models
from .warning import Warning
from .tag import Tag

class WarningTag(models.Model):
    warning = models.ForeignKey(Warning, on_delete=models.CASCADE, related_name='warning_tags')
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, related_name='warning_tags')

    class Meta:
        unique_together = ('warning', 'tag')

    def __str__(self):
        return f'{self.tag.name} for {self.warning.tag}'
