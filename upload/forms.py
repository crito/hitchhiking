from django import forms
from models import Upload
 
class UploadForm(forms.models.ModelForm):
    class Meta:
        model = Upload
        exclude = ('timestamp',)
