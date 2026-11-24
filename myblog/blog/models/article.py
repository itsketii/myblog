from django.db import models
from .categorie import Categorie
from .tag import Tag



class Article(models.Model):
    categorie = models.ForeignKey(
        Categorie,
        on_delete=models.CASCADE,
        related_name="articles",
    )
    tags = models.ManyToManyField(Tag)
    titre = models.CharField(max_length=50)
    contenu = models.TextField()
    image = models.ImageField(upload_to="articles/cover", null=True)
    date_publication = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated_at = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        pass

    def __str__(self):
        return self.titre