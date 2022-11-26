
import unittest
from bank import bank
from validationClass import ValidationError

class TestBank(unittest.TestCase):

    def setUp(self) -> None:
        self.myBank = bank()
        self.acc1 = self.myBank.create_account("Rahul Menon")
        self.acc2 = self.myBank.create_account("Bhagya Nair")

    def tearDown(self) -> None:
        pass

    def test_create_account(self):
        accNum = self.myBank.create_account("John Doe")
        self.assertIsInstance(accNum,int)

    def test_balance(self):

        # Successful balance check
        balance = self.myBank.deposit(self.acc1,10000)
        balance = self.myBank.balance(self.acc1)
        self.assertEqual(balance,10000)

        # Test invalid account number
        balance = self.myBank.balance(250)
        self.assertEqual(balance,-1)


    def test_withdrawal(self):

        ## Test successful withdrawal
        balance = self.myBank.deposit(self.acc1,1500)
        balance = self.myBank.withdraw(self.acc1,1000)
        self.assertEqual(balance,500)

        # Test max limit withdrawal 
        balance = self.myBank.withdraw(self.acc1,26000)
        self.assertEqual(balance, -1)

        # Test min limit withdrawal 
        balance = self.myBank.withdraw(self.acc1,900)
        self.assertEqual(balance, -1)

        # Test min account balance limit deposit 
        balance = self.myBank.withdraw(self.acc1,1000)
        self.assertEqual(balance,-1)
        

        # Test invalid account number
        balance = self.myBank.withdraw(250,250)
        self.assertEqual(balance,-1)

        # Test max daily limit breach deposit
        balance = self.myBank.deposit(self.acc1,2500)
        balance = self.myBank.withdraw(self.acc1,1000)
        self.assertEqual(balance,2000)
        balance = self.myBank.withdraw(self.acc1,1000)
        self.assertEqual(balance,1000)
        balance = self.myBank.withdraw(self.acc1,1000)
        self.assertEqual(balance,-1)



    def test_deposit(self):

        ## Test successful deposit
        balance = self.myBank.deposit(self.acc1,500)
        self.assertEqual(balance,500)

        # Test max limit deposit 
        balance = self.myBank.deposit(self.acc1,60000)
        self.assertEqual(balance, -1)

        # Test min limit deposit 
        balance = self.myBank.deposit(self.acc1,400)
        self.assertEqual(balance, -1)

        # Test max account balance limit deposit 
        balance = self.myBank.deposit(self.acc1,50000)
        self.assertEqual(balance,50500)
        balance = self.myBank.deposit(self.acc1,50000)
        self.assertEqual(balance, -1)

        # Test min limit deposit 
        balance = self.myBank.deposit(self.acc1,400)
        self.assertEqual(balance, -1)

        # Test invalid account number
        balance = self.myBank.deposit(250,250)
        self.assertEqual(balance,-1)

        # Test max daily limit breach deposit
        balance = self.myBank.deposit(self.acc1,500)
        self.assertEqual(balance,51000)
        balance = self.myBank.deposit(self.acc1,500)
        self.assertEqual(balance,-1)

    
    def test_transfer(self):

        self.myBank.deposit(self.acc1,1500)

        # Test successful transfer
        result = self.myBank.transfer(self.acc1,self.acc2,1000)
        self.assertEqual(result,True)

        # Test invalid account number
        result = self.myBank.transfer(250,self.acc2,1000)
        self.assertEqual(result,False)

        # Test unsuccessful transfer
        result = self.myBank.transfer(self.acc1,self.acc2,1000)
        self.assertEqual(result,False)


    def test_validation_error(self):
        err = ValidationError()
        print(err)





if __name__ == '__main__':
    unittest.main()