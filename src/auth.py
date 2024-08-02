#src/auth.py

from argon2 import PasswordHasher, exceptions

ph = PasswordHasher()

def hash_password(password):
	return ph.hash(password)

def verify_password(hashed_password, password):
	try:
		return ph.verify(hashed_password, password)
	except exceptions.VerifyMismatchError:
		return False


