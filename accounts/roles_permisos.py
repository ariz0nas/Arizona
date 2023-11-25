from django.shortcuts import render
from django.views import View
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .models import Rol, Permiso
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.shortcuts import redirect

class RolListView(ListView):
    model = Rol
    template_name = 'roles/roles_permisos.html'
    context_object_name = 'roles'

class RolDetailView(DetailView):
    model = Rol
    template_name = 'roles/roles_permisos.html'
    context_object_name = 'rol'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['permisos'] = Permiso.objects.all()
        return context

    def post(self, request, *args, **kwargs):
        rol = get_object_or_404(Rol, pk=self.kwargs['pk'])
        permisos = request.POST.getlist('permisos')

        # Actualizar permisos del rol
        rol.permisos.set(permisos)

        return redirect(reverse('account:rol-det', args=[rol.pk]))
