import secrets
import string
import getpass


class Credentials:
    '''
    Class that generates new instances of credentials class
    '''

    def __init__(self, password):
        self.password = password

    def generate_password():
        '''
        function generaring passwords
        '''
        alphabet = string.ascii_letters + string.digits
        password = ''.join(secrets.choice(alphabet) for i in range(20))
        file = open("password_keeper.txt", "a")
        file.write("\n"+password)
        file.close()
        # print(password)
    # generate_password()

class Userdata:
    '''
    Class that generates new instances of userdata class
    '''
    def __init__(self, username,upass):
        self.username = username
        self.upass = upass
    def create_user():
        print("Please enter Username and password to register\nusername:")
        username=input()
        print("Enter password:")
        upass= getpass.getpass()
        print("You entered:\n" +username +"\n" +upass)
    create_user()

