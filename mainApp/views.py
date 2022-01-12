from django.shortcuts import render
from django.http import HttpResponse
from cryptography.fernet import Fernet

# Create your views here.
def homepage(request):
    return render(request, 'homepage.html')

def get_secret_link(request):
    print ("here")
    Entered_Text = request.POST.get('Entered_Text')

    #generating secret key
    key = Fernet.generate_key()

    #assigning the secret key to a variable
    fernet = Fernet(key)

    encrypted_secret = fernet.encrypt(Entered_Text.encode())

    decrypted_secret = fernet.decrypt(encrypted_secret).decode()

    components = {
        "Plain_Text": Entered_Text,
        "Key": str(key),
        "Cipher_or_Encrypted_Text":  str(encrypted_secret),
    }
    print ("Entered Text: " + Entered_Text + "\nEncrypted Text: " + str(encrypted_secret) + "\nDecrypted Text: " + decrypted_secret + "\nKey: " + str(key))
    # return HttpResponse("Secret Key: %s" %Entered_Text)
    return render(request=request, template_name="Output.html", context=components)