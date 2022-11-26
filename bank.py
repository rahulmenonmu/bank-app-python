

import validationClass as vc
import re

# Global variable to keep track of unique account numbers
account_number = 1001

class account():
    def __init__(self, full_name):
        global account_number
        self.full_name = full_name
        self.__account_number =  account_number
        account_number += 1
        self.__balance = 0
        self.__depositCount = 0
        self.__withdrawCount = 0


    #Getters and Setters 

    def setBalance(self,balance):
        self.__balance = balance
    
    def getBalance(self):
        return self.__balance
    
    def getAccNumber(self):
        return self.__account_number

    def getWithdrawCount(self):
        return self.__withdrawCount
    
    def setWithdrawCount(self, value):
        self.__withdrawCount = value
    
    def getDepositCount(self):
        return self.__depositCount
    
    def setDepositCount(self, value):
        self.__depositCount = value


class bank():

    
    """
     The bank class holds all the accounts in the bank in a dictionary with the key being the account number
     and the value being the account object
    """

    def __init__(self):
        self.accounts = {}
        self.transactions = []

    
    """
    Validator Function to validate the constraints on the deposit functionality
    and raise appropriate exceptions

    @param account: account number 
    @param amount: amount to be deposited
    @return: Boolean if the validation passed
    @raise ValidationError : Error with appropriate message
    """

    def validate_deposit(self,account,amount):
        if(account.getDepositCount() == 3):
            raise vc.ValidationError('Maximum daily deposits for ' + str(account.getAccNumber()) + ' is 3')
        if(amount > 50000):
            raise vc.ValidationError('Maximum deposit amount for account ' + str(account.getAccNumber()) + ' is $50,000')
        if(amount < 500):
            raise vc.ValidationError('Minimum deposit amount for account ' + str(account.getAccNumber()) + ' is $500')
        if(account.getBalance() + amount > 100000):
            raise vc.ValidationError('Maximum Balance for ' + str(account.getAccNumber()) + ' is $100,000')
        return True

    """
    Validator Function to validate the constraints on the withdraw functionality
    and raise appropriate exceptions

    @param account: account number 
    @param amount: amount to be withrawed
    @return: Boolean if the validation passed
    @raise ValidationError : Error with appropriate message
    """

    def validate_withdrawal(self,account,amount):
        if(account.getWithdrawCount() == 3):
            raise vc.ValidationError('Maximum daily withdrawals for ' + str(account.getAccNumber()) + ' is 3')
        if(amount > 25000):
            raise vc.ValidationError('Maximum withdrawal amount for account ' + str(account.getAccNumber()) + ' is $25,000')
        if(amount < 1000):
            raise vc.ValidationError('Minimum withdrawal amount for account ' + str(account.getAccNumber()) + ' is $1000')
        if(account.getBalance() - amount < 0):
            raise vc.ValidationError('Maximum Balance for ' + str(account.getAccNumber()) + ' is $0')
        return True

    


    """
    Function to create a new account

    @param full_name: Full name of the account holder 

    @return: Account number of the newly created account
    """
    def create_account(self,full_name):
        acc = account(full_name=full_name)
        self.accounts[acc.getAccNumber()] = acc
        return acc.getAccNumber()


    """
    Function to display balance of an account

    @param account_number: Account Number 

    @return: Current balance in the account
    @raise ValidationError : Error with appropriate message
    """
    def balance(self,account_number):
        if(account_number in self.accounts):
            acc = self.accounts[account_number]
            return acc.getBalance()
        else:
            try:
                raise(vc.ValidationError('Invalid Account Number'))
            except vc.ValidationError as err:
                print(err)
                return -1


    """
    Function to perform the deposit on the supplied account number
    after carrying out necessary validation checks

    @param account_number: number of the account to be deposited into
    @param amount: amount to be deposited

    @return: Updated Balance of the account
    @raise ValidationError : Error with appropriate message
    """

    def deposit(self, account_number, amount):
        if(account_number in self.accounts):
            acc = self.accounts[account_number]
            try:
                self.validate_deposit(acc,amount)
                acc.setBalance(acc.getBalance() + amount)
                acc.setDepositCount(acc.getDepositCount() + 1)
                return acc.getBalance()
            except vc.ValidationError as err:
                print(err)
                return -1
        else:
            try:
                raise(vc.ValidationError('Invalid Account Number'))
            except vc.ValidationError as err:
                print(err)
                return -1


    """
    Function to perform the withdrawal on the supplied account number 
    after carrying out necessary validation checks

    @param account_number: number of the account to be withdrawed from
    @param amount: amount to be withdrawed

    @return: Updated Balance of the account
    @raise ValidationError : Error with appropriate message
    """

    def withdraw(self, account_number, amount):
        if(account_number in self.accounts):
            acc = self.accounts[account_number]
            try:
                self.validate_withdrawal(acc,amount)
                acc.setBalance(acc.getBalance() - amount)
                acc.setWithdrawCount(acc.getWithdrawCount() + 1)
                return acc.getBalance()
            except vc.ValidationError as err:
                print(err)
                return -1
        else:
            try:
                raise(vc.ValidationError('Invalid Account Number'))
            except vc.ValidationError as err:
                print(err)
                return -1



    """
    Function to perform the trasnfer from the source account number to the target account number
    after carrying out necessary validation checks

    @param source_account_number: number of the account to be withdrawed from
    @param target_account_number: number of the account to be deposited into
    @param amount: amount to be transferred

    @return: Boolean status of the action
    @raise ValidationError : Error with appropriate message
    """

    def transfer(self,source_acc_number, target_acc_number, amount):
        if(source_acc_number in self.accounts and target_acc_number in self.accounts):
            acc1 = self.accounts[source_acc_number]
            acc2 = self.accounts[target_acc_number]
            try:
                if(self.validate_withdrawal(acc1,amount) and self.validate_deposit(acc2,amount)):
                    self.withdraw(acc1.getAccNumber(),amount)
                    self.deposit(acc2.getAccNumber(),amount)
                    return True
            except vc.ValidationError as err:
                print(err)
                return False
        else:
            try:
                raise(vc.ValidationError('Invalid Account Number'))
            except vc.ValidationError as err:
                print(err)
                return False



# bank = bank()
# print(bank.create_account("Rahul Menon"))
# print(bank.create_account("Bhagya Nair"))
# bank.deposit(1000,500)
# bank.deposit(1001,60000)
# bank.deposit(1001,700)
# bank.deposit(1001,1000)
# bank.transfer(1001,1000,1000)
# bank.deposit(1000,1000)
# bank.deposit(1001,1000)
# bank.deposit(1001,1000)









