### Quantiacs Trend Following Trading System Example
# import necessary Packages below:
import numpy


def myTradingSystem(DATE, OPEN, HIGH, LOW, CLOSE, VOL, exposure, equity, settings):
    """
    This function is called daily by quantiacs with the new data passed in
    by returning an array of weights you indicate the way you want your postions to change
    """

    # nMarkets = CLOSE.shape[1] #The amount of markets being operated in

    weights = ((CLOSE-OPEN)/OPEN) #Calculate the daily gains of each asset
    weights = numpy.sum(weights, axis=0) #Sum all gains in the lookback period

    return weights, settings # When returned to quantiacs weights idicates the proportional component of budget
                             # that should be us for each asset i.e. if weights was [-1, .5, .5] then 1 half of
                             # the budget would short the first asset and then a quater of it would be used to purchase
                             # the second asset likewise for the third.


def mySettings():
    ''' Define your trading system settings here '''

    settings= {}

    settings['markets']=['AAPL','ABBV','ABT','ACN']

    # Futures Contracts


    settings['beginInSample'] = '20150506'
    settings['endInSample'] = '20180506'
    settings['lookback']= 50
    settings['budget']= 10**6
    settings['slippage']= 0.05

    return settings

# Evaluate trading system defined in current file.
if __name__ == '__main__':
    import quantiacsToolbox
    results = quantiacsToolbox.runts(__file__)
