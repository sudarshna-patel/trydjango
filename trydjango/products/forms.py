from django import forms
from .models import Product

# django form
class ProductForm(forms.ModelForm):
    title       = forms.CharField(label='', widget=forms.TextInput(attrs={"placeholder": "Your Title"})) # can change/set the label here
    # email       = forms.EmailField()
    description = forms.CharField(required=False, widget=forms.Textarea(
                                                        attrs={
                                                            "class": "new-class-name two",
                                                            "id": "my-id-for-textarea",
                                                            "placeholder": "Your Description",
                                                            "rows": 15,
                                                            "cols": 50
                                                        })) # any different attribute you can place here.
    price       = forms.DecimalField(initial=199.99) # can also set initial value of fields

    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price'
        ]

    # to get post django form cleaning title
    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get("title")
        if not "CFE" in title:
            raise forms.ValidationError("This is not valid title")
        return title

    # def clean_email(self, *args, **kwargs):
    #     email = self.cleaned_data.get("email")
    #     if not email.endswith("edu"):
    #         raise forms.ValidationError("This is not a valid email")
    #     return email

# Pure Django Form
class RawProductForm(forms.Form):
    # so this is how you overwrite the some of the basic things about the from itself
    title       = forms.CharField(label='', widget=forms.TextInput(attrs={"placeholder": "Your Title"})) # can change/set the label here
    description = forms.CharField(required=False, widget=forms.Textarea(
                                                        attrs={
                                                            "class": "new-class-name two",
                                                            "id": "my-id-for-textarea",
                                                            "placeholder": "Your Description",
                                                            "rows": 15,
                                                            "cols": 50
                                                        })) # any different attribute you can place here.
    price       = forms.DecimalField(initial=199.99) # can also set initial value of fields