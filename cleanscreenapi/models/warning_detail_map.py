from django.db import models
from .warning_detail import WarningDetail

class WarningDetailsMap(models.Model):
    warning = models.ForeignKey(Warning, on_delete=models.CASCADE, related_name='warning_details_maps')
    detail = models.ForeignKey(WarningDetail, on_delete=models.CASCADE, related_name='warning_details_maps')

    class Meta:
        unique_together = ('warning', 'detail')

    def __str__(self):
        return f'{self.detail.name} for {self.warning.tag}'
