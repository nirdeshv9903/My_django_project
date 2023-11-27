from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=122)
    phone_number = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    date_of_birth = models.CharField(max_length=122)
    Address = models.CharField(max_length=122)
    second_add = models.CharField(max_length=122)

    def __str__(self):
        return self.name