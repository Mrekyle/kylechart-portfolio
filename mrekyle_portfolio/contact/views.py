from django.shortcuts import render


# Create your views here.

def contact(request):
    """
        Handles the contact form
    """

    template = 'contact.html'

    context = {

    }

    return render(request, template, context)
