from src.Classes.Clients import Client
from src.Classes.Accounts import Bank_Account
import src.Func.Funcionalidades as Func
# Employer with ADM privileges


class Employer():
    
    def __init__(self,name, RG, CPF, Employer_number):
        self.name = name
        self.RG = RG
        self.CPF = CPF
        self.Number = Employer_number

    def __str__(self):
        return f"Employer name: {self.name}\nId: {self.Number}"

    def Promote_client(self,Client: Client, Type):
        if Type == "Gold":
            Client.Type = Type
            print("Client promoted to gold!")
        elif Type == "Black":
            Client.Type = Type
            print("Client promoted to black!") 
        else:
            print("Invalid Type of promotion")

    def Create_Account(self,Client: Client, Balance, Limit,Acc_Number, Credit, Accounts: list[Bank_Account] )-> Bank_Account:
        Acc = Bank_Account(Client,Balance, Limit,Acc_Number, Credit)
        Accounts.append(Acc)
        return Acc

    def Delete_account(self, Account_id, Accounts: list[Bank_Account]):
        conta = Func.find_account(Account_id, Accounts)
        if not conta:
            print("Account not found\n")
        elif conta.Balance != 0:
            print(f"Account cant be deleted, there's a balance of {conta.Balance}\n")
        else:
            print(f"Account of {conta.Client_name} Deleted!\n")
            Accounts.remove(conta)
            

    def Delete_client(self, Client_id, Clients: list[Client], Accounts: list[Bank_Account]):
        C1 = Func.find_client(Client_id, Clients)
        if not C1:
            print("Client not found\n")
            return

        for Account in Accounts:
            if C1.Name == Account.Client_name:
                print("Client still has an active account and cant be deleted!\n")
                return

        Clients.remove(C1)
        print(f"Client {C1.Name} Removed\n")


    def Check_client(self, cliente: Client):
        print("**Client Informmations:**")
        print(cliente)

    def Check_account(self, account: Bank_Account):
        print("**Account Information:**")
        print(account)