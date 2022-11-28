from django.db import models



#como deben ser las bebidas
class Drink(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500)


    #cambiar como se lee en admin
    def __str__(self):
        return self.name + '-' + self.description