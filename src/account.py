
from order import Order


class Account:


    def __init__(self, allocation) -> None:
        
        self.allocation = allocation

        self.shares_owned = 0
        self.amount_invested = 0
        self.balance = 0

        self.order_counts = {
            "MARKET": 0,
            "LIMIT": 0,
            "DIVIDEND": 0
        }

        self.orders : list[Order] = [] 

    def __repr__(self) -> str:
        shares_owned = f"Shares Owned: {self.shares_owned}\n"
        amount_invested = f"Amount Invested: {self.amount_invested}\n"
        pps = f"Price per Share: {self.amount_invested / self.shares_owned}\n"
        orders_left = f"Orders left: {len(self.orders)}\n"

        order_types = f"Order Counts: {self.order_counts}"
        
        return shares_owned + amount_invested + pps + orders_left + order_types



    def invest_dividend(self, amount_per_share, share_price):

        #just adding to shares owned based on dividend

        full_dividend_value = amount_per_share * self.shares_owned

        free_shares = full_dividend_value / share_price

        self.shares_owned += free_shares
        if free_shares > 0:
            self.order_counts["DIVIDEND"] += 1
            #print(f"Trade Made --- Type: Dividend - Price: {share_price} - Shares: {free_shares} - Amount: {full_dividend_value}")

        return

    def execute_available_orders(self, low_price, day):

        index = 0

        while True:

            if index >= len(self.orders):
                break

            order = self.orders[index]

            if order.expiration < day:
                self.orders.pop(index)
                amount_invest = order.shares * order.price
                self.balance += amount_invest

            elif order.price < low_price:
                index += 1
            else:

                shares = order.shares
                price = order.price

                amount_invest = shares * price

                self.shares_owned += shares
                self.amount_invested += amount_invest

                self.orders.pop(index)

                if shares > 0:
                    self.order_counts["LIMIT"] += 1
                    #print(f"Trade Made --- Type: Limit - Price: {price} - Shares: {shares} - Amount: {amount_invest}")





    def invest_allocation(self, amount, price, limit_expiration):

        self.balance += amount

        total_amount_investing = self.balance

        for (key, value ) in self.allocation.items():

            invest_amount = value * total_amount_investing
            purchase_price = key * price

            shares_buying = invest_amount / purchase_price


            self.balance -= invest_amount


            if key == 1:
                self.shares_owned += shares_buying
                self.amount_invested += invest_amount
                self.order_counts["MARKET"] += 1
               # print(f"Trade Made --- Type: Market - Price: {purchase_price} - Shares: {shares_buying} - Amount: {invest_amount}")
            else:
                new_order = Order(purchase_price, shares_buying, limit_expiration)
                self.orders.append(new_order)

    def get_account_value(self, share_price):
        return self.shares_owned * share_price


        