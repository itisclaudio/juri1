from django.urls import include, path
from .views import CasacionesLista, QuickSearch
from . import views

app_name = "juri"

urlpatterns = [
    path('', views.index_view, name='index'),
    path('casaciones/', CasacionesLista.as_view(), name='casaciones'),
    path('casacion/<int:casacion_id>/', views.casacion_detalle_view, name='casacion'),
    path('searchquick/', QuickSearch.as_view(), name='search'),
]
