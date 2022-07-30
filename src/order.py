
class Order:

    def __init__(self, price, shares, expiration) -> None:


        self.price = price
        self.shares = shares
        self.expiration = expiration

    def __repr__(self) -> str:
        
        return f"Price: {self.price}, Shares: {self.shares}, Expiration: {self.expiration}"


    
    def __eq__(self, other):
        return self.price == other.price


    def __lt__(self, other):
        return self.price > other.price