from django.db import models


class WaitlistEntry(models.Model):
    email = models.EmailField(unique=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
