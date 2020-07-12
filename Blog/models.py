from django.db import models

# Create your models here.

class Python(models.Model):
    heading = models.TextField(max_length=2000)
    code = models.TextField(max_length=200000)
    image = models.ImageField(null=True)

    def __str__(self):
        return self.heading


class Java(models.Model):
    heading = models.TextField(max_length=2000)
    code = models.TextField(max_length=200000)

    def __str__(self):
        return self.heading


class Csharp(models.Model):
    heading = models.TextField(max_length=2000)
    code = models.TextField(max_length=200000)

    def __str__(self):
        return self.heading


class Html(models.Model):
    heading = models.TextField(max_length=2000)
    code = models.TextField(max_length=200000)

    def __str__(self):
        return self.heading
