# Cadastro do cliente
class cliente:

    def _init_(self,Name,Age,CPF,RG,Born_data, Account_type):
        self.name = Name
        self.Age = Age
        self.CPF = CPF
        self.RG = RG
        self.Born_data = Born_data
        self.Type = Account_type

    
    # Funcionalidades da classe
    def Describe(self):
        print(f"Nome: {self.name}\n")
    
    #def Delete_client(self):
    
    # Standard is bronze, Silver type got some credit
    # Gold got more credit and can open more than 1 Account
    # Black type is the best, huge amount of credit and better investment options
    def Promote_client(self, Promotion_type):
        self.Type = Promotion_type



class Bank_Account(cliente):

    def __init__(self, Balance, Account_Number, Credit_elegibility, Credit, ):
        try:
            self.Balance = Balance
        except (ZeroDivisionError, TypeError):
            print("Error Creating account\n")
            pass
        else:
            print("Account Created")
    


# Employer with ADM privileges 
class Employer():

    def __init__(self,name ):
        self.name = name