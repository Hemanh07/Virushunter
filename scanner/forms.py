from django import forms

class UploadFileForm(forms.Form):
    file = forms.FileField(widget=forms.ClearableFileInput(attrs={'class': 'custom-file-input','id':'fileinput','placeholder': 'Choose file...'}))