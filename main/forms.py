from django.forms import ModelForm, TextInput, Textarea
from main.models import Education

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