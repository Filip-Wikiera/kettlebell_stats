from django.shortcuts import render
from .models import Session
from .forms import SessionFrom, MonthPicker
from datetime import datetime
from django.utils.safestring import mark_safe
from calendar import HTMLCalendar
from django.db.models import Avg, Sum, F


def index(request):
    context = {
        'welcome_message': 'Witaj w naszej aplikacji!'
    }
    return render(request, 'index.html', context)


def session(request):
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
            context = {
                'message': "Save error",
                "form": form
            }


    else:
        form = SessionFrom()
        context = {
            'message': '',
            "form": form
        }

    return render(request, "session.html", context)


def CalendarView(request):
    today = datetime.today()

    selected_month = today.month
    selected_year = today.year

    if request.method == 'POST':
        form = MonthPicker(request.POST)
        if form.is_valid():
            selected_month = int(form.cleaned_data['month'])
            selected_year = int(form.cleaned_data['year'])
    else:
        form = MonthPicker()

    events = Session.objects.filter(person=request.user, date__month=selected_month)
    events = events.filter(date__year=selected_year)

    cal = HTMLCalendar().formatmonth(selected_year, selected_month)

    for day in range(1, 32):
        cal = cal.replace(f'>{day}</td>', f'<td>{day} </td>')

    for event in events:
        id = event.date.day
        cal = cal.replace(f'>{id} ', f'<td>{id} <br>{event}')

    cal = cal.replace('<td ', '<td class="calendar-day" ')
    cal = cal.replace('<th ', '<th class="calendar-header" ')

    exercise_avg_data = events.values('exercise__name').annotate(
        # exercise_avg_data = Session.objects.values('exercise__name').annotate(

        avg_rep_count=Avg('rep_count'),
        avg_weight=Avg('weight'),
        total_reps=Sum('rep_count'),
        total_tonnage=Sum(F('rep_count') * F('weight'))
    )

    context = {
        'calendar': mark_safe(cal),
        'sessions': events,
        'form': form,
        'exercise_avg_data': exercise_avg_data
    }

    return render(request, 'calendar.html', context)


def edit_session(UpdateView):
    model = SessionFrom.Meta.model
    fields = SessionFrom.Meta.fields
    template_name = 'session.html'
    success_url = '/calendar/'
