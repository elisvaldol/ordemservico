from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.

class Cliente(models.Model):
    nome = models.CharField(max_length=200,null = False)
    cpf_cnpj = models.CharField(max_length=14)
    endereco = models.CharField(max_length=200)
    bairro = models.CharField(max_length=100)
    cidade = models.CharField(max_length=200)
    tel = models.IntegerField(default=991819934)

class vendedor(models.Model):
     nome= models.CharField(max_length=200,null=False)
     cpf_cnpj=models.CharField(max_length=14,null = False)
     endereco=models.CharField(max_length=200,null = False)
     bairro=models.CharField(max_length=100,null = False) 
     cidade=models.CharField(max_length=100,null = False)

class ordemservico(models.Model):
      observacao=models.TextField(max_length=500)
      servico=models.IntegerField(default=0)
      valor_servico=models.DecimalField(max_digits=15, decimal_places=15)
      valor_produto=models.DecimalField(max_digits=15, decimal_places=15)
      valor_total=models.DecimalField(max_digits=15, decimal_places=15)
      author = models.IntegerField(default=0)
      data_solicitacao = models.DateTimeField(default=timezone.now)
      

class os_servico(models.Model):
    cod_servico = models.IntegerField(default=0)
    cod_ordem = models.IntegerField(default=0)
    precoservico=models.DecimalField(max_digits=15, decimal_places=15)


