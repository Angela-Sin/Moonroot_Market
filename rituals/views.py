
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import user_passes_test
from .models import Ritual
from .forms import RitualForm


def is_admin(user):
    return user.is_superuser


@user_passes_test(is_admin)
def add_ritual(request):
    if request.method == 'POST':
        form = RitualForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('ritual_list')
    else:
        form = RitualForm()
    return render(request, 'rituals/ritual_form.html', {'form': form, 'action': 'Add'})

@user_passes_test(is_admin)
def update_ritual(request, ritual_id):
    ritual = get_object_or_404(Ritual, pk=ritual_id)
    if request.method == 'POST':
        form = RitualForm(request.POST, request.FILES, instance=ritual)
        if form.is_valid():
            form.save()
            return redirect('ritual_list')
    else:
        form = RitualForm(instance=ritual)
    return render(request, 'rituals/ritual_form.html', {'form': form, 'action': 'Update'})


def ritual_list(request):
    rituals = Ritual.objects.all()
    return render(request, 'rituals/ritual_list.html', {'rituals': rituals})


def ritual_detail(request, pk):
    ritual = get_object_or_404(Ritual, pk=pk)
    return render(request, 'rituals/ritual_detail.html', {'ritual': ritual})
