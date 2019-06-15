from django.urls import path, include

from .views import index, creator_detail, BirbMemeList, BirbMemeDetail, SignUp

urlpatterns = [
    path('', index, name='index'),
    path('memes/', BirbMemeList.as_view(), name='memes'),
    path('memes/<int:meme_id>/', BirbMemeDetail.as_view(), name='meme_detail'),
    path('creators/<int:creator_id>/', creator_detail, name='creator_detail'),
    path('accounts/signUp/', SignUp.as_view(), name='account_sign_up')
]
