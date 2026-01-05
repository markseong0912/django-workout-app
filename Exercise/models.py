from django.db import models

class Exercise(models.Model):
    name = models.CharField(max_length=100)
    image_url = models.URLField(blank=True)
    description = models.TextField()
    muscles_targeted = models.CharField(max_length=100)
    difficulty = models.CharField(max_length=50)
    equipment = models.CharField(max_length=100)


    def __str__(self):
        return self.name
