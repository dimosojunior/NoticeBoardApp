from . import views
from django.urls import path

urlpatterns = [
	

    path('signup/', views.user_create_view.as_view(), name="user_create_view"),

    
    

    
]