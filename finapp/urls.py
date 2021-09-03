from django.urls import include, path
from . import views
from django.conf import settings 
from django.conf.urls.static import static 

urlpatterns = [

		path('', views.index, name='index'),
		path('balance-sheet', views.balance, name='balance-sheet'),

]
