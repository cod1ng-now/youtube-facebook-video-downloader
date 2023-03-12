from django import forms
from .models import YoutubeRecord

class YoutubeDownloadForm(forms.ModelForm):
    class Meta:
        model=YoutubeRecord
        fields=('link',)
        widgets={
            'link':forms.URLInput(attrs={'class':'form-control shadow-lg','placeholder':'paste your video link here'})
        }