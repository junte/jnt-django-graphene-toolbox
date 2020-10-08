from django.db import models


class OrderTestModel(models.Model):
    """Model for testing ordering."""

    due_date = models.DateField(null=True, blank=True)
