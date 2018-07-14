from django import forms

from shortener.validators import validate_url, validate_dot_com


class SubmitUrlForm(forms.Form):
    url = forms.CharField(label='Submit URL', validators=[validate_url, validate_dot_com])

    def clean(self):
        super(SubmitUrlForm, self).clean()

    def clean_url(self):
        url = self.cleaned_data.get('url')
        if 'http' not in url:
            url = 'http://' + url

        return url
