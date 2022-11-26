import bank as Bank
import re


if __name__ == '__main__':
    file = open('input.txt', 'r')
    lines = file.readlines()

    myBank = Bank.bank()

    for index, line in enumerate(lines):

        # Create
        if(re.search('^Create',line)):
            line = line.split(' ',1)
            line[1] = line[1].strip('"')
            print(myBank.create_account(line[1]))

        # Balance
        elif(re.search('^Balance',line)):
            line = line.split(' ')
            print(myBank.balance(int(line[1])))
        
        # Deposit
        elif(re.search('^Deposit',line)):
            line = line.split(' ')
            print(myBank.deposit(int(line[1]),int(line[2])))
        
        # Withdraw
        elif(re.search('^Withdraw',line)):
            line = line.split(' ')
            print(myBank.withdraw(int(line[1]),int(line[2])))
        
        # Transfer
        elif(re.search('^Transfer',line)):
            line = line.split(' ')
            res = myBank.transfer(int(line[1]),int(line[2]),int(line[3]))
            if(res):
                print("Transfer Successful")
            else:
                print(res)
                print("Transfer Failed")
        
        else:
            print("Invalid Command")

        
    file.close()