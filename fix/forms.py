from django import forms
from .models import RequestBugs


class RequestForm(forms.ModelForm):

    files = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}), required=False)

    class Meta:
        model = RequestBugs
        fields = '__all__'
        exclude = ['date']
