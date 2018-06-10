import secrets
import string
import getpass


def selector():
    '''
    function that controls the flow of the application
    '''
    print('please use the codes below to continue:')
    print("log-for registered users\n", "\nnew-for new user\n",
          "\ngenPass-for generate passwords\n", "\nviewc-view credentials")
    code_selected = input("code_selected: ")
    if code_selected == "new":
        userdata.create_user()
        selector()
    elif code_selected == "log":
        login()
        selector()
    elif code_selected == "viewc":
        login()
        # selector()
        credentials.show_generatedPass()
    else:
        print("illegal code input")
        selector()


def login():
    '''
    function that enables access to the system
    '''
    print('Logging in........')
    username = input('Please enter username: ')
    upass = getpass.getpass('Please enter password: ')
    udata = {username: upass}
    f = open('login.txt', 'r')
    my_data = eval(f.read())
    if my_data == udata:
        print('correct credentials: Your are now logged in')
        return True
    else:
        print('incorrect credentials')
        return False


class Userdata(object):
    '''
    Class that generates new instances of userdata class
    '''

    # def __init__(self, username, upass, udata):
    #     self.username = username
    #     self.upass = upass
    #     self.udata = udata

    def create_user(self):
        '''
        function that creates new users
        '''
        print("Please enter Username and password to register\nusername:")
        username = input()
        print("Enter password:")
        upass = getpass.getpass()
        udata = {username: upass}
        file = open("userdata.txt", "a")
        file.write("\n" + str(udata))
        file.close()


userdata = Userdata()


class Credentials:
    '''
    Class that generates new instances of credentials class
    '''

    # def __init__(self, password):
    #     self.password = password

    def generate_password(self, password):
        '''
        function generating passwords
        '''
        alphabet = string.ascii_letters + string.digits
        password = ''.join(secrets.choice(alphabet) for i in range(20))
        file = open("password_keeper.txt", "a")
        file.write("\n"+password)
        file.close()
        # return(alphabet, password)
    # generate_password()

    def show_generatedPass(self):
        if login()==True:
            f = open('password_keeper.txt', 'r')
            if f.mode == 'r':
                contents = f.read()
                print(contents)


credentials = Credentials()
selector()
