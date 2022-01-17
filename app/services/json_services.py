from json import load, dump


def read_json(path_file: str):
    try:
        with open(path_file, "r") as file:
            return load(file)

    except:
        return []


def write_json(path_file: str, new_user: str):
    all_users = read_json(path_file)
    all_users.append(new_user)
    with open(path_file, "w") as file:
        dump(all_users, file, indent=2)
    return new_user

