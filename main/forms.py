from django.forms import ModelForm, TextInput, Textarea, Select
from main.models import Education, Experience

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