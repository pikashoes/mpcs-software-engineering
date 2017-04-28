# -*- coding: utf-8 -*-
"""
@author: pikashoes
I go in order of the actions required for the TDD.
"""
from ticketing import MaroonAirShell
import unittest

class TicketTest(unittest.TestCase):
    
    """ Customer Tests"""    
    def test_look_up_nonexisting_customer(self):
        self.shell = MaroonAirShell()
        self.assertEqual(None, self.shell.do_customer_lookup(00000))
    
    def test_add_customer(self):
        self.shell = MaroonAirShell()
        self.assertEqual(None, self.shell.do_customer_add("Susie Yi"))
    
    def test_add_customer_missing_lname(self):
        self.shell = MaroonAirShell()
        self.assertEqual(None, self.shell.do_customer_add("Susie"))

    def test_look_up_existing_customer(self):
        self.shell = MaroonAirShell()
        self.assertEqual(None, self.shell.do_customer_lookup(12345))

    """ Reservation Tests """
    def test_look_up_reservation(self):
        self.shell = MaroonAirShell()
        self.assertEqual(None, self.shell.do_reservation_lookup("294"))
    
    """ Credit Card Tests """
    def test_cc_wrong_length(self):
        self.shell = MaroonAirShell()
        self.assertEqual(False, self.shell.check_credit_card(3412442))
    
    def test_cc_wrong_cardtype(self):
        self.shell = MaroonAirShell()
        self.assertEqual(False, self.shell.check_credit_card(143423))
    
    def test_cc_wrong_sum(self):
        self.shell = MaroonAirShell()
        self.assertEqual(False, self.shell.check_credit_card(422171))
    
    def test_cc_correct_sum(self):
        self.shell = MaroonAirShell()
        self.assertEqual(True, self.shell.check_credit_card(422161))

if __name__ == '__main__':
    unittest.main()