from django.urls import path
from main.views import (
    show_main, show_experience, show_education, create_education, 
    get_education_json, delete_education,
    get_experience_json, create_experience, edit_experience, delete_experience,
    register, login_user, logout_user, toggle_star_experience, create_experience_ajax
)

app_name = "main"

urlpatterns = [
    path("", show_main, name="show_main"),
    path("experience/", show_experience, name="show_experience"),
    path("education/", show_education, name="show_education"),
    
    path("education/add/", create_education, name="create_education"),
    path("api/education/", get_education_json, name="get_education_json"),
    path("education/<uuid:education_id>/delete/", delete_education, name="delete_education"),
    path("api/experience/", get_experience_json, name="get_experience_json"),
    path("experience/add/", create_experience, name="create_experience"),
    path("experience/<uuid:id>/edit/", edit_experience, name="edit_experience"),
    path("experience/<uuid:id>/delete/", delete_experience, name="delete_experience"),
    path("experience/<uuid:id>/star/", toggle_star_experience, name="toggle_star_experience"),
    
    path("register/", register, name="register"),
    path("login/", login_user, name="login"),
    path("logout/", logout_user, name="logout"),

    path("experience/add-ajax/", create_experience_ajax, name="create_experience_ajax"),
]