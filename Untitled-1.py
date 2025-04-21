import random
import string
import requests
import hashlib

def check_password_pwned(password):
    sha1_hash = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()

    first5_chars = sha1_hash[:5]
    tail = sha1_hash[5:]

    url = f"https://api.pwnedpasswords.com/range/{first5_chars}"
    response = requests.get(url)
    
    if response.status_code != 200:
        print("Error Conecting API.")
        return False
    
    if tail in response.text:
        print(f"Password {password} ain't safe")
        return True
    else:
        print(f"Password {password} is safe.")
        return False


while True:
    password = input("Give Your Password: ")
    if password:
        break
    print("Password cant be empty.")

check_password_pwned(password)
