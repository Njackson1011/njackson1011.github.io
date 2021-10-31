from django import forms


class ScoreForm(forms.Form):
    username = forms.CharField(max_length=10)
    score = forms.IntegerField()
