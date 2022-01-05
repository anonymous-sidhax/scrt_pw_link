from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def homepage(request):
    return render(request, 'homepage.html')

def get_secret_link(request):
    secret_key = request.POST.get('secret_key')
    return HttpResponse("Secret Key: %s" %secret_key)