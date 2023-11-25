from django.db import models

# Create your models here.

# Modelo Loja
class Loja(models.Model):
  id_loja = models.CharField(max_length=10, primary_key=True)
  nome = models.CharField(max_length=30)
  endereco = models.CharField(max_length=50)
  horario_atendimento = models.CharField(max_length=30)


# Modelo Produto
class Produto(models.Model):
  id_produto = models.CharField(max_length=10, primary_key=True)
  codigo = models.CharField(max_length=30)
  nome = models.CharField(max_length=30)
  lote = models.CharField(max_length=30)


# Modelo VendeProduto
class VendeProduto(models.Model):
  preco = models.FloatField()
  loja = models.CharField(max_length=10)
  produto = models.CharField(max_length=10)



