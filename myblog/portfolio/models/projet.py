from django.db import models


class Projet(models.Model):
    nom = models.CharField(max_length=50)
    description = models.TextField()
    lien = models.URLField(blank=True, null=True)
    image = models.ImageField(upload_to="projet/apercu", null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated_at = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)


    class Meta:
        pass
    
    def __str__(self):
        return self.nom