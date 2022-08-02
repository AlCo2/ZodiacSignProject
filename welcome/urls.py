from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.welcome, name='welcome'),
    path('scorpio/',views.scorpio, name='scorpio'),
    path('aries/',views.aries, name='aries'),
    path('Taurus/',views.tau, name='taurus'),
    path('gemini/',views.gemini, name='gemini'),
    path('leo/',views.leo, name='leo'),
    path('cancer/',views.cancer, name='cancer'),
    path('Aquarius/',views.aqua, name='aqua'),
    path('Pisces/',views.pisces, name='pisces'),
    path('Capricorn/',views.capr, name='capri'),
    path('virgo/',views.virgo, name='virgo'),
    path('libra/',views.libra, name='libra'),
    path('Sagittarius/',views.sag, name='sag'),
    path('co2/',views.aboutme, name='co2'),   
]
