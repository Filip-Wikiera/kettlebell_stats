from django.shortcuts import render
from .forms import SessionFrom


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
