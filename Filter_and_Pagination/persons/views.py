from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Person
from .filters import PersonFilter


def show_all_persons(request):
    
    context = {}

    filtered_persons = PersonFilter(
        request.GET,
        queryset=Person.objects.all()
    )

    paginated_filtered_person = Paginator(filtered_persons.qs, 10)
    page_number = request.GET.get('page')
    person_page_obj = paginated_filtered_person.get_page(page_number)
    
    context['filtered_persons'] = filtered_persons
    context['person_page_obj'] = person_page_obj
 
    return render(request, 'persons/index.html', context)
