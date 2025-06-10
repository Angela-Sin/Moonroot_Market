
from django.shortcuts import render, get_object_or_404
from .models import Ritual


def ritual_list(request):
    rituals = Ritual.objects.all()
    return render(request, 'rituals/ritual_list.html', {'rituals': rituals})


def ritual_detail(request, pk):
    ritual = get_object_or_404(Ritual, pk=pk)
    return render(request, 'rituals/ritual_detail.html', {'ritual': ritual})
