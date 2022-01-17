from app.exception.wrong_type import WrongType
from app.services.json_services import read_json

def check_email_exists(path: str, new_email: str):
	user_list = read_json(path)
	
	for email in user_list:
		if new_email == email["email"]:
			return True
	
	return False

def check_type(word_to_check: str, type_request: str):
	if type(word_to_check) is str:
		return word_to_check
	
	raise WrongType(word_to_check, type_request)