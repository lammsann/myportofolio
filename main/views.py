# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.core import serializers
from django.http import HttpResponse
from main.models import Experience, Education
from main.forms import EducationForm


def show_main(request):
    context = {
        "name": "Ghulam",
        "npm": "2506656766",
        "study_program": "S1 Ilmu Komputer",
        "bio": (
            "I'm a Computer Science student at Universitas Indonesia and I'm really interested in Blockchain and Cybersecurity. I have some basic knowledge in networking and cloud computing. I also have practical experience as an IT Technician Intern, where I developed hands-on skills in network troubleshooting, hardware maintenance, and system support."
        ),
    }
    return render(request, "index.html", context)


def show_experience(request):
    context = {
        "name": "Ghulam",
        "experience_list": Experience.objects.all(),
    }
    return render(request, "experience.html", context)

def get_education_json(request):
    title_query = request.GET.get("title", "").strip()
    educations = Education.objects.all()
    
    if title_query:
        educations = educations.filter(institution__icontains=title_query)
        
    educations_json = serializers.serialize("json", educations)
    return HttpResponse(educations_json, content_type="application/json")

def show_education(request):
    json_response = get_education_json(request)
    educations = serializers.deserialize("json", json_response.content.decode("utf-8"))
    educations = [edu.object for edu in educations]
    
    title_query = request.GET.get("title", "").strip()
    context = {
        "name": "Ghulam",
        "education_list": educations,
        "title_query": title_query,
    }
    return render(request, "education.html", context)

def create_education(request):
    form = EducationForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Pendidikan baru berhasil ditambahkan!")
        return redirect("main:show_education")
    context = {
        "name": "Ghulam",
        "form": form,
    }
    return render(request, "education_form.html", context)

def delete_education(request, education_id):
    education = get_object_or_404(Education, pk=education_id)
    if request.method == "POST":
        education.delete()
        messages.success(request, "Riwayat pendidikan berhasil dihapus!")
        return redirect("main:show_education")
    return redirect("main:show_education")