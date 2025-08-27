from src.Classes.Accounts import Bank_Account
from src.Classes.Employers import Employer
from src.Classes.Clients import Client, Client_Black, Client_Gold
from src.Classes.Transaction import Transaction
import src.Func.Funcionalidades as func

Clients = []
Transactions = []
Accounts = []

def main():
    Robson = Client("Robson", 32, 3522822, "19/09/1995","Bronze")
    Carlos = Client("Carlos", 29, 88393,"18/12/1999","Bronze")
    Marcos = Employer("Marcos", 4334535, 54533455, 44)
    c1 = Marcos.Create_Account(Robson,0, 7000, 453352,1000, Accounts)
    c2 = Marcos.Create_Account(Carlos, 2000, 800, 123456, 900, Accounts)
    
    
    Clients.append(Robson)
    Clients.append(Carlos)

    print("Antes: \n")
    Marcos.Check_client(Robson)
    Marcos.Delete_client(3522822,Clients, Accounts)

    Marcos.Delete_client(45,Clients, Accounts)
    
    Marcos.Delete_account(453352,Accounts)
    Marcos.Delete_client(3522822,Clients, Accounts)


    print("Depois: \n")
    Marcos.Check_client(Robson) 
    
    #Teste de Transacao

    # func.Transfer(1000, c1,c2,Transactions)

    # func.Transfer(-1000,c1,c2,Transactions)

    # func.Transfer(7000,c2,c1,Transactions)

    # func.Transfer(5000,c1,c2,Transactions)

    # Marcos.Check_account(c2)

    # func.List_transactions(Transactions)






main()