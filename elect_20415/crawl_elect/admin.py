from django.contrib import admin
from .models import Candidate, Precinct
# Register your models here.

class PrecinctAdmin(admin.ModelAdmin):
    model = Precinct
    search_fields = ['sigun', 'admin_location']

admin.site.register(Candidate)
admin.site.register(Precinct, PrecinctAdmin)

