from django.contrib import admin
from BirbMeme.models import BirbMeme, MemeCreator, MemeEvaluation

# Register your models here.

admin.site.register(BirbMeme)
admin.site.register(MemeCreator)
admin.site.register(MemeEvaluation)
