from django.db import models

# Create your models here.
from django.db.models import CharField, DateTimeField, ForeignKey, CASCADE, BigAutoField


class Movie(models.Model):
    id = BigAutoField(primary_key=True)
    name = CharField(max_length=500, unique=True, db_index=True)
    release_date = DateTimeField(null=True, blank=True)
    created_at = DateTimeField(auto_now_add=True)


class Theatre(models.Model):
    id = BigAutoField(primary_key=True)
    name = CharField(max_length=200, unique=True, db_index=True)
    created_at = DateTimeField(auto_now_add=True)


class Screen(models.Model):
    id = BigAutoField(primary_key=True)
    name = CharField(max_length=50)
    theatre = ForeignKey(to=Theatre, on_delete=CASCADE)
    created_at = DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('name', 'theatre',)

    def __str__(self):
        return f"{self.id} - {self.name} <-> {self.theatre.id} - {self.theatre.name}"


class Show(models .Model):
    id = BigAutoField(primary_key=True)
    screen = ForeignKey(to=Screen, on_delete=CASCADE)
    movie = ForeignKey(to=Movie, on_delete=CASCADE)
    start = DateTimeField()
    end = DateTimeField()
    created_at = DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('screen', 'movie', 'start',)


