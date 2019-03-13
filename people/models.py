from django.db import models

class House(models.Model):
    name = models.CharField(max_length = 30)

    def __str__(self):
        return self.name

class Person(models.Model):
    name = models.CharField(max_length = 30)
    house = models.ForeignKey(House, on_delete = models.CASCADE)
    def __str__(self):
        return self.name

class Pet(models.Model):
    name = models.CharField(max_length = 30)
    owner = models.ManyToManyField(Person)

    def __str__(self):
        return self.name
