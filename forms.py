from django import forms
from .models import File

class SubjectForm(forms.Form):
    SUBJECT_CHOICES = [
        ('mathematics', 'Mathematics'),
        ('physics', 'Physics'),
        ('java','Java'),
        ('python','Python'),
        ('C-programming')
    ]
    
    subject = forms.ChoiceField(choices=SUBJECT_CHOICES, label='Select a Subject')

class FileUploadForm(forms.ModelForm):
    class Meta:
        model = File
        fields = ['uploaded_file']