from django.urls import path, include
from User import views


urlpatterns = [
    path('', views.show_posts, name='show_posts'),
    path('add-post/', views.add_post, name='add_post'),

    # authentication urls
    path('login/', views.login_method, name='login'),
    path('logout/', views.logout_method, name='logout'),
    path('username/', views.available_username, name='available_username'),
    path('signup/', views.signup, name='signup'),
    
]
