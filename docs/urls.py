from django.conf.urls import url
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Birbmeme API')

urlpatterns = [
    url('docs/', schema_view)
]