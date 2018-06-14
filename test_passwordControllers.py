import unittest

import controllers  # module to test
import password_locker




class TestPasswordControllers(unittest.TestCase):    #TestCase class
    def setUp(self):
        print('set')
        pass
    def tearDown(self):
        print('tear')
        pass
    def test_login(self):
        print('login')
        pass
    def test_accessController(self):
        print('access')
    def test_generatePassword(self):
        print('genpass')
        pass
    def test_showGeneratedPassword(self):
        print('showgenpass')
        pass
    def test_copyCredentials(self):
        print('copyCred')
        pass
    

if __name__ == '__main__':
    unittest.main() 