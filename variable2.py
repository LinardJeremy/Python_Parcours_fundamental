import unittest
 
class TestNotebook(unittest.TestCase):
 
    def test_name(self):
        self.assertEqual(name, "Alan Turing")
    
    def test_age(self):
        self.assertEqual(age, 42)
    
    def test_person(self):
        self.assertEqual(person,["Alan Turing", 42, "mathematician"])
    
    def test_text(self):
        self.assertEqual(text,"Hello, my name is Alan Turing and i am 42 years old and i am a mathematician.")
        
    def test_type(self):
        self.assertEqual(typeAge,type(int()))
    

unittest.main(argv=[''], verbosity=2, exit=False)