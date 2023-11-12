PHONEBOOK = {}


def input_error(func):
    def wrap(*args):
        try:
            return func(*args)
        except IndexError:
            return 'Give me name and phone please.'
    return wrap


@input_error
def add_handler(data):
    name = data[0].title()
    phone = data[1]
    PHONEBOOK[name] = phone
    return f"Contacts {name} with phone {phone} was saved"


@input_error
def change_handler(data):
    name = data[0].title()
    phone = data[1]
    if name in PHONEBOOK:
        PHONEBOOK[name] = phone
        return f"phone number for {name} was updated to {phone}"
    else:
        return f"Contact {name} does not exist"


@input_error
def phone_handler(data):
    name = data[0].title()
    if name in PHONEBOOK:
        return f"{name} phone number is {PHONEBOOK[name]}"
    else:
        return f"Contact {name} does not exist"


def exit_handler(*args):
    return 'Good bye!!!'


def hello_handler(*args):
    return 'Hello, can I help you?'


def show_all_handler(*args):
    if PHONEBOOK:
        contact = ""
        for name, phone in PHONEBOOK.items():
            contact += f"{name}: {phone}\n"
            return contact
        else:
            return 'No contact found.'


def parser(in_str):
    elements = in_str.split()
    command = elements[0].lower()
    for handler, item in COMMANDS.items():
        for cmd in item:
            if cmd.startswith(command):
                return handler(elements[1:])


COMMANDS = {
    add_handler: ['add', '+', 'додай', 'добав'],
    change_handler: ['change', 'поміняй'],
    phone_handler: ['phone'],
    show_all_handler: ['show all', 'покажи записник'],
    exit_handler: ['good bye!', 'close', 'exit'],
    hello_handler: ['hello', 'hi', 'привіт']
}


def main():
    while True:
        user_input = input('>enter you command ')
        result = parser(user_input)
        print(result)
        if result == 'Good bye!':
            break


if __name__ == '__main__':
    main()
