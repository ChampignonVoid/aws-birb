from django.contrib import admin
from BirbMeme.models import BirbMeme, MemeEvaluation
from django.contrib.auth.admin import UserAdmin
from .models import BirbUser

# Register your models here.
admin.site.register(BirbUser, UserAdmin)
admin.site.register(BirbMeme)
admin.site.register(MemeEvaluation)
