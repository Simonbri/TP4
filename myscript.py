import os

good_hash = os.getenv("GOOD_HASH")
bad_hash = os.getenv("BAD_HASH")

os.system(f"git bisect start {bad_hash} {good_hash}")
os.system("git bisect run python manage.py test")
os.system("git bisect reset")