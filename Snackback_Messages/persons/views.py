from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Person
from .forms import PersonForm
# Create your views here.
def person_list(request):
    persons = Person.objects.all()
    return render(request, 'persons/list.html', {'persons':persons})

def person_update(request, pk=None):
    print(pk)
    person_obj = get_object_or_404(Person, pk = pk)
    form = PersonForm(request.POST or None, instance=person_obj)
    if form.is_valid():
        form.save()
        messages.success(request, f'Änderungen an Person {person_obj.pk} gespeichert!')
        return redirect('list')
    return render(request, 'persons/update.html',{'form': form})