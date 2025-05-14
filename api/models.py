import uuid
from django.db import models


class TimeStampedModel(models.Model):
    creation_date = models.DateTimeField(auto_now_add=True)
    modification_date = models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True

class Hospital(TimeStampedModel):
    hospital_uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    registration_number = models.CharField(max_length=255)
    address = models.TextField()
    city = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=20)
    contact_number = models.CharField(max_length=20)
    contact_email = models.EmailField()
    is_active = models.BooleanField(default=True)\

    def __str__(self):
        return self.name
