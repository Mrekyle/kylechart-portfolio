from django.shortcuts import render

# Create your views here.


def index(request):
    """
        Renders the home page
    """

    template = 'index.html'

    context = {

    }

    return render(request, template, context)
