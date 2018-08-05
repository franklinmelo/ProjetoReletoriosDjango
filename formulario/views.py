from django.shortcuts import render, redirect, get_object_or_404
from .models import Relatorio
from .forms import RelatorioForm


def list_relatorios(request):
    relatorios = Relatorio.objects.all()
    return render(request, 'relatorios.html', {'relatorios': relatorios})


def create_relatorios(request):
    form = RelatorioForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('list_relatorio')

    return render(request, 'relatorio-form.html', {'form': form})


def update_relatorio(request, id):
    relatorio = Relatorio.objects.get(id=id)

    form = RelatorioForm(request.POST or None, instance=relatorio)

    if form.is_valid():
        form.save()
        return redirect('list_relatorio')

    return render(request, 'relatorio-form.html', {'form': form, 'relatorio': relatorio})


def delete_relatorio(request, id):
    relatorio = Relatorio.objects.get(id=id)

    if request.method == 'POST':
        relatorio.delete()
        return redirect('list_relatorio')

    return render(request, 'relatorio-delete-confirm.html', {'relatorio': relatorio})
