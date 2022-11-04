from django.shortcuts import render, get_object_or_404
from django.views.generic.list import ListView
from django.db.models import Q
from django.contrib import messages
# from operator import or_, and_
from juri.models import Casacion
from .forms import search_Form


def index_view(request):
    """ Pagina principal """
    template = 'index.html'
    ctx = {}
    return render(request, template, ctx)


class CasacionesLista(ListView):
    """ Lista de Casaciones """
    paginate_by = 10
    model = Casacion
    template_name = 'juri/casaciones_lista.html'

    def get_queryset(self):
        return Casacion.objects.filter(activo=True)


def casacion_detalle_view(request, casacion_id):
    """ Detalle de Casacion """
    template = 'juri/casacion_detalle.html'
    casacion = get_object_or_404(Casacion, id=casacion_id)
    ctx = {'casacion': casacion}
    return render(request, template, ctx)


class QuickSearch(ListView):
    """ Busqueda rapida """
    paginate_by = 10
    model = Casacion
    template_name = 'juri/resultados.html'

    def get_queryset(self):
        search = self.request.GET.get('search',  None)
        object_list = self.model.objects.filter(activo=True)
        print(f'object_list len: {len(object_list)}')
        if search:
            print(f'There is search: {search}')
            object_list = object_list.filter(Q(numero__icontains=search) | Q(demandante__icontains=search)).distinct()
            messages.success(self.request, f'Resultados por: "{search}"')
        return object_list
