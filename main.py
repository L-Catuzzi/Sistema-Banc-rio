from src.Classes.Accounts import Bank_Account
from src.Classes.Clients import Client
import src.Func.Funcionalidades as Func

Clients = []

def main():
    Robson = Client("Robson", 32, 3522822, "19/09/1995","Bronze")
    Carlos = Client("Carlos", 29, 88393,"18/12/1999","Bronze")
    c1 = Bank_Account(Robson,10000, 7000, 453352, 1000)
    c2 = Bank_Account(Carlos, 2000, 800, 123456, 900)

    Clients.append(Robson)
    Clients.append(Carlos)

    print(Clients)


    # Robson.Describe()
    # c1.Description()

    # c1.Withdraw(2000)

    # c1.Balance_check()

    # c1.Deposit(50000)

    # c1.Balance_check()






main()