from django import forms
from home.models import Post


class HomeForm(forms.ModelForm):
    title = forms.CharField(widget = forms.TextInput(
        attrs = {
        'class' :'form-control',
        'placeholder' : "Enter your title..."
        }
    ))
    text  = forms.CharField(widget = forms.TextInput(
        attrs = {
        'class' :'form-control',
        'placeholder' : "Text goes here..."
        }
    ))

    class Meta:
        model = Post
        fields = ('title',
                    'text',
                )
