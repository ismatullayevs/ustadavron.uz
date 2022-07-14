from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder': 'Name', 'class': 'form-control'}))
    email = forms.EmailField(max_length=150, widget=forms.TextInput(attrs={'placeholder': 'Email', 'class': 'form-control', 'type': 'email'}))
    subject = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder': 'Subject', 'class': 'form-control'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'I want to join the masterclass because...', 'rows': 6, 'class': 'form-control'}), max_length=2000)