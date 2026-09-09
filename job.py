import os

a = 2
print("coucou", a)

secret = os.getenv("SECRET_API_TOKEN")
if secret is None:
    raise RuntimeError("SECRET_API_TOKEN est absent")

print("SECRET_API_TOKEN est accessible (valeur masquée)")
