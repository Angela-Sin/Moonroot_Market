from django.shortcuts import render
from .models import DaySpell
from django.db.models import Q
import logging


logger = logging.getLogger(__name__)  


def get_day_spell(request):
    spell = None
    query = ""

    if request.method == "POST":
        query = request.POST.get('keyword', '').strip()
        logger.info(f"Received keyword: {query}")

        if query:
            try:
                spell = (
                    DaySpell.objects.filter(Q(keyword__icontains=query))
                    .order_by('?')
                    .first()
                )
                logger.info(f"Found spell: {spell}") 
            except Exception as e:
                logger.error(f"Database error: {e}")  
                spell = None 

    return render(
        request, 'day_spell/day_spell.html', {'spell': spell, 'query': query}
    )
