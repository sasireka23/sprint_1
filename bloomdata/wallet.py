class Wallet:

    #write init method

    def __init__(self,initial_amount = 0):
        self.balance = initial_amount

    
    #spend cash method

    def spend_cash(self, amount):
        if self.balance < amount:
            return "Not enough money"

        else:
            self.balance = self.balance - amount
            return f"remaining balance : ${self.balance}"

    def add_cash(self, amount):
        self.balance = self.balance + amount
        return f"new balace: ${self.balance}"

    def __repr__(self):
        return f"Wallet with balance of : ${self.balance}"

    
if __name__ == '__main__':
    wallet1 = Wallet(50)
    print(wallet1)
    print(wallet1.spend_cash(100))
    print(wallet1.add_cash(1000))
    print(wallet1.spend_cash(240))
    print(wallet1.balance)

