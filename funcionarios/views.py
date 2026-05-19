from django.contrib import messages
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.core.paginator import Paginator
from django.db.models import ProtectedError
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from funcionarios.forms import FuncionariosModelForm
from funcionarios.models import Funcionario


# Create your views here.
class FuncionariosView(PermissionRequiredMixin, ListView):
    permission_required = 'funcionarios.view_funcionario'
    permission_denied_message = 'Visualizar funcionário'
    model = Funcionario
    template_name = 'funcionarios.html'

    def get_queryset(self):
        buscar = self.request.GET.get('buscar')
        qs = super(FuncionariosView, self).get_queryset()

        if buscar:
            qs = qs.filter(nome__icontains=buscar)

        if qs.count() > 0:
            paginator = Paginator(qs, 10)
            listagem = paginator.get_page(self.request.GET.get('page'))
            return listagem
        else:
            return messages.info(self.request, 'Não existem funcionários cadastrdos!')

class FuncionarioAddView(PermissionRequiredMixin, SuccessMessageMixin, CreateView):
    permission_required = 'funcionarios.add_funcionario'
    permission_denied_message = 'Cadastrar funcionário'
    model = Funcionario
    form_class = FuncionariosModelForm
    template_name = 'funcionario_form.html'
    success_url = reverse_lazy('funcionarios')
    success_message = 'Funcionario cadastrado com sucesso!'

class FuncionarioUpdateView(PermissionRequiredMixin, SuccessMessageMixin, UpdateView):
    permission_required = 'funcionarios.update_funcionario'
    permission_denied_message = 'Editar funcionário'
    model = Funcionario
    form_class = FuncionariosModelForm
    template_name = 'funcionario_form.html'
    success_url = reverse_lazy('funcionarios')
    success_message = 'Funcionario atualizado com sucesso!'

class FuncionarioDeleteView(PermissionRequiredMixin, SuccessMessageMixin, DeleteView):
    permission_required = 'funcionarios.delete_funcionario'
    permission_denied_message = 'Excluir funcionário'
    model = Funcionario
    template_name = 'funcionario_apagar.html'
    success_url = reverse_lazy('funcionarios')
    success_message = 'Funcionario excluído com sucesso!'

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_url = self.get_success_url()
        try:
            return super().post(request, *args, **kwargs)
        except ProtectedError:
            messages.error(request, f'O funcionário {self.object} não pode ser excluído.'
                           f'Esse funcioário está registrado em agendamentos e/ou ordens de serviço.')

        return redirect(success_url)