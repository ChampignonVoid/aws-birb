import datetime

from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model


# Create your models here.

from django.contrib.auth.models import AbstractUser


class BirbUser(AbstractUser):
    def number_of_creation(self):
        return BirbMeme.objects.filter(creator=self.id).count()


class BirbMeme(models.Model):
    meme_image = models.ImageField(upload_to='birb_meme')
    description = models.TextField()
    creation_date = models.DateField(auto_now_add=True)
    creator = models.ForeignKey(get_user_model(),
                                on_delete=models.CASCADE)

class MemeEvaluation(models.Model):
    EVALUATION_MARK = [(x, x) for x in range(0, 11)]
    meme_eval = models.PositiveIntegerField(choices=EVALUATION_MARK, default=0)
    meme = models.ForeignKey(BirbMeme, on_delete=models.CASCADE)
    creator = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
