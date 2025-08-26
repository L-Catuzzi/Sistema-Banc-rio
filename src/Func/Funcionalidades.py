# Some useful functions
from src.Classes.Clients import Client
from src.Classes.Accounts import Bank_Account,Transaction


def find_client(client_id, Client_list: list[Client]):
    for client in Client_list:
        if client.CPF == client_id:
            return client
        else:
            return "Client not found"
        

def find_account(Account: Bank_Account, Accounts):
    
    for Account in Accounts:
        if Account.Acc_Number == Account:
            return Account
        else:
            print("Account doesnt exist")

def Transfer(Quantity, Sender : Bank_Account, Receiver: Bank_Account):
    if Quantity > 0 and Sender.Balance >= Quantity:
        Sender.Balance -= Quantity
        Receiver.Balance += Quantity
        print("Transaction concluded")
    
def Create_account() -> Bank_Account:
    pass
