from django import forms
# Create your forms here.


class ContactForm(forms.Form):
    contact_email = forms.EmailField(required=True, label="Email")
    subject = forms.CharField(required=True, label="Subject")
    content = forms.CharField(
        required=True,
        widget=forms.Textarea,
        label="Message"
    )
