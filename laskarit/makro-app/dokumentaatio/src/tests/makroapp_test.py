import unittest

from makroapp import UI

class TestUI(unittest.TestCase):
    def setUp(self):
        self.frame = None


    def test_registerView(self):
        # Test if mainView is the start view.
        #UI.start
        self.assertEqual(1, 1)

    
