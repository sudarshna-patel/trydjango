from django import forms
from .models import Course

class CourseModelForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['title']
    
    # validation only does it on the form not on model level
    # to validate a key, so mthod name should be clean_<fieldname>
    def clean_title(self):
        title = self.cleaned_data.get('title')
        if title.lower() == 'abc':
            raise forms.ValidationError("This is not a valid title") 
        return title