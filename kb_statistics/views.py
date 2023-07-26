from django.shortcuts import render
from .models import Session
from .forms import SessionFrom
from .classes.EventCalendar import EventCalendar
from datetime import datetime
from django.utils.safestring import mark_safe
from calendar import HTMLCalendar


def index(request):
    context = {
        'welcome_message': 'Witaj w naszej aplikacji!'
    }
    return render(request, 'index.html', context)


def session(request):
    context = {
        'message': '',
        'form': SessionFrom()
    }
    if request.method == "POST":
        form = SessionFrom(request.POST)
        if form.is_valid():
            form.instance.person = request.user
            form.save()
            context = {
                'message': 'Session added!',
                "form": form
            }
            return render(request, 'session.html', context)

    else:
        form = SessionFrom()
        context = {
            'message': '',
            "form": form
        }

    return render(request, "session.html", context)


def CalendarView(request):
    today = datetime.today()
    events = Session.objects.filter(person=request.user, date__month=today.month)

    cal = HTMLCalendar().formatmonth(today.year, today.month)

    for day in range(1, 32):
        cal = cal.replace(f'>{day}</td>', f'<td>{day} </td>')

    for event in events:
        id = event.date.day
        cal = cal.replace(f'>{id} ', f'<td>{id} <br>{event}')

    cal = cal.replace('<td ', '<td class="calendar-day" ')
    cal = cal.replace('<th ', '<th class="calendar-header" ')

    context = {
        'calendar': mark_safe(cal),
        'sessions': events
    }

    return render(request, 'calendar.html', context)


def edit_session(UpdateView):
    model = SessionFrom.Meta.model
    fields = SessionFrom.Meta.fields
    template_name = 'session.html'
    success_url = '/calendar/'
