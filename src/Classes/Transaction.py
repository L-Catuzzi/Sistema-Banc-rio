from datetime import datetime

class Transaction():

    def __init__(self,Quantity,Sender_id, Receiver_id):
        self.Quantity = Quantity
        self.Sender = Sender_id
        self.Receiver = Receiver_id
        self.timestamp = datetime.now()


    def __str__(self):
        data_formatada = self.timestamp.strftime("%d/%m/%Y às %H:%M:%S")
        return (f"[{data_formatada}] Transferência de R${self.Quantity:.2f} "
                f"da conta {self.Sender} para a conta {self.Receiver}")