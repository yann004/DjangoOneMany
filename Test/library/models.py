from django.db import models

GENRE_CHOICES = (
    ('H', 'Homme'),
    ('F', 'Femme'),
)
STATUTS_CHOICES = (
    ('M', 'Marie'),
    ('S', 'Single'),
)

class Author(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    genre = models.CharField(max_length=1, choices=GENRE_CHOICES) 
    statut = models.CharField(max_length=1, choices=STATUTS_CHOICES)
    origine = models.CharField(max_length=100)


    def __str__(self):
        return self.name

class Book(models.Model):

    title = models.CharField(max_length=100)
    nbre_exemplaire = models.IntegerField()
    published_date = models.DateField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    # D'autres champs d'information sur le livre

    def __str__(self):
        return self.title
