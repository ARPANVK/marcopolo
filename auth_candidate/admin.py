from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Candidate_data

admin.site.register(Candidate_data, UserAdmin)
