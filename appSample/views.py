from django.shortcuts import render, redirect, get_object_or_404
from .functions import *


# Create your views here.
def index(request):
    return render(request, 'content/index.html', get_context(request))


def save(request):
    if request.method == 'POST':
        form = FormPerson(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    return redirect('appSample:index')


def up_name(request, person_id):
    person = get_object_or_404(Person, id=person_id)
    person.first_name = request.POST.get('first_name')
    person.last_name = request.POST.get('last_name')
    person.save()
    return redirect('appSample:index')


def up_birth(request, person_id):
    person = get_object_or_404(Person, id=person_id)
    person.birth = request.POST.get('birth')
    person.save()
    return redirect('appSample:index')


def up_photo(request, person_id):
    person = get_object_or_404(Person, id=person_id)
    person.photo = request.FILES.get('photo')
    person.save()
    return redirect('appSample:index')


def order_filter(request, order_by):
    return render(request, 'content/index.html', get_context(request, order_by=order_by))


def emphasis(request, person_id):
    return render(request, 'content/index.html', get_context(request, person_id=person_id))


def delete(request, person_id):
    Person.objects.get(id=person_id).delete()
    return redirect('appSample:index')
