from django.shortcuts import render
from .models import DaySpell
from django.db.models import Q

def get_day_spell(request):
    spell = None
    query = ""

    if request.method == "POST":
        query = request.POST.get('keyword')
        spell = DaySpell.objects.filter(Q(keyword__icontains=query)).order_by('?').first()

    return render(request, 'day_spell/day_spell.html', {'spell': spell, 'query': query})