# Another reason you probably can't beat or time the market

This repo implements a simulated attempt at beating the stock market. The thesis is that you can outperform the market if you place limit orders slightly below market price to capture the spread induced by market volatility. The strategy goes as follows:

1. Start with $0.00 in a simulated brokerage account
2. On each day, check if the stock gave out any dividends. Reinvest the dividends at the Open price for that day.
3. Execute all existing limit orders that haven't expired and were able to be filled.
4. If it's a trade day (every `d` days), invest `x` dollars into the account. Make a market order at the close price and limit orders at lower fractions of the market price. This allocation is specified in `parameters`
5. If limit orders expire, invest those funds on the next trading day in addition to the `x` dollars.
6. Compare strategy against `parameters={1:1}`, which is normal periodic investing every `d` days, independent of market prices. The goal is to beat these metrics

So far, I haven't found a combination of stocks, timeframes, parameters, and limit time frames that have been able to beat the base case. If you think this strategy has some promise and should be able to beat the market, prove me wrong by following the steps below.

## Getting Started

1. Run `git clone https://github.com/mdjorup/strategy-simulation.git` in the command line in a directory of your choice.
2.
