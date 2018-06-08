import secrets
import string


class Credentials:
    '''
    Class that generates new instances of credentials class
    '''
    password_list = []

    def __init__(self, password):
        self.password = password

    def generate_password():
        '''
        function generaring passwords
        '''
        alphabet = string.ascii_letters + string.digits
        password = ''.join(secrets.choice(alphabet) for i in range(20))
        
        # print(password)
    generate_password()

