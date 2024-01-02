from django.http import HttpResponse

def home(request):
    return HttpResponse('<h3>Hello, This is Sohan</h3>');