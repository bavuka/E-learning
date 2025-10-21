from django import forms
from instructor.models import User

class InstructorCreateForm(forms.ModelForm):
    class Meta:
        model=User
        fields=["first_name","username","email","password"]

        widgets={"first_name":forms.TextInput(attrs={"class":"form_control"}),
                 "username":forms.TextInput(attrs={"class":"form_control"}),
                 "email":forms.TextInput(attrs={"class":"form_control"}),
                 "password":forms.PasswordInput(attrs={"class":"form_control"}),}



# widgets_peaks        