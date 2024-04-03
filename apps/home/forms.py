from .models import New
from django import forms
from django.utils import  timezone



class ExistingListItemForm(forms.models.ModelForm):

    def __init__(self, for_list, *args, **kwargs):
        super(ExistingListItemForm, self).__init__(*args, **kwargs)


        

class NewCreateForm(forms.ModelForm):
    class Meta:
        model=New
        fields=["image", "title", "body", "category", "tags"]
        widgets={
            "title":forms.TextInput(attrs={'class':'form-control'}),
            "body":forms.Textarea(attrs={'class':'form-control'}),
            "category":forms.Select(attrs={'class':'form-control'}),
            "tags":forms.SelectMultiple(attrs={'class':'form-control'})

        }