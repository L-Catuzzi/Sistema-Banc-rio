# Cadastro do cliente
class Client:
    number= 123
    def __init__(self,Name,Age,CPF,Born_data, Account_type):
        self.name = Name
        self.Age = Age
        self.CPF = CPF
        self.Born_data = Born_data
        self.Type = Account_type
        
    
    # Funcionalidades da classe
    def Describe(self):
        print(f"Name: {self.name}\nAge: {self.Age}\nBorn data: {self.Born_data}\nCPF: {self.CPF}\nAccount type: {self.Type}")
    
    

    #@classmethod # funciona com variáveis globais da classe
    
    # Standard is bronze, Silver type got some credit
    # Gold got more credit and can open more than 1 Account
    # Black type is the best, huge amount of credit and better investment options