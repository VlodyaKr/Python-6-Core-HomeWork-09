from handlers import *


COMMANDS = {'hello': salute, 'add': add_contact, 'change': change_contact, 'phone': show_phone, '?': help_me,
            'show all': show_all, 'good bye': goodbye, 'close': goodbye, 'exit': goodbye, 'help': help_me}


def main():
    contacts = {}
    while True:
        user_command = input('Enter command >>> ')
        for key in COMMANDS.keys():
            if user_command.lower().startswith(key):
                args = user_command[len(key):].split()
                result = COMMANDS[key](contacts, *args)
                if result is None:
                    print('Good bye!')
                    exit(0)
                print(result, '\n')
                break
        else:
            print('Unknown command! Enter again!\n')


if __name__ == '__main__':
    main()
