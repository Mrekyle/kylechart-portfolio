from django.shortcuts import render


def handler404(request, exception):
    """
        Handles 404 page requests
    """

    template = '404.html'

    return render(request, template, status=404)
