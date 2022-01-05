from cryptography.fernet import Fernet



def get_secret_link():
    encrypted_text = b'gAAAAABh1UyjCuZnAn_xLtHy65_-Ge8bsSn_8g4JIRuv6oaplufWa9N4EupcIXUKT_OR-oVTXEY2UGElH8C5QpBleg2s5NCOLQ=='
    key = b'ar5h4nlBj377Svv-WbRJToLIeIunlEQIYyJs4tSt1k8='
    print ("Key: " + str(key))
    print (type(key))
    fernet = Fernet(key)
    decrypt = fernet.decrypt(encrypted_text).decode()

    print(decrypt)

get_secret_link()