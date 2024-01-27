import getpass
import codecs

PASSWORD_FILE = 'passwd.txt'

def check_existing_username(username):
    with open(PASSWORD_FILE, 'r') as f:
        existing_usernames = [line.split(':')[0] for line in f.readlines()]
        return username in existing_usernames

def write_to_password_file(lines):
    with open(PASSWORD_FILE, 'w') as f:
        f.writelines(lines)

def add_user(username, real_name, password):
    with open(PASSWORD_FILE, 'r') as f:
        existing_usernames = [line.split(':')[0] for line in f.readlines()]

    if username in existing_usernames:
        print("Cannot add. User already exists.")
    else:
        with open(PASSWORD_FILE, 'a') as f:
            f.write(f"{username}:{real_name}:{codecs.encode(password, 'rot_13')}\n")
        print("User created.")

def delete_user(username):
    with open(PASSWORD_FILE, 'r') as f:
        lines = f.readlines()

    new_lines = [line for line in lines if not line.split(':')[0] == username]

    if len(new_lines) < len(lines):
        write_to_password_file(new_lines)
        print(f"User '{username}' deleted.")
    else:
        print(f"User '{username}' not found. Nothing changed.")


def change_password(username, current_password, new_password):
    with open(PASSWORD_FILE, 'r') as f:
        lines = f.readlines()

    found = False
    new_lines = []
    for line in lines:
        if line.startswith(f"{username}:") and line.endswith(f":{current_password}\n"):
            found = True
            new_lines.append(f"{username}:{line.split(':')[1]}:{new_password}\n")
        else:
            new_lines.append(line)

    if found:
        write_to_password_file(new_lines)
        print("Password changed.")
    else:
        print("User not found or current password is incorrect. Nothing changed.")

def login(username, password):
    with open(PASSWORD_FILE, 'r') as f:
        for line in f:
            user_info = line.strip().split(':')
            # Decode the stored password using ROT-13 for comparison
            stored_password = codecs.decode(user_info[2], "rot_13")
            if user_info[0] == username and stored_password == password:
                return True
    return False

def main():
    command = input("Enter command (adduser, deluser, passwd, login): ")

    if command == "adduser":
        username = input("Enter new username: ")
        real_name = input("Enter real name: ")

        while True:
            password = getpass.getpass("Enter password: ")
            if len(password) >= 8:
                break
            else:
                print("Password must be at least 8 characters long.")
        
        add_user(username, real_name, password)

    elif command == "deluser":
        username = input("Enter username: ")
        delete_user(username)

    elif command == "passwd":
        username = input("User: ")
        current_password = getpass.getpass("Current Password: ")
        new_password = getpass.getpass("New Password: ")
        confirm_password = getpass.getpass("Confirm: ")

        if new_password == confirm_password:
            change_password(username, current_password, new_password)
        else:
            print("Passwords do not match. Nothing changed.")

    elif command == "login":
        username = input("User: ")
        password = getpass.getpass("Password: ")

        if login(username, password):
            print("Access granted.")
        else:
            print("Access denied.")

    else:
        print("Invalid command. Please use adduser, deluser, passwd, or login.")

if __name__ == "__main__":
    main()