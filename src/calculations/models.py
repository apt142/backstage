from django.db import models


class DifferenceRequestLog(models.Model):
    requested_number = models.IntegerField(db_index=True)
    calculated_value = models.IntegerField()
    requested_at = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
