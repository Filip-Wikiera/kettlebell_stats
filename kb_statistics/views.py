from django.shortcuts import render
from .models import Session
from .forms import SessionFrom
from django.views.generic import UpdateView


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


def edit_session(UpdateView):
    model = SessionFrom.Meta.model
    fields = SessionFrom.Meta.fields
    template_name = 'session.html'
    success_url = '/calendar/'
