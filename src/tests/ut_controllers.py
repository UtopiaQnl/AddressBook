import unittest

if "CORRECT_PATH" not in vars():
    import sys
    import os

    CORRECT_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    sys.path.append(CORRECT_PATH)

from controllers.MenuController import is_valid_user_request, get_new_state_from_request
from supportive.State import State


class TestMenuControllers(unittest.TestCase):

    def test_valid_user_request_digit(self):
        self.assertEqual(is_valid_user_request('-1'), True)
        self.assertEqual(is_valid_user_request('-2'), True)
        self.assertEqual(is_valid_user_request('-3'), True)
        self.assertEqual(is_valid_user_request('-4'), True)
        self.assertEqual(is_valid_user_request('-5'), True)
        self.assertEqual(is_valid_user_request('-6'), True)
        self.assertEqual(is_valid_user_request('-7'), True)
        self.assertEqual(is_valid_user_request('-8'), True)
        self.assertEqual(is_valid_user_request('-9'), True)

        self.assertEqual(is_valid_user_request('0'), True)
        self.assertEqual(is_valid_user_request('1'), True)
        self.assertEqual(is_valid_user_request('2'), True)
        self.assertEqual(is_valid_user_request('3'), True)
        self.assertEqual(is_valid_user_request('4'), True)
        self.assertEqual(is_valid_user_request('5'), True)
        self.assertEqual(is_valid_user_request('6'), True)
        self.assertEqual(is_valid_user_request('7'), True)
        self.assertEqual(is_valid_user_request('8'), True)
        self.assertEqual(is_valid_user_request('9'), True)

    def test_no_valid_user_request_digit(self):
        self.assertEqual(is_valid_user_request('1234'), False)
        self.assertEqual(is_valid_user_request('134'), False)
        self.assertEqual(is_valid_user_request('34'), False)
        self.assertEqual(is_valid_user_request('-034'), False)
        self.assertEqual(is_valid_user_request('-34'), False)
        self.assertEqual(is_valid_user_request('1234'), False)
        self.assertEqual(is_valid_user_request('12340'), False)
        self.assertEqual(is_valid_user_request('010'), False)
        self.assertEqual(is_valid_user_request('00'), False)

        self.assertEqual(is_valid_user_request('slkdjf'), False)
        self.assertEqual(is_valid_user_request(':@#$%'), False)
        self.assertEqual(is_valid_user_request('234:234'), False)
        self.assertEqual(is_valid_user_request(''), False)
        self.assertEqual(is_valid_user_request('-'), False)

        self.assertEqual(is_valid_user_request('2.1'), False)
        self.assertEqual(is_valid_user_request('-1.0'), False)
        self.assertEqual(is_valid_user_request('0.34'), False)
        self.assertEqual(is_valid_user_request('12.2'), False)

    def test_valid_user_request_str_exit(self):
        self.assertEqual(is_valid_user_request('ex'), True)
        self.assertEqual(is_valid_user_request('e'), True)
        self.assertEqual(is_valid_user_request('exit'), True)

    def test_valid_user_request_str_show(self):
        self.assertEqual(is_valid_user_request('show'), True)
        self.assertEqual(is_valid_user_request('s'), True)
        self.assertEqual(is_valid_user_request('sh'), True)

    def test_no_valid_user_request_str(self):
        self.assertEqual(is_valid_user_request('exxit'), False)
        self.assertEqual(is_valid_user_request('eit'), False)
        self.assertEqual(is_valid_user_request('et'), False)
        self.assertEqual(is_valid_user_request('exxitt'), False)
        self.assertEqual(is_valid_user_request('exiit'), False)
        self.assertEqual(is_valid_user_request('ext'), False)
        self.assertEqual(is_valid_user_request('shows'), False)
        self.assertEqual(is_valid_user_request('sho'), False)
        self.assertEqual(is_valid_user_request('sow'), False)
        self.assertEqual(is_valid_user_request('how'), False)
        self.assertEqual(is_valid_user_request('shos'), False)


class TestMenuControllers2(unittest.TestCase):

    def test_get_state(self):
        self.assertEqual(get_new_state_from_request('0'), State.EXIT)
        self.assertEqual(get_new_state_from_request('exit'), State.EXIT)
        self.assertEqual(get_new_state_from_request('ex'), State.EXIT)
        self.assertEqual(get_new_state_from_request('e'), State.EXIT)

        self.assertEqual(get_new_state_from_request('1'), State.ADD)
        self.assertEqual(get_new_state_from_request('2'), State.SHOW)

        self.assertEqual(get_new_state_from_request('5'), State.INIT)
        self.assertEqual(get_new_state_from_request('9'), State.INIT)
        self.assertEqual(get_new_state_from_request('-2'), State.INIT)
        self.assertEqual(get_new_state_from_request('-3'), State.INIT)
        self.assertEqual(get_new_state_from_request('-4'), State.INIT)
        self.assertEqual(get_new_state_from_request('-5'), State.INIT)


if __name__ == "__main__":
    unittest.main()
