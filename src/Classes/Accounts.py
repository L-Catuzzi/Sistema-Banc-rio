from src.Classes.Clients import Client

class Bank_Account():

    def __init__(self,Client: Client, Balance: float,Limit: float, Account_Number: int, Credit: float):
        self.Client_name = Client.Name
        self.Balance = Balance
        self.Limit = Limit
        self.Acc_Number = Account_Number
        self.Credit = Credit
        
    def Description(self):
        print(f"User name: {self.Client_name}\nBalance: {self.Balance}\nLimit: {self.Limit}\nAccount Number: {self.Acc_Number}\nCredit: {self.Credit}")

    def Withdraw(self,Value):
        if Value > 0:
            if self.Balance >= Value:
                self.Balance -= Value
                print("Withdraw Succeful")
            else:
                print("Balance too low")
        else:
            print("Invalid Value")
    

    def Deposit(self, Value):
        if Value >= 0:
            self.Balance += Value
        else:
            print("Invalid Value")
    
    def Balance_check(self):
        print("/*================*/\n")
        print(f"Your Balance is {self.Balance}\n")
        print("/*================*/\n")

    

class Investment_Account(Bank_Account):
    def __init__(self, ):
        pass



class Transaction:
    def __init__(self,Quantity,Sender_id, Receiver_id):
        self.Quantity = Quantity
        self.Sender = Sender_id
        self.Receiver = Receiver_id
