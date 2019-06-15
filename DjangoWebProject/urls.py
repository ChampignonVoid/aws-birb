"""
Definition of urls for DjangoWebProject.
"""

from datetime import datetime
from django.conf.urls import url
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
import django.contrib.auth.views

# Uncomment the next lines to enable the admin:
# from django.conf.urls import include
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = [
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:    
    path('api/v1/', include('BirbMeme.urls')),
    path('api/v1/admin/', admin.site.urls),
    path('api/v1/accounts/', include('django.contrib.auth.urls')),
    path('api/v1/', include('docs.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
