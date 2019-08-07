import requests
import hashlib

password = input()

password_hash = hashlib.sha1(password.encode()).hexdigest().upper()

password_hash_prefix = password_hash[:5]
password_hash_root = password_hash[5:]

r = requests.get(f"https://api.pwnedpasswords.com/range/{password_hash_prefix}")
s = r.text
output = s.splitlines()

for i in output:
    if password_hash_root == i.split(':', 1)[0]:
        print(f'password {password} has been leaked')
        print('hash digest matched', i.split(':', 1)[1], 'times')
    else:
        pass
