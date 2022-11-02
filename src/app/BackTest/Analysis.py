import warnings
warnings.filterwarnings('ignore')
import pandas as pd
from src.app.BackTest.BackTest import BackTest
import matplotlib.pyplot as plt
import datetime
import seaborn as sns

class Analysis ():
    
    def analyzeBacktest(self, symbols, timeframe, usd=100, start_date='2019-01-01T00:00:00'):
        backtest = BackTest()
        dfTrades,positionInProgress = backtest.trade(symbols, timeframe, usd, start_date)
        dfBuyAndHold = backtest.buyAndHold(symbols, timeframe, usd, start_date)
        walletFinal = dfTrades.wallet.iloc[-1]
        algoPercentage = ((walletFinal - usd)/usd) * 100
        buyAndHold = dfBuyAndHold.finalBalance.sum()
        vsHoldPercentage = ((walletFinal/buyAndHold)-1)*100
        bestTrade = str(round(dfTrades['performance'].max(), 2))
        idbest = dfTrades['performance'].idxmax()
        worstTrade = str(round(dfTrades['performance'].min(), 2))
        idworst = dfTrades['performance'].idxmin()
        totalGoodTrades = len(dfTrades.loc[dfTrades['resultat'] == 'good'])
        totalBadTrades = len(dfTrades.loc[dfTrades['resultat'] == 'bad'])
        winRateRatio = (totalGoodTrades/(dfTrades.loc[dfTrades['position'] == 'Buy'].symbol.count())) * 100
        tradesPerformance = round(dfTrades.performance.mean(), 3)
        AveragePercentagePositivTrades = round(dfTrades[dfTrades['performance'] > 0].performance.mean(), 3)
        AveragePercentageNegativTrades = round(dfTrades[dfTrades['performance'] <= 0 ].performance.mean(), 3)
        
        print("")
        print("Trading Bot on :", len(symbols), 'coins | Timeframe :', timeframe)
        print("Starting date : [" + str(start_date) + "]")
        print("Starting balance :", usd, "$")
        print("\n----- General Informations -----")
        print("Final balance :", round(walletFinal, 2), "$")
        print("Performance :", round(algoPercentage, 2), "%")
        print("Buy and Hold :", round(buyAndHold, 2), "$")
        print("Performance vs Buy and Hold :", round(vsHoldPercentage, 2), "%")
        print("Best trade : +"+bestTrade, "%, the", idbest)
        print("Worst trade :", worstTrade, "%, the", idworst)
        print("\n----- Trades Informations -----")
        print("Number of trade :", (dfTrades.loc[dfTrades['position'] == 'Buy'].count()).symbol, "trades")
        print("Number of positive trades :", totalGoodTrades)
        print("Number of negative trades : ", totalBadTrades)
        print("Trades win rate ratio :", round(winRateRatio, 2), '%')
        print("Average trades performance :", tradesPerformance, "%")
        print("Average positive trades :", AveragePercentagePositivTrades, "%")
        print("Average negative trades :", AveragePercentageNegativTrades, "%")
        print("\n----- Pair Result -----")
        dash = '-' * 95
        print(dash)
        print('{:<6s}{:>10s}{:>15s}{:>15s}{:>15s}{:>15s}{:>15s}'.format(
            "Trades","Pair","Sum-result","Mean-trade","Worst-trade","Best-trade","Win-rate"
            ))
        print(dash)
        for pair in symbols:
            dfPairLoc = dfTrades.loc[dfTrades['symbol'] == pair].performance
            pairGoodTrade = len(dfTrades.loc[(dfTrades['symbol'] == pair) & (dfTrades['performance'] > 0)])
            pairTotalTrade = int(len(dfPairLoc)/2)
            pairResult = str(round(dfPairLoc.sum(),2))+' %'
            pairAverage = str(round(dfPairLoc.mean(),2))+' %'
            pairMin = str(round(dfPairLoc.min(),2))+' %'
            pairMax = str(round(dfPairLoc.max(),2))+' %'
            pairWinRate = str(round(100*(pairGoodTrade/pairTotalTrade),2))+' %'
            print('{:<6d}{:>10s}{:>15s}{:>15s}{:>15s}{:>15s}{:>15s}'.format(
                pairTotalTrade,pair,pairResult,pairAverage,pairMin,pairMax,pairWinRate
            ))
        self.plot_bar_by_month(dfTrades)
        return()
    
    def plot_bar_by_month(self, dfTrades):
        sns.set(rc={'figure.figsize':(11.7,8.27)})
        lastMonth = int(dfTrades.iloc[-1]['date'].month)
        lastYear = int(dfTrades.iloc[-1]['date'].year)
        dfTrades = dfTrades.set_index(dfTrades['date'])
        dfTrades.index = pd.to_datetime(dfTrades.index)
        myMonth = int(dfTrades.iloc[0]['date'].month)
        myYear = int(dfTrades.iloc[0]['date'].year)
        custom_palette = {}
        dfTemp = pd.DataFrame([])
        while myYear != lastYear or myMonth != lastMonth:
            myString = str(myYear) + "-" + str(myMonth)
            try:
                myResult = (dfTrades.loc[myString].iloc[-1]['wallet'] -
                            dfTrades.loc[myString].iloc[0]['wallet'])/dfTrades.loc[myString].iloc[0]['wallet']
            except:
                myResult = 0
            myrow = {
                'date': str(datetime.date(1900, myMonth, 1).strftime('%B')),
                'result': round(myResult*100)
            }
            dfTemp = dfTemp.append(myrow, ignore_index=True)
            if myResult >= 0:
                custom_palette[str(datetime.date(1900, myMonth, 1).strftime('%B'))] = 'g'
            else:
                custom_palette[str(datetime.date(1900, myMonth, 1).strftime('%B'))] = 'r'
            # print(myYear, myMonth, round(myResult*100, 2), "%")
            if myMonth < 12:
                myMonth += 1
            else:
                g = sns.barplot(data=dfTemp,x='date',y='result', palette=custom_palette)
                for index, row in dfTemp.iterrows():
                    if row.result >= 0:
                        g.text(row.name,row.result, '+'+str(round(row.result))+'%', color='black', ha="center", va="bottom")
                    else:
                        g.text(row.name,row.result, '-'+str(round(row.result))+'%', color='black', ha="center", va="top")
                g.set_title(str(myYear) + ' performance in %')
                g.set(xlabel=myYear, ylabel='performance %')
                yearResult = (dfTrades.loc[str(myYear)].iloc[-1]['wallet'] -
                            dfTrades.loc[str(myYear)].iloc[0]['wallet'])/dfTrades.loc[str(myYear)].iloc[0]['wallet']
                print("----- " + str(myYear) +" Performances: " + str(round(yearResult*100,2)) + "% -----")
                plt.show()
                dfTemp = pd.DataFrame([])
                myMonth = 1
                myYear += 1

        myString = str(lastYear) + "-" + str(lastMonth)
        try:
            myResult = (dfTrades.loc[myString].iloc[-1]['wallet'] -
                        dfTrades.loc[myString].iloc[0]['wallet'])/dfTrades.loc[myString].iloc[0]['wallet']
        except:
            myResult = 0
        g = sns.barplot(data=dfTemp,x='date',y='result', palette=custom_palette)
        for index, row in dfTemp.iterrows():
            if row.result >= 0:
                g.text(row.name,row.result, '+'+str(round(row.result))+'%', color='black', ha="center", va="bottom")
            else:
                g.text(row.name,row.result, '-'+str(round(row.result))+'%', color='black', ha="center", va="top")
        g.set_title(str(myYear) + ' performance in %')
        g.set(xlabel=myYear, ylabel='performance %')
        yearResult = (dfTrades.loc[str(myYear)].iloc[-1]['wallet'] -
                dfTrades.loc[str(myYear)].iloc[0]['wallet'])/dfTrades.loc[str(myYear)].iloc[0]['wallet']
        print("----- " + str(myYear) +" Performances: " + str(round(yearResult*100,2)) + "% -----")
        plt.show()

if __name__ == '__main__':
    analysis = Analysis()
    pairList = ['BTC/USDT', 'ETH/USDT', 'BNB/USDT', 'XRP/USDT', 'ADA/USDT']
    analysis.analyzeBacktest(pairList, '1h', start_date='2021-01-01')