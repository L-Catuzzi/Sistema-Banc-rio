from datetime import datetime

class Transacao:
    def __init__(self, valor: float, remetente_num: int, destinatario_num: int):
        self.valor = valor
        self.remetente_num = remetente_num
        self.destinatario_num = destinatario_num
        self.timestamp = datetime.now()


    def __str__(self):
        data_formatada = self.timestamp.strftime("%d/%m/%Y às %H:%M:%S")
        return (f"[{data_formatada}] Transferência de R${self.valor:.2f} "
                f"da conta {self.remetente_num} para a conta {self.destinatario_num}")