from django import forms

from .models import Funcionario

class FuncionariosModelForm(forms.ModelForm):

    class Meta:
        model = Funcionario
        fields = ['nome', 'funcao', 'fone', 'email', 'data_admissao', 'foto']


        error_messages = {
            'nome': {'required': 'O nome do funcionário é um campo obrigatório'},
            'funcao': {'required': 'A função do funcionário é um campo obrigatório'},
            'fone': {'required': 'O número de telefone do funcionário é um campo obrigatório'},
            'email': {'required': 'Formato inválido para o e-mail. Exemplo de formato válido: fulano@dominio.com', 'unique': 'E-mail já cadastrado'
            },
            'data_admissao': {'required': 'A data de admissão é um campo obrigatório'},
        }