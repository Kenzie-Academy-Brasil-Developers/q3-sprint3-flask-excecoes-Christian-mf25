from json import load, dump

def read_json(path_file: str):

	try:
		with open(path_file, "r") as file:
			return load(file)
	
	except:
		new_data = {"data": []}
		with open(path_file, "w") as file:
			dump(new_data, file, indent=2)
		return new_data


def write_json(path_file: str, new_user: str):

	try:
		all_users = read_json(path_file)["data"]
		all_users.append(new_user)
		with open(path_file, "w") as file:
			dump({"data": all_users}, file, indent=2)
		return new_user
			
	except:
		with open(path_file, "w") as file:
			dump({"data": [new_user]}, file, indent=2)
		return new_user