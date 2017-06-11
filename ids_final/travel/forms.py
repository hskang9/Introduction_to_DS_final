from django import forms

class SearchPostForm(forms.Form):
    search = forms.CharField(max_length=50, required=True)