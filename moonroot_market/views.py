from django.shortcuts import render
from django.http import HttpResponse


def handler404(request, exception):
    """ Error Handler 404 - Page Not Found """
    return render(request, "errors/404.html", status=404)


def google_site_verification(request):
    return HttpResponse(
        "google-site-verification: google94c9ffb3d4c799c9.html", content_type="text/html"
    )