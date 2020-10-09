from django import forms

class NewUserForm(forms.Form):
    username = forms.CharField(label="declare username")
    password_declare = forms.CharField(label="declare password")
    password_confirm = forms.CharField(label="confirm password")

class LoginForm(forms.Form):
    username = forms.CharField(label="username")
    password = forms.CharField(label="password")
    
    def clean_message(self):
        username = self.cleaned_data.get("username")
        return username
