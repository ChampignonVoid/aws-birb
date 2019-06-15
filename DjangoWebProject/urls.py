"""
Definition of urls for DjangoWebProject.
"""

from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

# Uncomment the next lines to enable the admin:
# from django.conf.urls import include
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = [
    path('api/v1/', include('BirbMeme.urls')),
    path('api/v1/admin/', admin.site.urls),
    path('api/v1/accounts/', include('django.contrib.auth.urls')),
    path('api/v1/', include('docs.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
