from django import forms
from blog.models import BlogPost

JOBS=(
    ("python", "Développeur python"),
    ("javascript", "Développeur javascript"),
    ("java", "Développeur java"),
)

class SignupForm(forms.Form):
    pseudo = forms.CharField(max_length=8, required=False)
    email = forms.EmailField()
    password = forms.CharField(min_length=6, widget=forms.PasswordInput())
    job = forms.ChoiceField(choices=JOBS)
    cgu_accept = forms.BooleanField(initial=True)

    def clean_pseudo(self):
        pseudo = self.cleaned_data.get("pseudo")
        if "$" in pseudo:
            raise forms.ValidationError("Champ invalide")
        else:
            return pseudo
class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ["title", "published", "description", "content"]
        labels = {"title":"Titre", "category":"Catégorie"}
        widgets = {"date":forms.SelectDateWidget(years=range(1990, 2040))}