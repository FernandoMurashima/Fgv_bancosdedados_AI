from django.shortcuts import render, redirect
from lojasvarejistasapp.forms import LojaForm
from lojasvarejistasapp.forms import ProdutoForm
from lojasvarejistasapp.forms import VendeProdutoForm
from lojasvarejistasapp.models import Loja
from lojasvarejistasapp.models import Produto
from lojasvarejistasapp.models import VendeProduto



def lojasvarejistasadmin(request):
  return render(request, 'lojasvarejistasadmin.html')

# Loja

def listar_loja(request):
  data = {}
  data['db'] = Loja.objects.all()
  return render(request, 'listar_loja.html', data)

# Completar as views de Loja

def nova_loja(request):
  data = {}
  data['form'] = LojaForm()
  return render(request, 'nova_loja.html', data)

def create_loja(request):
  form = LojaForm(request.POST or None)
  if form.is_valid():
    form.save()
    return redirect('/admin_loja/')
 
def visualizar_loja(request, pk):
  data ={}
  data['db'] = Loja.objects.get(pk=pk)  
  return render(request, 'visualizar_loja.html', data)

def editar_loja(request, pk):
  data = {}
  data['db'] = Loja.objects.get(pk=pk)
  data['form']=LojaForm(instance=data['db'])
  return render(request, 'nova_loja.html', data)

def atualizar_loja(request,pk):
  data = {}
  data['db'] = Loja.objects.get(pk=pk)
  form = LojaForm(request.POST or None, instance=data['db'])
  if form.is_valid():
    form.save()
  return redirect('/admin_loja')

def excluir_loja(request, pk):
  db = Loja.objects.get(pk=pk)
  db.delete()
  return redirect('/admin_loja')

#listar_loja, nova_loja, create_loja, visualizar_loja, editar_loja, atualizar_loja, excluir_loja
# Produto

def listar_produto(request):
  data = {}
  data['db'] = Produto.objects.all()
  return render(request, 'listar_produto.html', data)

# Completar as views de Produto

def novo_produto(request):
  data = {}
  data['form'] = ProdutoForm()
  return render(request, 'novo_produto.html', data)
  
def create_produto(request):
    form=ProdutoForm(request.POST or None)
    if form.is_valid():
      form.save()
    return redirect('/admin_produto')

def visualizar_produto(request,pk):
  data ={}
  data['db'] = Produto.objects.get(pk=pk)  
  return render(request, 'visualizar_produto.html', data)

def editar_produto(request,pk):
  data = {}
  data['db']=Produto.objects.get(pk=pk)
  data['form'] = ProdutoForm(instance=data['db'])
  return render(request, 'novo_produto.html', data)

def atualizar_produto(request,pk):
  data = {}
  data['db']=Produto.objects.get(pk=pk)
  form=ProdutoForm(request.POST or None, instance=data['db'])
  if form.is_valid():
    form.save()
  return redirect('/admin_produto')
    
def excluir_produto(request,pk):
  db=Produto.objects.get(pk=pk)
  db.delete()
  return redirect('/admin_produto')

# Vende Produto

def listar_vendeproduto(request):
  data = {}
  data['db'] = VendeProduto.objects.all()
  return render(request, 'listar_vendeproduto.html', data)


# Completar as views de VendeProduto
#listar_vendeproduto, novo_vendeproduto, create_vendeproduto, visualizar_vendeproduto, editar_vendeproduto, atualizar_vendeproduto, excluir_vendeproduto


def novo_vendeproduto(request):
  data = {}
  data['form'] = VendeProdutoForm()
  return render(request, 'novo_vendeproduto.html', data)

def create_vendeproduto(request):
  form= VendeProdutoForm(request.POST or None)
  if form.is_valid():
    form.save()
  return redirect('/admin/VendeProduto')

def visualizar_vendeproduto(request,pk):
  data = {}
  data['db'] = VendeProduto.objects.get(pk=pk)
  return render(request, 'visualizar_vendeproduto.html', data)

def editar_vendeproduto(request,pk):
  data = {}
  data['db']=VendeProduto.objects.get(pk=pk)
  data['form'] = VendeProdutoForm(instance=data['db'])
  return render(request, 'novo_vendeproduto.html', data)

def atualizar_vendeproduto(request,pk):
  data = {}
  data['db']=VendeProduto.objects.get(pk=pk)
  form=VendeProdutoForm(request.POST or None, instance=data['db'])
  if form.is_valid():
    form.save()
  return redirect('/admin/VendeProduto')

def excluir_vendeproduto(request,pk):
  db=VendeProduto.objects.get(pk=pk)
  db.delete()
  return redirect('/admin/VendeProduto')

