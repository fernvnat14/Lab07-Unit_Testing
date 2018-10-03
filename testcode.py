import code
import unittest



class TestCode(unittest.TestCase):
   def test_login(self):
       self.assertEqual(code.check_login(code.username,code.password),'Passed')
       self.assertEqual(code.check_login('Fern','1234'),'Passed')
   def test_password(self):
       self.assertEqual(code.check_login('Fern','000333'),'Incorrect password')
   def test_username(self):
       self.assertEqual(code.check_login('Fernnaja','1234'),'Incorrect username')
                     
if __name__ == '__main__':
   unittest.main()
