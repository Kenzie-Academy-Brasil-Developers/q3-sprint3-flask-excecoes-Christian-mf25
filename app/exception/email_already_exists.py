from distutils.log import error
from email import message


class EmailAlreadyExistsError(Exception):
	message = "User already exists."
	code = 409