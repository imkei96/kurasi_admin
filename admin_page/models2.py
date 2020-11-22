from django.db import models
from django.urls import reverse  # Used to generate URLs by reversing the URL patterns

from . import neodb as neo


# Create your models here.
class Kategori(models.Model):
    category = models.CharField(max_length=200)

    class Meta:
        ordering = ['category']

    def __str__(self):
        """String for representing the Model object."""
        return self.category

    def get_absolute_url(self):
        """Returns the url to access a detail record for this book."""
        return reverse('link-detail', args=[str(self.category)])


class Kelas(models.Model):
    LIST_KELAS = (
        ('1', 'SD Kelas 1'),
        ('2', 'SD Kelas 2'),
        ('3', 'SD Kelas 3'),
        ('4', 'SD Kelas 4'),
    )
    kelas = models.CharField(max_length=200, choices=LIST_KELAS, default='1', help_text="Kelas")

    class Meta:
        ordering = ['kelas']

    def __str__(self):
        return self.kelas


class Pelajaran(models.Model):
    pelajaran = models.CharField(max_length=200, help_text="Pelajaran")

    class Meta:
        ordering = ['pelajaran']

    def __str__(self):
        return self.pelajaran


class Data(models.Model):
    """Model representing a specific copy of a book (i.e. that can be borrowed from the library)."""
    user = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    judul = models.CharField(max_length=200, default='DEFAULT')
    kelas = models.ForeignKey(Kelas, on_delete=models.SET_NULL, null=True)
    pelajaran = models.ForeignKey(Pelajaran, on_delete=models.SET_NULL, null=True)
    kategori = models.ManyToManyField(Kategori)
    link = models.TextField(max_length=1000, default='DEFAULT')

    class Meta:
        ordering = ['user']

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.judul} {self.kelas} {self.pelajaran}'

    def get_absolute_url(self):
        """Returns the url to access a detail record for this book."""
        return reverse('data-detail', args=[str(self.id)])

person = neo.Person.nodes.all()
for p in person:
    print(p)