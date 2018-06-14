import secrets
import string
import getpass
import pyperclip
import controllers


class Userdata:
    '''
    Class that generates new instances of userdata class
    '''

    def create_user(self):
        '''
        function that creates new users
        '''
        print("Please enter Username and password to register\nusername:")
        username = str(input())
        print("Enter password:")
        upass = getpass.getpass()
        udata = {username: upass}
        file = open("login.txt", "a")
        file.write("\n" + str(udata))
        file.close()
        print(f"successfully created account for {username}")
        print('want to continue? y or n')
        opt = input().lower()
        if opt == 'y':
            controllers.controllers.login()
        else:
            print('thanks for registering.you can login later')
            exit


userdata = Userdata()


class Credentials:
    '''
    Class that generates new instances of credentials class
    '''

    def generate_password(self):
        '''
        function generating passwords
        '''
        print('input the username+accountFor to generate password.(don\'t space)')
        accountFor = str(input())
        alphabet = string.ascii_letters + string.digits
        password = ''.join(secrets.choice(alphabet) for i in range(20))
        file = open("password_keeper.txt", "a")
        file.write("\n" + accountFor+':'+password)
        print(f"password for account {accountFor} generated")
        file.close()
    # generate_password()

    def show_generatedPass(self):
        inputted_username = str(input('Please enter username+accountFor:').lower())
        with open('password_keeper.txt') as f:
            for line in f:
                line2= line.split(':')
                if inputted_username in line2:
                    print(line)
                    break
            else:
                print('doesn\'t exists')
                controllers.controllers.access_controller()
    # show_generatedPass()

    def copy_credentials(self):
        '''
        function copies passwords for account to piperclip
        '''
        print("please specify account name to copy password:")
        name = str(input())
        f = open('password_keeper.txt', 'r')
        for line in f.readlines():
            tag, key = line.strip().split(":")
            if (name in tag):
                key = key.strip()
                # print(key)
                pyperclip.copy(key)
                print(f"password for account {name} copied")
        print('your now exiting...')        
        exit
    # copy_credentials()

credentials = Credentials()