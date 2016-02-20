from django import forms

class RegistrationForm(forms.Form):
    fl_name = forms.CharField(max_length=100, label='', widget=forms.TextInput(attrs={'placeholder': 'name', 'onfocus': "this.placeholder = ''", 'onblur': "this.placeholder = 'name'"}))
    email = forms.EmailField(max_length=100, label='', widget=forms.TextInput(attrs={'placeholder': 'email address', 'onfocus': "this.placeholder = ''", 'onblur': "this.placeholder = 'email address'"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'password', 'onfocus': "this.placeholder = ''", 'onblur': "this.placeholder = 'password'"}), label='')
    password_confirmation = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'confirm password', 'onfocus': "this.placeholder = ''", 'onblur': "this.placeholder = 'confirm password'"}), label='')

class LoginForm(forms.Form):
    email = forms.EmailField(max_length=100, label='', widget=forms.TextInput(attrs={'placeholder': 'email address', 'onfocus': "this.placeholder = ''", 'onblur': "this.placeholder = 'email address'"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'password', 'onfocus': "this.placeholder = ''", 'onblur': "this.placeholder = 'password'"}), label='')

class NewTaskForm(forms.Form):
    title = forms.CharField(max_length=500, label='task info', widget=forms.TextInput(attrs={'placeholder': 'task title', 'onfocus': "this.placeholder = ''", 'onblur': "this.placeholder = 'task title'"}))
    description = forms.CharField(max_length=5000, label='', widget=forms.TextInput(attrs={'placeholder': 'description', 'onfocus': "this.placeholder = ''", 'onblur': "this.placeholder = 'description'"}))
    collaborator1 = forms.CharField(max_length=100, required=False, label='collaborators', widget=forms.TextInput(attrs={'placeholder': 'email', 'onfocus': "this.placeholder = ''", 'onblur': "this.placeholder = 'email'"}))
    collaborator2 = forms.CharField(max_length=100, required=False, label='', widget=forms.TextInput(attrs={'placeholder': 'email', 'onfocus': "this.placeholder = ''", 'onblur': "this.placeholder = 'email'"}))
    collaborator3 = forms.CharField(max_length=100, required=False, label='', widget=forms.TextInput(attrs={'placeholder': 'email', 'onfocus': "this.placeholder = ''", 'onblur': "this.placeholder = 'email'"}))
