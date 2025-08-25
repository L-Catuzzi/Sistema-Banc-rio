# Some useful functions
from src.Classes.Clients import Client



def find_client(client_id, clients):
    for user in clients:
        if user.CPF == client_id:
            return user
        else:
            return "Client not found"
        

def find_account(Account_id, Accounts):
    for Account in Accounts:
        if Account_id == Account:
            return Account
        else:
            print("Account doesnt exist")