#Levi Duke

#This file determines the routes of where the user will go
from .views import indexPageView
from django.urls import path
from .views import individualpersonPageView
from .views import missingpersonstablePageView
from .views import displayPersonPageView



urlpatterns = [  
    path("<int:id>/", displayPersonPageView, 
name="displayPerson"), 
    path("missingpersonstable/", missingpersonstablePageView, name="mptable"), 
    path("<str:oPerson>/", individualpersonPageView, name="individualperson"), 
    path("", indexPageView, name="index"),
] 

urlpatterns = [
    path("",indexPageView, name="index"),
    path("missingpersonstable/", missingpersonstablePageView, name="mptable"  ),
    path("individualperson/", individualpersonPageView, name = "individualperson"),
]
