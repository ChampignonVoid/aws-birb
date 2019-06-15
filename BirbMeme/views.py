from django.shortcuts import get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.decorators import api_view, renderer_classes

from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from .serializers import BirbMemeSerializer, SignUpSerializer, MemeEvalSerializer
from .schemas import SignUpSchema, BirbMemeSchema
from BirbMeme.models import BirbUser, BirbMeme, MemeEvaluation

from rest_framework_swagger.renderers import OpenAPIRenderer, SwaggerUIRenderer

def redirectToIndex():
    """
    The main page of this API will be the memes' list
    """
    return HttpResponseRedirect(reverse('memes'))

def index(request):
    return redirectToIndex()


@api_view(['GET'])
@renderer_classes([OpenAPIRenderer, SwaggerUIRenderer])
def creator_detail(request, creator_id):
    """
    Get the user\'s details
    """
    the_creator = BirbUser.objects.get(id=creator_id)
    return HttpResponse("You're looking at creator %s. %s" % (creator_id,
                                                              str(the_creator)))

@api_view(['POST'])
@renderer_classes([OpenAPIRenderer, SwaggerUIRenderer])
def meme_eval(request, meme_id):
    """
    Evaluate a meme
    """
    meme = BirbMeme.objects.get(pk=meme_id)
    if not request.user.is_authenticated:
        return redirect('login')
    try:
        MemeEvaluation.objects.get(meme=meme, creator=request.user)
        MemeEvaluation.objects.create(meme_eval=int(request.data.get('eval')),
                                      meme=meme,
                                      creator=request.user)
    except MemeEvaluation.DoesNotExist:
        pass
    return HttpResponseRedirect(reverse('meme_detail',
                                        kwargs={ 'meme_id': meme_id }))

class BirbMemeList(APIView):
    renderer_classes = [
        TemplateHTMLRenderer,
        OpenAPIRenderer,
        SwaggerUIRenderer
    ]
    template_name = "BirbMeme/index.html"
    
    def get(self, request):
        """
        Display the last 25 memes
        """
        serializer = BirbMemeSerializer()
        queryset = BirbMeme.objects.order_by('-id')[:25]

        return Response({'latest_meme_list': queryset, 'serializer': serializer})

    def post(self, request):
        """
        Create a new meme
        """
        if not request.user.is_authenticated:
            return redirect('login')
        serializer = BirbMemeSerializer(data=request.data)
        
        if serializer.is_valid():
            BirbMeme.objects.create(meme_image=request.data.get('meme_image'),
                                    description=request.data.get('description'),
                                    creator=request.user)
            return redirectToIndex()

        return Response({'serializer': serializer})


class BirbMemeDetail(APIView):
    renderer_classes = [
        TemplateHTMLRenderer,
        OpenAPIRenderer,
        SwaggerUIRenderer
    ]
    template_name = "BirbMeme/meme.html"
    schema = BirbMemeSchema()

    def get(self, request, meme_id):
        """
        Get a meme by its id
        """
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
        """
        Get the form in order to SignUp
        """
        if request.user.is_authenticated:
            return redirectToIndex()
        serializer = SignUpSerializer()
        return Response({'title': 'SignUp', 'serializer': serializer})

    def post(self, request):
        """
        Create a new user and automatically login
        """
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
