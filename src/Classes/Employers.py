from src.Classes.Clients import Client
from src.Classes.Accounts import Bank_Account
import src.Func.Funcionalidades as Func
# Employer with ADM privileges
#  
class Employer():
    
    def __init__(self,name, RG, CPF, Employer_number, Role):
        self.name = name
        self.RG = RG
        self.CPF = CPF
        self.Number = Employer_number
        self.Role = Role

    def Promote_client(self,Client_id,Bank_Account):
        if Func.find_client(Client_id):


    def Delete_account(self, Account_id):
        

    # def Promote_client(self, Promotion_type, client_id):
    #  
