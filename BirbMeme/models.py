import datetime

from django.db import models
from django.utils import timezone

# Create your models here.

from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass

class MemeCreator(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    creation_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return 'Name : ' + self.name + ', Mail : ' + self.email

    def number_of_creation(self):
        return BirbMeme.objects.filter(creator=self.id).count()

class BirbMeme(models.Model):
    meme_image = models.ImageField(upload_to='birb_meme')
    description = models.TextField()
    creation_date = models.DateField(auto_now_add=True)
    creator = models.ForeignKey(MemeCreator, on_delete=models.CASCADE)

    def __str__(self):
        return 'Created by : ' + self.creator.name + ', Description : ' + self.description

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class MemeEvaluation(models.Model):
    EVALUATION_MARK = [(x, x) for x in range(0, 11)]
    meme_eval = models.PositiveIntegerField(choices=EVALUATION_MARK, default=0)
    meme = models.ForeignKey(BirbMeme, on_delete=models.CASCADE)
    creator = models.ForeignKey(MemeCreator, on_delete=models.CASCADE)

    def __str__(self):
        return 'Evaluation of ' + self.creator.name + ' : ' + str(self.meme_eval) + '/10'