from unicodedata import name
from django.shortcuts import render
from user_data_viewer.models import Person
from django.views import generic

# Create your views here.
def index(request):
    num_persons = Person.objects.all().count()
    context={'num_persons': num_persons}

    return render(request, 'index.html', context=context)


class PersonListView(generic.ListView):
    model = Person
