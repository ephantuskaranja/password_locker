import secrets
import string
import getpass
import pyperclip


def selector():
    '''
    function that controls the flow of the application
    '''
    print('please use the codes below to continue:')
    print("log-for registered users\n", "\nnew-for new user\n")
    selector_call = input()
    if selector_call == "new":
        userdata.create_user()
        # selector()
    elif selector_call == "log":
        login()
    else:
        print("illegal code input")
        selector()


def access_controller():
    '''
    Gives options after login function is True
    '''
    print('genpass-for generate passwords or viewc-view credentials')
    access_call = input()
    if access_call == 'genpass':
        credentials.generate_password()
        print('generated new password')
    elif access_call == 'viewc':
        credentials.show_generatedPass()
    else:
        print('illegal input')


def login():
    '''
    function that enables access to the system
    '''
    print('Logging in........')
    username = input('Please enter username: ')
    upass = getpass.getpass('Please enter password: ')
    udata = {username: upass}
    if str(udata) in open('login.txt').read():
        # print("true")
        print(f'correct credentials: Your are now logged in as {username}')
        if True:
            access_controller()
    else:
        print('incorrect credentials')

def copy_credentials():
    print("please specify account name to copy password:")
    name=input()
    if name in open('password_keeper.txt').read():
        pyperclip.copy()



class Userdata:
    '''
    Class that generates new instances of userdata class
    '''

    def create_user(self):
        '''
        function that creates new users
        '''
        print("Please enter Username and password to register\nusername:")
        username = input()
        print("Enter password:")
        upass = getpass.getpass()
        udata = {username: upass}
        file = open("login.txt", "a")
        file.write("\n" + str(udata))
        file.close()
        print(f"{username} created")
    # login()


# userdata = Userdata()


# class Credentials:
#     '''
#     Class that generates new instances of credentials class
#     '''

#     def generate_password(self):
#         '''
#         function generating passwords
#         '''
#         print('input the account to generate for')
#         accountFor = input()
#         alphabet = string.ascii_letters + string.digits
#         password = ''.join(secrets.choice(alphabet) for i in range(20))
#         file = open("password_keeper.txt", "a")
#         file.write("\n"+password + '-'+accountFor)
#         file.close()
#     # generate_password()

#     def show_generatedPass(self):
#         f = open('password_keeper.txt', 'r')
#         if f.mode == 'r':
#             contents = f.read()
#             print(contents)


# credentials = Credentials()
# selector()
