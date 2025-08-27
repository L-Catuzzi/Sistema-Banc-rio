from src.Classes.Accounts import Bank_Account
from src.Classes.Employers import Employer
from src.Classes.Clients import Client, Client_Black, Client_Gold
import src.Func.Funcionalidades as func

Clients = []
Transactions = []
Accounts = []

def main():
    Robson = Client("Robson", 32, 3522822, "19/09/1995","Bronze")
    Carlos = Client("Carlos", 29, 88393,"18/12/1999","Bronze")
    c1 = Bank_Account(Robson,10000, 7000, 453352, 1000)
    c2 = Bank_Account(Carlos, 2000, 800, 123456, 900)

    Marcos = Employer("Marcos", 4334535, 54533455, 44)


    Accounts.append(c1)
    Accounts.append(c2)
    Marcos.Check_account(c1)




    # func.Transfer(1000,c1,c2)
    # print(Robson)
    # Robson.Describe()

    # c1.Withdraw(2000)

    # c1.Balance_check()

    # c1.Deposit(50000)

    # c1.Balance_check()




main()