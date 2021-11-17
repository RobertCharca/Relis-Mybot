from django.urls import path
from . import views
from authentication import views
urlpatterns = [
    path('relis/', views.relis_page, name="relis"),
    path('login/', views.loginStudent, name="login"),
    path('logout/', views.logoutStudent, name="logout"),
    path('', views.register, name="register")
]