
from utils import load_data
from account import Account

parameters = {
    1: 1,
    0.925: 0,

}

d = 20 # number of trading days between each additional investment
x = 1000 # number of dollars to add on trading days
limit_expiration_days = 20

stock = "AAPL"

period = "5y"


data = load_data(stock, period)

account = Account(parameters)


day = 0

for stock_info in data:

    open = stock_info.get("open")
    high = stock_info.get("high")
    low = stock_info.get("low")
    close = stock_info.get("close")
    dividend = stock_info.get("dividend")

    # Check for dividends, if so add to account
    #dividends are reinvested at the open price

    account.invest_dividend(dividend, open)


    # execute all valid limit orders

    account.execute_available_orders(low, day)

    # if it's a trade day, make trades based on the allocation

    if day % d == 0:
        account.invest_allocation(x, close, day+limit_expiration_days)

    day += 1

    if day == len(data):
        print(f"Account Value: {account.get_account_value(close)}")
        print(f"Account Return: {round(100*((account.get_account_value(close) / account.amount_invested)-1), 2)}%")




print(str(account))