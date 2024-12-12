from django import forms
from django.forms import inlineformset_factory
from .models import Article, Image

class EditArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('title', 'content')
        widgets = {
            'title': forms.TextInput(attrs={
            'class': 'form-control' 
            }),
            'content': forms.Textarea(attrs={
            'class': 'form-control' 
            }),
        }

ImageFormSet = inlineformset_factory(
    Article, 
    Image, 
    fields=('img', 'caption'), 
    extra=1, 
    can_delete=True,
    widgets={
        'img': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        'caption': forms.TextInput(attrs={'class': 'form-control'}),
    }
)