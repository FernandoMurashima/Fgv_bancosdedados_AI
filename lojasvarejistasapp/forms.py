from django.forms import ModelForm
from lojasvarejistasapp.models import Loja
from lojasvarejistasapp.models import Produto
from lojasvarejistasapp.models import VendeProduto

#Forms dos Modelos Loja, Produto, VendeProduto

class LojaForm(ModelForm):
  class Meta:
    model = Loja
    fields = ['id_loja', 'nome', 'endereco', 'horario_atendimento']

class ProdutoForm(ModelForm):
  class Meta:
    model = Produto
    fields = ['id_produto', 'codigo', 'nome', 'lote']

class VendeProdutoForm(ModelForm):
  class Meta:
    model = VendeProduto
    fields = ['preco', 'loja', 'produto']
