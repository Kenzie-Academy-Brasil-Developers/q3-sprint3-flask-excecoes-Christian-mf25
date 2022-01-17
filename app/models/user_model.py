from app.exception.email_already_exists import EmailAlreadyExistsError
from app.exception.wrong_type import WrongType
from app.services.json_services import read_json, write_json
from app.services.user_services import check_email_exists, check_type

class User:

	file_name = "./app/database/database.json"

	def __init__(self, email: str, nome: str) -> None:
		self.email = check_type(email, "email").lower()
		self.nome = check_type(nome, "nome").title()
		self.id = len(read_json(self.file_name))
		print(email)
	
	@classmethod
	def get_users(cls):
		return read_json(cls.file_name)
	
	def create_user(self):

		new_user = self.__dict__
		if check_email_exists(self.file_name, self.email):
			raise EmailAlreadyExistsError()
		
		return write_json(self.file_name, new_user)

