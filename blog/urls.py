from django.urls import path
from .views import index, post_list, post_detail, register, user_login, user_logout, like_post, subscribe, unsubscribe, forgot_password, reset_password, ckeditor_upload, post_search, categoris_post

urlpatterns = [
    path("post_search/", post_search, name="post_search"),
    path("upload/", ckeditor_upload, name="custom_upload_file"),
    path('', index, name="index"),
    path('register/', register, name='register'), 
    path('login/', user_login, name='login'),
    path('forgot_password/', forgot_password, name='forgot_password'),
    path('reset/<uidb64>/<token>/', reset_password, name='reset_password'),
    path('logout/', user_logout, name='logout'),
    path('like_post/', like_post, name='like_post'),
    path('subscribe/', subscribe, name='subscribe'),
    path('unsubscribe/', unsubscribe, name='unsubscribe'),
    path('ckeditor/upload/', ckeditor_upload, name='ckeditor_5_upload_file'),
    path('category/<str:category_name>/', categoris_post, name='categoris_post'),
    path("<slug:slug>/", post_detail, name="post_detail"),
]
