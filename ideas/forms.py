from django import forms

from .models import Idea

# Creates a DjangoForm


class IdeaModelForm(forms.ModelForm):
    class Meta:
        model = Idea
        fields = [
            'title',
            'content'
        ]

    def clean_title(self):
        data = self.cleaned_data.get('title')
        if len(data) < 3:
            raise forms.ValidationError(
                "The title is not long enough. It should be at least tre characters.")
        return data

    def clean_content(self):
        data = self.cleaned_data.get('content')
        if len(data) < 5:
            raise forms.ValidationError(
                "Content is not long enough. It should be at least five characters.")
        return data
