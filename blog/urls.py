from django.urls import path
from .views import index, post_list, post_detail, register, user_login, user_logout, like_post, subscribe, unsubscribe, forgot_password, reset_password


urlpatterns = [
    path('', index, name="index"),
    path('register/', register, name='register'), 
    path('login/', user_login, name='login'),
    path('forgot_password/', forgot_password, name='forgot_password'),
    path('reset/<uidb64>/<token>/', reset_password, name='reset_password'),
    path('logout/', user_logout, name='logout'),
    path('like_post/', like_post, name='like_post'),
    path('subscribe/', subscribe, name='subscribe'),
    path('unsubscribe/', unsubscribe, name='unsubscribe'),
    path("<slug:slug>/", post_detail, name="post_detail"),
]
