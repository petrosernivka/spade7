from django.db import models

class Gamer (models.Model):
    login = models.CharField(max_length=20)
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.login