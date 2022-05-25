class UserAlreadyExists(Exception):
    """You cannot add an existing user"""


def input_error(func):
    def wrapper(contacts, *args):
        try:
            result = func(contacts, *args)
        except IndexError:
            result = 'Error! Give me name and phone please!'
        except KeyError:
            result = 'Error! User not found!'
        except ValueError:
            result = 'Error! Phone number is incorrect!'
        except UserAlreadyExists:
            result = 'Error! You cannot add an existing user'
        return result
    return wrapper


def salute(*args):
    return 'Hello! How can I help you?'


@input_error
def add_contact(contacts, *args):
    name, phone = args[0], args[1]
    if name in contacts:
        raise UserAlreadyExists
    verify_phone(phone)
    contacts[name] = phone
    return f'Added user {name}'


@input_error
def change_contact(contacts, *args):
    name, phone = args[0], args[1]
    old_phone = contacts[name]
    contacts[name] = phone
    return f'Change user {name}'


@input_error
def show_phone(contacts, *args):
    name, phone = args[0], contacts[args[0]]
    return f'User {name} - phone {phone}'


def show_all(contacts, *args):
    result = 'List of all users:'
    for name, phone in contacts.items():
        result += f'\nUser {name} - phone {phone}'
    return result


def goodbye(*args):
    return None


def verify_phone(phone: str):
    new_phone = phone.removeprefix('+').replace('(', '').replace(')', '').replace('-', '')
    return str(int(new_phone))


def help_me(*args):
    return """Command format:
    help or ? - this help;
    hello - greeting;
    add name phone - add user to directory;
    change name phone - change the user's phone number;
    phone user - show the user's phone number;
    show all - show data of all users;
    good bye or close or exit - exit the program"""
