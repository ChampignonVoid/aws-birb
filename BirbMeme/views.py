from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.template import loader
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response

from django.contrib.auth.decorators import login_required


from .serializers import BirbMemeSerializer

from BirbMeme.models import BirbUser, BirbMeme, MemeEvaluation

# Create your views here
def index(request):
    return redirect('memes/')

def creator_detail(request, creator_id):
    the_creator = BirbUser.objects.get(id=creator_id)
    return HttpResponse("You're looking at creator %s. %s" % (creator_id, str(the_creator)))

### API View ###

class BirbMemeList(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "BirbMeme/index.html"

    def get(self, request):
        queryset = BirbMeme.objects.order_by('-creation_date')[:5]
        return Response({'latest_meme_list': queryset})

    @login_required(login_url='/')
    def post(self, request):
        serializer = BirbMemeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return redirect('/')
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BirbMemeDetail(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "BirbMeme/meme.html"

    def get(self, request, meme_id):
        the_meme = get_object_or_404(BirbMeme, pk=meme_id)
        meme_evals = MemeEvaluation.objects.filter(meme__id=meme_id)
        return Response({'meme': the_meme, 'meme_evals': meme_evals})