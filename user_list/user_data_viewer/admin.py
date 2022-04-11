from django.contrib import admin
from user_data_viewer.models import Person

# Register your models here.
#admin.site.register(Person)

class PersonAdmin(admin.ModelAdmin):
    list_display = ('name', 'last_name', 'age')

admin.site.register(Person, PersonAdmin)
