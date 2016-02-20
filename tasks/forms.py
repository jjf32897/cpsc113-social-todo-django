from django import forms

class NewTaskForm(forms.Form):
    title = forms.CharField(max_length=500, label='task info', widget=forms.TextInput(attrs={'placeholder': 'task title', 'onfocus': "this.placeholder = ''", 'onblur': "this.placeholder = 'task title'"}))
    description = forms.CharField(max_length=5000, label='', widget=forms.TextInput(attrs={'placeholder': 'description', 'onfocus': "this.placeholder = ''", 'onblur': "this.placeholder = 'description'"}))
    collaborator1 = forms.CharField(max_length=100, required=False, label='collaborators', widget=forms.TextInput(attrs={'placeholder': 'collaborator email', 'onfocus': "this.placeholder = ''", 'onblur': "this.placeholder = 'name'"}))
    collaborator2 = forms.CharField(max_length=100, required=False, label='', widget=forms.TextInput(attrs={'placeholder': 'collaborator email', 'onfocus': "this.placeholder = ''", 'onblur': "this.placeholder = 'name'"}))
    collaborator3 = forms.CharField(max_length=100, required=False, label='', widget=forms.TextInput(attrs={'placeholder': 'collaborator email', 'onfocus': "this.placeholder = ''", 'onblur': "this.placeholder = 'name'"}))
