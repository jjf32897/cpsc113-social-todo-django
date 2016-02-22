from django import forms

# defines the registration, login and new task forms with styled placeholders
class RegistrationForm(forms.Form):
    fl_name = forms.CharField(max_length=100, label='', widget=forms.TextInput(attrs={'placeholder': 'Name', 'onfocus': "this.placeholder = ''", 'onblur': "this.placeholder = 'Name'"}))
    email = forms.EmailField(max_length=100, label='', widget=forms.TextInput(attrs={'placeholder': 'Email address', 'onfocus': "this.placeholder = ''", 'onblur': "this.placeholder = 'Email address'"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'onfocus': "this.placeholder = ''", 'onblur': "this.placeholder = 'Password'"}), label='')
    password_confirmation = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirm password', 'onfocus': "this.placeholder = ''", 'onblur': "this.placeholder = 'Confirm password'"}), label='')

class LoginForm(forms.Form):
    email = forms.EmailField(max_length=100, label='', widget=forms.TextInput(attrs={'placeholder': 'Email address', 'onfocus': "this.placeholder = ''", 'onblur': "this.placeholder = 'Email address'"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'onfocus': "this.placeholder = ''", 'onblur': "this.placeholder = 'Password'"}), label='')

class NewTaskForm(forms.Form):
    title = forms.CharField(max_length=500, label='Task Info', widget=forms.TextInput(attrs={'placeholder': 'Task title', 'onfocus': "this.placeholder = ''", 'onblur': "this.placeholder = 'Task title'"}))
    description = forms.CharField(max_length=5000, label='', widget=forms.TextInput(attrs={'placeholder': 'Description', 'onfocus': "this.placeholder = ''", 'onblur': "this.placeholder = 'Description'"}))
    collaborator1 = forms.CharField(max_length=100, required=False, label='Collaborators', widget=forms.TextInput(attrs={'placeholder': 'Email address', 'onfocus': "this.placeholder = ''", 'onblur': "this.placeholder = 'Email address'"}))
    collaborator2 = forms.CharField(max_length=100, required=False, label='', widget=forms.TextInput(attrs={'placeholder': 'Email address', 'onfocus': "this.placeholder = ''", 'onblur': "this.placeholder = 'Email address'"}))
    collaborator3 = forms.CharField(max_length=100, required=False, label='', widget=forms.TextInput(attrs={'placeholder': 'Email address', 'onfocus': "this.placeholder = ''", 'onblur': "this.placeholder = 'Email address'"}))
