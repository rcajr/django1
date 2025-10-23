from django.db import models

class User(models.Model):
    name = models.CharField('nome', max_length= 20)
    lastname = models.CharField('sobrenome', max_length= 20)
    user = models.CharField('usuario', max_length= 20)
    password = models.CharField('senha', max_length= 255)

    def __str__(self):
        return f'{self.name} {self.lastname}'

class Expense(models.Model):
    description = models.CharField('descrição', max_length= 255)
    value = models.DecimalField('valor', max_digits=8, decimal_places=2)
    parcel = models.IntegerField('parcela')
    firstParcelDate = models.DateField('data da primeira parcela')

    def __str__(self):
        return f'{self.description}'



