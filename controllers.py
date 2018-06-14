import secrets
import string
import getpass
import pyperclip
import password_locker


class Controllers():
    def selector(self):
        '''
        function that controls the flow of the application
        '''
        print('please use the codes below to continue:')
        print("log-for registered users\n", "\nnew-for new user\n")
        selector_call = input()
        if selector_call == "new":
           password_locker.userdata.create_user()
            # selector()
        elif selector_call == "log":
            controllers.login()
        else:
            print("illegal code input")
            controllers.selector()


    def access_controller(self):
        '''
        Gives options after login function is True
        '''
        print('genpass-for generate passwords or viewc-view saved credentials')
        access_call = input()
        if access_call == 'genpass':
            password_locker.credentials.generate_password()
            print("*"*35)
            print('to continue, choose option')
            controllers.access_controller()
        elif access_call == 'viewc':
            password_locker.credentials.show_generatedPass()
            print("copy credentials?:y or n")
            called = input().lower()
            if called == 'y':
               password_locker.credentials.copy_credentials()

            else:
                print('thanks for your time.your are now exiting')
                print('*'*30)
                exit
        else:
            print('illegal input')


    def login(self):
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
              controllers.access_controller()
        else:
            print('incorrect credentials')

controllers= Controllers()