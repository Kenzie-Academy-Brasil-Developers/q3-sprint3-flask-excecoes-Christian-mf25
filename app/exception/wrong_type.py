class WrongType(Exception):
	code = 400

	def __init__(self, wrong: str, type_request: str) -> None:
		self.wrong = type(wrong).__name__
		self.type_request = type_request