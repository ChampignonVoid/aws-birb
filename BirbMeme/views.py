from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from BirbMeme.models import MemeCreator, BirbMeme, MemeEvaluation

# Create your views here
def index(request):
    latest_meme_list = BirbMeme.objects.order_by('-creation_date')[:5]
    template = loader.get_template('BirbMeme/index.html')
    context = {
        'latest_meme_list' : latest_meme_list,
        }
    return HttpResponse(template.render(context, request))

def meme_detail(request, meme_id):
    the_meme = BirbMeme.objects.get(id=meme_id)
    meme_evals = MemeEvaluation.objects.filter(meme__id=meme_id)
    template = loader.get_template('BirbMeme/meme.html')
    context = {
        'meme' : the_meme,
        'meme_evals' : meme_evals,
        }
    return HttpResponse(template.render(context, request))

def creator_detail(request, creator_id):
    the_creator = MemeCreator.objects.get(id=creator_id)
    return HttpResponse("You're looking at creator %s. %s" % (creator_id, str(the_creator)))