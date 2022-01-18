class EmailAlreadyExistsError(Exception):
	message = "User already exists."
	code = 409