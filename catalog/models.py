from django.db import models
from django.urls import reverse


class Style(models.Model):
    style = models.CharField(max_length=200,
                             help_text="Enter a style of beer (Pale Lager and Pilsner, Dark Lager, German Bock, Brown Ale, Pale Ale, India Pale Ale, Porter, Stout, Belgian-Style Ale, Wheat Beer, Wild & Sour Ale, Specialty Beer)")

    def __str__(self):
        return self.style


class Category(models.Model):
    category = models.CharField(max_length=200, help_text="Enter a category of beer (...)")

    def __str__(self):
        return self.category


class Beer(models.Model):
    name = models.CharField(max_length=200)
    style = models.ManyToManyField(Style, help_text="Select a style of beer")
    category = models.ManyToManyField(Category, help_text="Select a category of beer")
    volume = models.FloatField(max_length=100)
    producer = models.ForeignKey('Producer', on_delete=models.SET_NULL, null=True)
    photo_path = models.TextField(max_length=1000, null=True)
    fact = models.TextField(max_length=1000, null=True)
    score = models.FloatField(max_length=5.0, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('catalog:beer-detail', args=[str(self.id)])


class Producer(models.Model):
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    brewer = models.CharField(max_length=100)

    def get_absolute_url(self):
        return reverse('catalog:producer-detail', args=[str(self.id)])

    def __str__(self):
        return '%s, %s' % (self.country, self.city)
