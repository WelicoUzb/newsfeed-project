from django.urls import path
from .views import Home , View , Contact , Error , Uzbekistan , World , Economy , Technology , Sport

urlpatterns = [
    path('' , Home.as_view(), name="home"),
    path('new/<int:pk>/',View , name="view" ),
    path('contact/' , Contact.as_view() , name = "contact"),
    path('404/', Error , name="error"),
    path('uzbekistan/' , Uzbekistan.as_view() , name='uzbekistan_page'),
    path('world/' , World.as_view() , name='world_page'),
    path('economy/' , Economy.as_view() , name='economy_page'),
    path('technology/' , Technology.as_view() , name='technology_page'),
    path('sport/' , Sport.as_view() , name='sport_page'),
]
