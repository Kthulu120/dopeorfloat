from django import forms

from .models import Grabber


class PostForm(forms.ModelForm):

    class Meta:
        model = Grabber
        fields = ('imageLink', 'votes','title')
