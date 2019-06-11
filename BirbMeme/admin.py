from django.contrib import admin
from BirbMeme.models import BirbMeme, MemeCreator, MemeEvaluation
from django.contrib.auth.admin import UserAdmin
from .models import User

# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.register(BirbMeme)
admin.site.register(MemeCreator)
admin.site.register(MemeEvaluation)
