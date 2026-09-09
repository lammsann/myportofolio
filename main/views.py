# Create your views here.
from django.shortcuts import render

from main.models import Experience, Mahasiswa


def show_main(request):
    context = {
        "name": "Ghulam Muhammad Ihsan",
        "npm": "2506656766",
        "study_program": "S1 Ilmu Komputer",
        "bio": (
            "I'm a Computer Science student at Universitas Indonesia and I'm really interested in Blockchain and Cybersecurity. I have some basic knowledge in networking and cloud computing. I also have practical experience as an IT Technician Intern, where I developed hands-on skills in network troubleshooting, hardware maintenance, and system support."
        ),
        "mahasiswa_list": Mahasiswa.objects.all(),
    }
    return render(request, "index.html", context)


def show_experience(request):
    context = {
        "name": "Ghulam",
        "experience_list": Experience.objects.all(),
    }
    return render(request, "experience.html", context)