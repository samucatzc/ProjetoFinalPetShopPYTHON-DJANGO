from django.shortcuts import render
from base.forms import ContatoForm, ReservaForm, AgendamentoForm, CategoriaForm, PetForm

def inicio(request):
    return render(request, "inicio.html")

def contato(request):
    sucesso = False
    if request.method == "GET":
        form = ContatoForm()
    else:
        form = ContatoForm(request.POST)
        if form.is_valid():
            sucesso = True
            form.save()
    contexto = {
        'telefone': '(99) 99999.9999',
        'responsavel': 'Samuel Carlos de Souza',
        'form' : form,
        'sucesso': sucesso
    }

    return render(request, "contato.html", contexto)

def reserva(request):
    sucesso = False
    if request.method == "GET":
        form = ReservaForm()
    else:
        form = ReservaForm(request.POST)
        if form.is_valid():
            sucesso = True
            form.save()
    contexto = {
        'form' : form,
        'sucesso': sucesso
    }

    return render(request, "reserva.html", contexto)

def agendamento(request):
    sucesso = False
    if request.method == "GET":
        form = AgendamentoForm()
    elif request.method == "DELETE":
        form = AgendamentoForm(request.DELETE)
        if form.is_valid():
            sucesso = True
            form.delete()
    else:
        form = AgendamentoForm(request.POST)
        if form.is_valid():
            sucesso = True
            form.save()
    contexto = {
        'form' : form,
        'sucesso': sucesso
    }

    return render(request, "agendamento.html", contexto)

def categoria(request):
    sucesso = False
    if request.method == "GET":
        form = CategoriaForm()
    else:
        form = CategoriaForm(request.POST)
        if form.is_valid():
            sucesso = True
            form.save()
    contexto = {
        'telefone': '(99) 99999.9999',
        'responsavel': 'Samuel Carlos de Souza',
        'form' : form,
        'sucesso': sucesso
    }

    return render(request, "categoria.html", contexto)

def pet(request):
    sucesso = False
    if request.method == "GET":
        form = PetForm()
    else:
        form = PetForm(request.POST)
        if form.is_valid():
            sucesso = True
            form.save()
    contexto = {
        'telefone': '(99) 99999.9999',
        'responsavel': 'Samuel Carlos de Souza',
        'form' : form,
        'sucesso': sucesso
    }

    return render(request, "pet.html", contexto)

