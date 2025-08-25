from src.Classes.Clients import Client

class Bank_Account(Client):

    def __init__(self, Balance,Limit, Account_Number, Credit, Transactions_Historic):
        try:
            self.User = Client.name
            self.Balance = Balance
            self.Limit = Limit
            self.Acc_Number = Account_Number
            self.Credit = Credit
            self.Transactions = Transactions_Historic
        except (ZeroDivisionError, TypeError):
            print("Error Creating account\n")
            pass
        else:
            print("Account Created")
        
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
    
    def Balance(self):
        return self.Balance
    
    def Transfer(self, Quantity, Sender_id, Receiver_id):
        print("Transfer concluded")

    
    # @staticmethod
    # def Id_generator():
    #     rand = randint(10000,19999)
    #     return rand


class Transaction:
    def __init__(self,Quantity,Sender_id, Receiver_id):
        self.Quantity = Quantity
        self.Sender = Sender_id
        self.Receiver = Receiver_id
