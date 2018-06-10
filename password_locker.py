import secrets
import string
import getpass


def login():
    print('Logging in........')
    username = input('Please enter username: ')
    upass = getpass.getpass('Please enter password: ')
    udata = {username: upass}
    print(udata)
    f = open('userdata.txt', 'r')
    my_dict = eval(f.read())
    print(my_dict)
        # if my_data == udata:
        #     print('correct credentials')
        #     return True
        # else:
        #     print('incorrect credentials')
        #     return False
login()


# class Userdata:
#     '''
#     Class that generates new instances of userdata class
#     '''

#     def __init__(self, username, upass, udata):
#         self.username = username
#         self.upass = upass
#         self.udata = udata

#     def create_user():
#         print("Please enter Username and password to register\nusername:")
#         username = input()
#         print("Enter password:")
#         upass = getpass.getpass()
#         udata = {username: upass}
#         file = open("userdata.txt", "a")
#         file.write("\n" + str(udata))
#         file.close()

#     def datacheck():
#         existing = {'ephantus': 'karanja'}
#         print("Please Enter username and then password")
#         username_inputted = input()
#         password_inputted = getpass.getpass()
#         udata = {username_inputted: password_inputted}
#         if (udata == existing):
#             print("login successful")
#         else:
#             print("Please register")
    




# class Credentials:
#     '''
#     Class that generates new instances of credentials class
#     '''

#     def __init__(self, password):
#         self.password = password

#     def generate_password():
#         '''
#         function generating passwords
#         '''
#         alphabet = string.ascii_letters + string.digits
#         password = ''.join(secrets.choice(alphabet) for i in range(20))
#         file = open("password_keeper.txt", "a")
#         file.write("\n"+password)
#         file.close()
#         return(alphabet, password)
#     # generate_password()

