from django import forms
from .models import Ritual


class RitualForm(forms.ModelForm):
    class Meta:
        model = Ritual
        fields = [
            'name',
            'description',
            'instructions',
            'related_products',
            'magic_properties',
            'image',
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

