from django.urls import include, path

from . import views

app_name = "profiles"

urlpatterns = [
    path('contactanos/', views.contactanos_view, name='contactanos'),
    path('logout/', views.logout_view, name='logout'),
    path('login/', views.login_view, name='login'),
]
