from django.db import models

# Create your models here.

class Topic(models.Model):

    """A topic that user is learning about"""
    text = models.CharField(max_length = 200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):

        """Reaturn a string representation of the model."""
        return self.text


class Entry(models.Model):

    """Something specific learned about topic"""

    topic = models.ForeignKey('Topic', on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)


    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        if len(self.text) < 50:
            return self.text
        else:
            return self.text[:50] + "..."
