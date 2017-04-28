from coin_machine import CoinMachine
import unittest

# To Do:
# Write code here that will test the CoinMachine

# Need a hint?  Post a public question on Piazza.

class CointMachineTest(unittest.TestCase):
    
    def test_initializing_machine(self):
        machine = CoinMachine(0, 0, 0, 0)
        self.assertEqual({  "quarter": 0, "dime": 0,
                            "nickel": 0, "penny": 0 }, machine.coinCount)
    
    def test_getChange_without_enough_change(self):
        machine = CoinMachine(0, 0, 0, 0)
        self.assertEqual("ERROR", machine.getChange(10))
    
    def test_getChange_with_enough_change(self):
        machine = CoinMachine(10, 10, 10, 10)
        self.assertEqual([['quarter', 1], ['dime', 0], ['nickel', 0], ['penny', 0]], machine.getChange(25))
    
    def test_getChange_requiring_switching_coin_count(self):
        machine = CoinMachine(1, 50, 50, 50)
        self.assertEqual([['quarter', 1], ['dime', 2], ['nickel', 1], ['penny', 0]], machine.getChange(50))
    
    def test_getChange_in_all_pennies(self):
        machine = CoinMachine(0, 0, 0, 100)
        self.assertEqual([['quarter', 0], ['dime', 0], ['nickel', 0], ['penny', 99]], machine.getChange(99))

if __name__ == '__main__':
    unittest.main()