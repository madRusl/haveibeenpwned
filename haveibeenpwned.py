import requests
import hashlib
import getpass

password = getpass.getpass("Enter your password: ")

password_hash = hashlib.sha1(password.encode()).hexdigest().upper()
password_hash_prefix = password_hash[:5]
password_hash_root = password_hash[5:]

r = requests.get(f"https://api.pwnedpasswords.com/range/{password_hash_prefix}")
s = r.text
output = s.splitlines()

def hash_check():
    for i in output:
        if password_hash_root == i.split(':', 1)[0]:
            print(f'Your password \'{password}\' has been leaked')
            print('Hash digest matched', i.split(':', 1)[1], 'times')
            return True
        else:
            pass
    return False

if hash_check() is False:
    print('Password hasn\'t been leaked')

password = None
