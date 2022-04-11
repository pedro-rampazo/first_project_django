from django.shortcuts import render
from user_data_viewer.models import Person

# Create your views here.
def index(request):
    """View function for home page of site."""
    num_persons = Person.objects.all().count()
    name_persons = Person.objects.name

    context = {'num_persons': num_persons, 'name_persons': name_persons}

    return render(request, 'index.html', context=context)
