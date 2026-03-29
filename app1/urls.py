from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home,name='home'),
    path('saveform/',views.save_form,name='saveform'),
    # path('savefile/',views.save_file,name='savefile'),
    path('contact/',views.Contact,name='contact'),
    path("courses/<int:id>",views.courses),   # ID get karne ka liya 
    path("abhay/<str:data>",views.abhay)  ,    # Str  data get karn ka liya
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)   # imges upload k liya