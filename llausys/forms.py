from django import forms

from apps.leads.models import EmailLead

class ContactForm(forms.Form):
    email = forms.EmailField()
    content = forms.CharField(widget=forms.Textarea)

    def clean_email(self, *args, **kwargs):
        email = self.cleaned_data.get('email')
        # if email.endswith(".edu"):
        #     raise forms.ValidationError("Invalid info")
        return email

class EmailLeadForm(forms.ModelForm):
    email = forms.EmailField(label="", widget=forms.EmailInput(
        attrs={
            'class': 'input',
            'type':'text',
            'placeholder': 'Enter your email'
        }
    ))
    
    class Meta:
        model = EmailLead
        fields = [
            'email'
        ]

    def clean_email(self):
        email = self.cleaned_data.get("email")
        email_qs = EmailLead.objects.filter(email=email)
        if email_qs.exists():
            raise forms.ValidationError("Email already registered")

        return email