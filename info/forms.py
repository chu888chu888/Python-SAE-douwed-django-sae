from django import forms


class ContactForm(forms.Form):
    photo_img = forms.URLField(max_length=50)
    position = forms.CharField(max_length=20, required=False)
    want_say = forms.CharField(widget=forms.Textarea, max_length=500)
