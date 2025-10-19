from django.db import models

# Create your models here.
from django.db import models

class Client(models.Model):
    name = models.CharField(max_length=100)
    cash = models.FloatField(default=0)
    hawa = models.FloatField(default=0)
    note = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
