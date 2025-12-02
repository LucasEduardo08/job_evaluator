from django import forms
from django.contrib.auth.forms import User

class SimpleRegisterForm(forms.Form):
    email = forms.EmailField(label="Email", widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label="Senha", widget=forms.PasswordInput(attrs={'class': 'form-control'}))
   
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Este email já está cadastrado.")
        return email

# Formulário de Upload
class ResumeUploadForm(forms.Form):
    job_description = forms.CharField(widget=forms.Textarea(attrs={'rows': 10, 'class': 'form-control'}), 
        label="Descrição da Vaga")    
    resume_text = forms.CharField(widget=forms.Textarea(attrs={'rows': 10, 'class': 'form-control'}), 
        label="Cole o Texto do Currículo")