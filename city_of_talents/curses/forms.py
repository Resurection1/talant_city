from django import forms
from .models import Video


class MyModelForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ['video_file']
        widgets = {
            'video_file': forms.ClearableFileInput(attrs={'multiple': True}),
        }
