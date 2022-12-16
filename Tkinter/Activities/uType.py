class uType:
    def __init__(self,customer, bank, acnt, limit):
        self.Acustomer = customer
        self.Abank = bank
        self.Aacnt = acnt
        self.Alimit = limit
        self.balance = 0
        self.price = 0
    def getAcustomer(self):
        return self.Acustomer
    def getAbank(self):
        return self.Abank
    def getAacnt(self):
        return self.Aacnt
    def getAlimit(self):
        return self.Alimit
    def getbalance(self):
        return self.balance
    def charge(self):
        return self.price