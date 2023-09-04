from .forms import *
from django.core.paginator import Paginator
from django.db.models import Q, Value
from django.db.models.functions import Concat


def get_persons(request, order_by, /):
    term = request.GET.get('term')
    if term:
        field = Concat('first_name', Value(' '), 'last_name')
        list_persons = Person.objects.annotate(
            complete_name=field
        ).filter(
            Q(complete_name__icontains=term)
        )
    else:
        list_persons = Person.objects.all().order_by(order_by)
    paginator = Paginator(list_persons, 4)
    page_num = request.GET.get('page')
    persons = paginator.get_page(page_num)
    return persons


def get_emphasis(person_id):
    person = Person.objects.all()
    if person_id is None or not person_id:
        return person.order_by('-updated').first()
    else:
        return person.get(id=person_id)


def get_context(request, order_by='-created', person_id=None):
    return {
        'form': FormPerson(),
        'persons': get_persons(request, order_by),
        'emphasis': get_emphasis(person_id)
    }
