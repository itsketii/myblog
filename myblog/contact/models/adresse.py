from django.db import models


class Adresse(models.Model):
    pays = models.CharField(max_length=100)
    ville = models.CharField(max_length=100)
    quartier = models.CharField(max_length=100)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        pass

    def __str__(self):
        return f"{self.ville} - {self.pays}"