
dict_phone = {}

def input_error(func):
    def inner(*args):
        try:
            return func(*args)
        except IndexError:
            return 'Not enough params. Try again'
        except ValueError:
            return 'Phon nomber is not correct. Try again'
        except KeyError:
            return r'There’s no record of that name in the phone book. Try again'
    return inner


@input_error
def add_contact(*args)->str:
    name = args[1]
    phone = args[2]
    if int(phone):
        dict_phone[name]=phone
        return f'Add {phone = } {name = }'
    
    
@input_error
def print_phone(*args)->str:
    name = args[1]
    phone_srh = dict_phone[name]
    return f"{name = } Phone number = {phone_srh}"


@input_error
def change_phon(*args)->str:
    name = args[1]
    phone = args[2]
    if int(phone):
        dict_phone[name]=phone
    return f'CHANGE {phone = } {name = }'

def helf_cla():
    return 'Command Line Interface\n'\
        'I will help you with your phone book\n'\
        'List of commands you can use:\n'\
        '\tHELLO - greeting\n'\
        '\tADD (name and phone number separated by space) - add a phonebook entry\n'\
        '\tPHONE (name) - phone search by name\n'\
        '\tCHANGE (name and new phone number separated by space) - stores the new phone number of the existing contact\n'\
        '\tSHOW ALL -displays all saved contacts with phone numbers in the console\n'\
        '\tGOOD BAY, CLOSE, EXIT - shutdown\n'\
        '\tHELP - Displays this alarm in the console\n'\
        'The bot is not sensitive to the register of commands entered\n'\
        'Success in your work!'
        
    

def main():
    print(helf_cla())
    while True:
        stp_user_input= input('<<<< ')

        list_user_input=stp_user_input.split()
        
        if list_user_input[0].lower() == 'hello':
            print('How can I help you?')
            continue
        if list_user_input[0].lower() == 'add':
            print(add_contact(*list_user_input))
            continue
        if list_user_input[0].lower() == 'show'and list_user_input[1].lower() == 'all':
            if dict_phone:
                for key, value in dict_phone.items():
                    print(f'{key = } - {value = }')
            else:
                print('Dict is empty')
            continue
        if list_user_input[0].lower() == 'phone':
            print(print_phone(*list_user_input))
            continue
        if list_user_input[0].lower() == 'help':
            print(helf_cla())
            continue
        if list_user_input[0].lower() == 'change':
            print(change_phon(*list_user_input))
            continue
        if list_user_input[0].lower() == 'close' or list_user_input[0].lower() == 'exit'or (list_user_input[0].lower() == 'good' and list_user_input[1].lower() == 'bye'):
            print('Good bye!')
            break
        #if list_user_input[0].lower() == 'good' and list_user_input[1].lower() == 'bye'

        # print(list_user_input)
        # break

if __name__ == "__main__":
     main()