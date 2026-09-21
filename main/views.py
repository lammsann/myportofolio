# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.core import serializers
from django.http import HttpResponse
from main.models import Experience, Education
from main.forms import EducationForm, ExperienceForm


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

def get_experience_json(request):
    title_query = request.GET.get("title", "").strip()
    experiences = Experience.objects.all()
    if title_query:
        experiences = experiences.filter(title__icontains=title_query)

    experiences_json = serializers.serialize("json", experiences)

    return HttpResponse(experiences_json, content_type="application/json")

def show_experience(request):
    json_response = get_experience_json(request)
    experiences = serializers.deserialize("json", json_response.content.decode("utf-8"))
    experiences = [exp.object for exp in experiences]
    
    title_query = request.GET.get("title", "").strip()
    context = {
        "name": "Ghulam",
        "experience_list": experiences,
        "title_query": title_query,
    }

    return render(request, "experience.html", context)

def create_experience(request):
    form = ExperienceForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Pengalaman baru berhasil ditambahkan!")
        return redirect("main:show_experience")
    context = {
        "name": "Ghulam", 
        "form": form
    }

    return render(request, "experience_form.html", context)

def edit_experience(request, id):
    experience = get_object_or_404(Experience, pk=id)
    form = ExperienceForm(request.POST or None, instance=experience) # instance ini agar formnya terisi otomatis
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Pengalaman berhasil diperbarui!")
        return redirect("main:show_experience")
    context = {
        "name": "Ghulam", 
        "form": form, 
        "is_update": True
    }

    return render(request, "experience_form.html", context)

def delete_experience(request, id):
    experience = get_object_or_404(Experience, pk=id)
    if request.method == "POST":
        experience.delete()
        messages.success(request, "Pengalaman berhasil dihapus!")
        return redirect("main:show_experience")
    
    return redirect("main:show_experience")

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