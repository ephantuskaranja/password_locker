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
    print('genpass-for generate passwords or viewc-view saved credentials')
    access_call = input()
    if access_call == 'genpass':
        credentials.generate_password()
        print("*"*35)
        print('to continue, choose option')
        access_controller()
    elif access_call == 'viewc':
        credentials.show_generatedPass()
        print("copy credentials?:y or n")
        called = input().lower()
        if called == 'y':
            credentials.copy_credentials()
         
        else:
            print('thanks for your time.your are exiting now')
            print('*'*30)
            exit
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
        print('*'*30)
        if True:
            access_controller()
    else:
        print('incorrect credentials')



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


userdata = Userdata()


class Credentials:
    '''
    Class that generates new instances of credentials class
    '''

    def generate_password(self):
        '''
        function generating passwords
        '''
        print('input the accountFor+username to generate password.(dont space)')
        accountFor = input()
        alphabet = string.ascii_letters + string.digits
        password = ''.join(secrets.choice(alphabet) for i in range(20))
        file = open("password_keeper.txt", "a")
        file.write("\n"+ accountFor+':'+password)
        print(f"password for account {accountFor} generated")
        file.close()
    # generate_password()

    def show_generatedPass(self):   
        inputted_username = input('Please enter username:').lower()
        with open('password_keeper.txt') as f:
            for line in f:
                if inputted_username in line:
                    print(line)
    # show_generatedPass()
        
    def copy_credentials(self):
        '''
        function copies passwords for account to piperclip
        '''
        print("please specify account name to copy password:")
        name=input()
        f =  open ('password_keeper.txt', 'r')
        for line in f.readlines():
            tag, key = line.strip().split(":")
            if (name in tag) :
                key = key.strip()
                # print(key)
                pyperclip.copy(key)
                print(f"password for account {name} copied")
                return True

    # copy_credentials()
credentials = Credentials()
selector()
