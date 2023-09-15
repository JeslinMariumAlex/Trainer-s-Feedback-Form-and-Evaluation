from django import forms
from .models import Feedback

class FeedbackForm(forms.ModelForm):

    class Meta:
        model=Feedback
        #fields="__all__"
        fields=['trainer_name','batch_name','course_name','suggestion','rating',]

        widgets={
            'rating':forms.RadioSelect
        }