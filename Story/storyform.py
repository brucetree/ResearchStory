from .models import Story
from django import forms

class StoryForm(forms.Form):
    title=forms.CharField(label='title',max_length=128,
                               widget=forms.TextInput(attrs={'placeholder':'Please enter your title'})
                               )
    category=forms.ChoiceField(label='category',choices=(('ComputerScience', 'ComputerScience'),
                                         ('Physics', 'Physics'),
                                         ("ElectricalEngineering", "ElectricalEngineering"))
    )
    #viewsNum=forms.IntegerField(label='viewsNum')
    text=forms.CharField(widget=forms.Textarea)
    videoUrl=forms.URLField(label='videoUrl',max_length=512,
                         widget=forms.URLInput(attrs={'placeholder':'Please enter your content'})
                         )
    paperLink=forms.URLField(label='paperLink',max_length=512,
                             widget=forms.URLInput(attrs={'Placeholder':'Please enter your paper link'}))

    class Meta:
        model = Story
        fields=(
            'title',
            'category',
            'viewsNum',
            'paperLink',
            'text',
            'videoUrl',

        )