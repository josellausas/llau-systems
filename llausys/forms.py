from django import forms


class ContactForm(forms.Form):
    email = forms.EmailField()
    content = forms.CharField(widget=forms.Textarea)
