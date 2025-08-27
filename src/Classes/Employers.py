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



    def Promote_client(self,Client: Client, Type):
        if Type == "Gold":
            Client.Type = Type
            print("Client promoted to gold!")
        elif Type == "Black":
            Client.Type = Type
            print("Client promoted to black!") 
        else:
            print("Invalid Type of promotion")


    def Delete_account(self, Account_id):
        conta = Func.find_account(Account_id)


    def Delete_client(self, Client_id):
        pass

    def Check_client(self, cliente: Client):
        print("**Client Informmations:**")
        print(cliente)

    def Check_account(self, account: Bank_Account):
        print("**Account Information:**")
        print(account)