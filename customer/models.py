from django.db import models

# Create your models here.

class Customer(models.Model):
    firstname = models.CharField('Name', max_length=50)
    lastname = models.CharField('Lastname',max_length=50)
    age = models.IntegerField('Age')
    profession = models.TextField('Profession')

    def __str__(self):
        return self.firstname


    def get_absolute_url(self):
        return f'/customer/{self.id}'


    class Meta:
        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'