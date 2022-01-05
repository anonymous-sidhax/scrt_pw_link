from django.shortcuts import render
from django.http import HttpResponse

from cryptography.fernet import Fernet

# Create your views here.
def homepage(request):
    return render(request, 'homepage.html')

def get_secret_link(request):
    secret_key = request.POST.get('secret_key')

    key = Fernet.generate_key()
    fernet = Fernet(key)

    encrypted_secret = fernet.encrypt(secret_key.encode())

    decrypted_secret = fernet.decrypt(encrypted_secret).decode()
    print ("Secret Key: " + secret_key + "\nEncrypted Text: " + str(encrypted_secret) + "\nDecrypted Text: " + decrypted_secret + "\nKey: " + str(key))
    return HttpResponse("Secret Key: %s" %secret_key)