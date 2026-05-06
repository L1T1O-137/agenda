from django.db import models
from django.db.models.functions import Upper


class Servico(models.Model):
    nome = models.CharField(max_length=100, help_text='Nome completo do serviço', unique=True)
    preco = models.DecimalField(max_digits=5, decimal_places=2, help_text='Preço do serviço')
    descricao = models.TextField('Descrição', max_length=300, help_text='Descrião do serviço')
    produtos = models.ManyToManyField('produtos.Produto', through='servicos.ProdutosServico', related_name='servco_produtos')
    class Meta:
        verbose_name = 'Serviço'
        verbose_name_plural = 'Serviços'
        ordering = [Upper('nome')]

    def __str__(self):
        return self.nome

class ProdutosServico(models.Model):
    servico = models.ForeignKey('servicos.Servico', verbose_name='Serviço', on_delete=models.CASCADE, related_name='produtos_servico_servico')
    produto = models.ForeignKey('produtos.Produto', verbose_name='Produto', on_delete=models.PROTECT, related_name='produtos_servico_produto')
    quantidade = models.DecimalField('Quantidade', max_digits=5, decimal_places=2)

    class Meta:
        verbose_name = 'Produto utilizado'
        verbose_name_plural = 'Produtos utilizados'

        constraints = [models.UniqueConstraint(fields=['servico', 'produto'], name='constraint_servico_produto')]

    def __str__(self):
        return f'{self.produto}'
