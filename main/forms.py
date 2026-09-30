from django.forms import ModelForm, TextInput, Textarea, Select
from main.models import Education, Experience
from django.core.exceptions import ValidationError
from django.utils.html import strip_tags 

class EducationForm(ModelForm):
    class Meta:
        model = Education
        fields = ["degree", "institution", "description", "graduation_year"]
        
        labels = {
            "degree": "Gelar / Tingkat",
            "institution": "Institusi",
            "description": "Deskripsi",
            "graduation_year": "Tahun Lulus",
        }
        
        widgets = {
            "degree": TextInput(attrs={"placeholder": "Contoh: S1 Ilmu Komputer"}),
            "institution": TextInput(attrs={"placeholder": "Contoh: Universitas Indonesia"}),
            "description": Textarea(attrs={"placeholder": "Ceritakan pendidikanmu", "rows": 3}),
            "graduation_year": TextInput(attrs={"placeholder": "Contoh: 2028"}),
        }

class ExperienceForm(ModelForm):
    class Meta:
        model = Experience
        fields = ["title", "description", "category"]
        
        labels = {
            "title": "Posisi / Pekerjaan",
            "description": "Deskripsi Pekerjaan",
            "category": "Kategori",
        }
        
        widgets = {
            "title": TextInput(attrs={"placeholder": "Contoh: Software Engineer Intern"}),
            "description": Textarea(attrs={"placeholder": "Ceritakan pengalaman kerjamu", "rows": 3}),
            "category": Select(),
        }

    def clean_title(self):
        title = strip_tags(self.cleaned_data["title"]).strip()
        if not title:
            raise ValidationError("Posisi/Pekerjaan tidak boleh hanya berisi tag HTML.")
        return title
    def clean_description(self):
        return strip_tags(self.cleaned_data["description"]).strip()