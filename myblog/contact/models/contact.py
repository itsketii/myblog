from django.db import models


class Contact(models.Model):
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telephone = models.CharField(max_length=20)
    adresse = models.TextField(null=True)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        pass

    def __str__(self):
        return f"{self.nom} {self.prenom}"