from django.db import models


class AuditData(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True # Ensures this model is not turned into a database table but can be inherited by others


class Products(AuditData):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(decimal_places=2, max_digits=5)
    is_available = models.BooleanField(default=False)
    