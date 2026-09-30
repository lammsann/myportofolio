import datetime
from django.views.decorators.http import require_POST
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.core import serializers
from django.http import HttpResponse
from django.http import JsonResponse

from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied

from main.models import Experience, Education
from main.forms import EducationForm, ExperienceForm

def register(request):
    form = UserCreationForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Akun berhasil dibuat. Silakan login.")
        return redirect("main:login")
    context = {"name": "Ghulam", "form": form}
    return render(request, "register.html", context)

def login_user(request):
    form = AuthenticationForm(request, data=request.POST or None)
    if request.method == "POST" and form.is_valid():
        user = form.get_user()
        login(request, user)
        response = redirect("main:show_main")
        response.set_cookie('last_login', datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        return response
    context = {"name": "Ghulam", "form": form}
    return render(request, "login.html", context)

def logout_user(request):
    logout(request)
    response = redirect("main:show_main")
    response.delete_cookie('last_login')
    return response

def show_main(request):
    last_login = request.COOKIES.get('last_login', 'Belum ada sesi login / Cookie tidak ditemukan')
    context = {
        "name": "Ghulam",
        "npm": "2506656766",
        "study_program": "S1 Ilmu Komputer",
        "bio": ("I'm a Computer Science student at Universitas Indonesia and I'm really interested in Blockchain and Cybersecurity. I have some basic knowledge in networking and cloud computing. I also have practical experience as an IT Technician Intern, where I developed hands-on skills in network troubleshooting, hardware maintenance, and system support."),
        "last_login": last_login,
    }
    return render(request, "index.html", context)

def get_experience_json(request):
    title_query = request.GET.get("title", "").strip()
    experiences = Experience.objects.prefetch_related('starred_by').all()
    if title_query:
        experiences = experiences.filter(title__icontains=title_query)
        
    data = []
    for exp in experiences:
        starred_users = exp.starred_by.all()
        is_starred = request.user in starred_users if request.user.is_authenticated else False
        starred_by_names = ", ".join([u.username for u in starred_users])
        
        data.append({
            "pk": str(exp.id),
            "fields": {
                "title": exp.title,
                "description": exp.description,
                "category_display": exp.get_category_display(),
                "is_ongoing": exp.is_ongoing,
                "star_count": starred_users.count(),
                "is_starred": is_starred,
                "starred_by_names": starred_by_names,
            }
        })
    return JsonResponse(data, safe=False)

def show_experience(request):
    title_query = request.GET.get("title", "").strip()
    is_editor = request.user.groups.filter(name='Editor').exists() if request.user.is_authenticated else False
    
    context = {
        "name": "Ghulam",
        "title_query": title_query,
        "is_editor": is_editor,
        "form": ExperienceForm(),
    }
    return render(request, "experience.html", context)

@login_required(login_url="/login/")
def create_experience(request):
    if not request.user.is_superuser: raise PermissionDenied
    form = ExperienceForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Pengalaman baru berhasil ditambahkan!")
        return redirect("main:show_experience")
    context = {"name": "Ghulam", "form": form}
    return render(request, "experience_form.html", context)

@login_required(login_url="/login/")
def edit_experience(request, id):
    is_editor = request.user.groups.filter(name='Editor').exists()
    if not (request.user.is_superuser or is_editor): 
        raise PermissionDenied
    experience = get_object_or_404(Experience, pk=id)
    form = ExperienceForm(request.POST or None, instance=experience)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Pengalaman berhasil diperbarui!")
        return redirect("main:show_experience")
    context = {"name": "Ghulam", "form": form, "is_update": True}
    return render(request, "experience_form.html", context)

@login_required(login_url="/login/")
def delete_experience(request, id):
    if not request.user.is_superuser: raise PermissionDenied
    experience = get_object_or_404(Experience, pk=id)
    if request.method == "POST":
        experience.delete()
        messages.success(request, "Pengalaman berhasil dihapus!")
        return redirect("main:show_experience")
    return redirect("main:show_experience")

@login_required(login_url="/login/")
def toggle_star_experience(request, id):
    experience = get_object_or_404(Experience, pk=id)
    if request.method == "POST":
        if request.user in experience.starred_by.all():
            experience.starred_by.remove(request.user)
        else:
            experience.starred_by.add(request.user)
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

@login_required(login_url="/login/")
def create_education(request):
    if not request.user.is_superuser: raise PermissionDenied
    form = EducationForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Pendidikan baru berhasil ditambahkan!")
        return redirect("main:show_education")
    context = {"name": "Ghulam", "form": form}
    return render(request, "education_form.html", context)

@login_required(login_url="/login/")
def delete_education(request, education_id):
    if not request.user.is_superuser: raise PermissionDenied
    education = get_object_or_404(Education, pk=education_id)
    if request.method == "POST":
        education.delete()
        messages.success(request, "Riwayat pendidikan berhasil dihapus!")
        return redirect("main:show_education")
    return redirect("main:show_education")


@require_POST
def create_experience_ajax(request):
    if not request.user.is_superuser:
        return JsonResponse({"message": "Hanya pemilik yang dapat menambahkan experience."}, status=403)
    
    form = ExperienceForm(request.POST)
    if form.is_valid():
        experience = form.save()
        return JsonResponse({"message": "Berhasil ditambahkan.", "pk": str(experience.id)}, status=201)
    
    return JsonResponse({"errors": form.errors.get_json_data()}, status=400)