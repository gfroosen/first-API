from django.http import HttpResponse


def index(request):
    return HttpResponse("Less is mo")
