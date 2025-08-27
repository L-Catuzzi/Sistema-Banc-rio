
# Cadastro do cliente
class Client:
    number= 123
    def __init__(self,Name,Age,CPF,Born_data, Account_type):
        self.Name = Name
        self.Age = Age
        self.CPF = CPF
        self.Born_data = Born_data
        self.Type = Account_type
        
    
    # Funcionalidades da classe
    def __str__(self):
        return f"Name: {self.Name}\nAge: {self.Age}\nBorn data: {self.Born_data}\nCPF: {self.CPF}\nAccount type: {self.Type}"
    

    #@classmethod # funciona com variáveis globais da classe
    
    # Standard is bronze
    # Gold got more credit and can open more than 1 Account
    # Black type is the best, huge amount of credit and better investment options

class Client_Gold(Client):
    def __init__(self, Gold_id):
        self.Id = Gold_id
    
class Client_Black(Client):
    def __init__(self, Black_id):
        self.Id = Black_id
