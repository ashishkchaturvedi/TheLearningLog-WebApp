from django.db import models

# Create your models here.

class Pizza(models.Model):

    """A pizza that user is trying to create"""
    text = models.CharField(max_length = 200)
    
    def __str__(self):

        """Return a strikng representation of the model"""
        return self.text


class Topping(models.Model):

    pizza = models.ForeignKey('Pizza', on_delete=models.CASCADE)
    name = models.TextField()

    class Meta:
        verbose_name_plural = 'toppings'

    def __str__(self):
        
        """Return the string representation of the model"""
        return self.name
