from django.shortcuts import get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.decorators import api_view, renderer_classes

from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from .serializers import BirbMemeSerializer, SignUpSerializer
from .schemas import SignUpSchema
from BirbMeme.models import BirbUser, BirbMeme, MemeEvaluation

from rest_framework_swagger.renderers import OpenAPIRenderer, SwaggerUIRenderer

def redirectToIndex():
    return HttpResponseRedirect(reverse('memes'))

def index(request):
    return HttpResponseRedirect(reverse('memes'))


@api_view(['GET'])
@renderer_classes([OpenAPIRenderer, SwaggerUIRenderer])
def creator_detail(request, creator_id):
    """
    Get the user\'s details
    """
    the_creator = BirbUser.objects.get(id=creator_id)
    return HttpResponse("You're looking at creator %s. %s" % (creator_id,
                                                              str(the_creator)))


class BirbMemeList(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "BirbMeme/index.html"
    
    def get(self, request):
        serializer = BirbMemeSerializer()
        queryset = BirbMeme.objects.order_by('-creation_date')[:5]

        return Response({'latest_meme_list': queryset, 'serializer': serializer})

    def post(self, request):
        serializer = BirbMemeSerializer(data=request.data)
        
        if serializer.is_valid():
            BirbMeme.objects.create(meme_image=request.data.get('meme_image'),
                                    description=request.data.get('description'),
                                    creator=request.user)
            return redirectToIndex()

        return Response({'serializer': serializer})


class BirbMemeDetail(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "BirbMeme/meme.html"

    def get(self, request, meme_id):
        the_meme = get_object_or_404(BirbMeme, pk=meme_id)
        meme_evals = MemeEvaluation.objects.filter(meme__id=meme_id)
        return Response({'meme': the_meme, 'meme_evals': meme_evals})


class SignUp(APIView):
    renderer_classes = [
        TemplateHTMLRenderer,
        OpenAPIRenderer,
        SwaggerUIRenderer
    ]
    template_name = "BirbMeme/sign_up.html"
    schema = SignUpSchema()

    def get(self, request):
        if request.user.is_authenticated:
            return redirectToIndex()
        serializer = SignUpSerializer()
        return Response({'title': 'SignUp', 'serializer': serializer})

    def post(self, request):
        if request.user.is_authenticated:
            return redirectToIndex()

        serializer = SignUpSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({'title': 'SignUp', 'serializer': serializer})
        username = request.data.get('username')
        first_name = request.data.get('first_name')
        last_name = request.data.get('last_name')
        email = request.data.get('email')
        password = request.data.get('password')
        user = BirbUser.objects.create_user(username=username,
                                            first_name=first_name,
                                            last_name=last_name,
                                            email=email,
                                            password=password)
        login(request, user)
        return redirectToIndex()
