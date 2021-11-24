from django import forms


class TestForm(forms.Form):
    """
    Данный класс описывают форму для ответов.
    """
    option_1 = forms.BooleanField(required=False, initial=False, widget=forms.CheckboxInput(attrs={
        'class': 'check__input'
    }))
    option_2 = forms.BooleanField(required=False, initial=False, widget=forms.CheckboxInput(attrs={
        'class': 'check__input'
    }))
    option_3 = forms.BooleanField(required=False, initial=False, widget=forms.CheckboxInput(attrs={
        'class': 'check__input'
    }))
    option_4 = forms.BooleanField(required=False, initial=False, widget=forms.CheckboxInput(attrs={
        'class': 'check__input'
    }))
