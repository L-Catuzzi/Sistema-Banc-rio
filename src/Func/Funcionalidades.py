# Some useful functions
from src.Classes.Clients import Client
from src.Classes.Accounts import Bank_Account,Transaction


def find_client(client_id, Client_list: list[Client]):
    for client in Client_list:
        if client.CPF == client_id:
            return client
        else:
            return "Client not found"
        

def find_account(Account_id, Accounts: list[Bank_Account]) -> Bank_Account:
    
    for Account in Accounts:
        if Account.Acc_Number == Account_id:
            return Account
        else:
            print("Account doesnt exist")

def Transfer(Quantity, Sender : Bank_Account, Receiver: Bank_Account, Transactions: list[Transaction]):
    if Quantity > 0 and Sender.Balance >= Quantity:
        Sender.Balance -= Quantity
        Receiver.Balance += Quantity
        t1 = Transaction(Quantity, Sender.Acc_Number, Receiver.Acc_Number)
        Transactions.append(t1)
        print("Transaction concluded")
    elif Quantity <= 0:
        print("Invalid Value")
    else:
        print("Insuficient balance")
    



def List_transactions(Transactions: list[Transaction]):
    print("=========\nLista de Transacoes")
    
    for transaction in Transactions:
        print(transaction)

    print("=========")
