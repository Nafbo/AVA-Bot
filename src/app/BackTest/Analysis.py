import warnings
warnings.filterwarnings('ignore')
import pandas as pd
from src.app.BackTest.BackTest import BackTest
import matplotlib.pyplot as plt
import datetime
import seaborn as sns

class Analysis ():
    
    def analyzeBacktest(self, symbols, timeframe, usd=100, start_date='2019-01-01T00:00:00',end_date=None, leverage=1):
        backtest = BackTest()
        dfTrades,positionInProgress = backtest.trade(symbols, timeframe, usd, start_date, end_date, leverage)
        dfBuyAndHold = backtest.buyAndHold(symbols, timeframe, usd, start_date,end_date)
        walletFinal = dfTrades.wallet.iloc[-1]
        algoPercentage = ((walletFinal - usd)/usd) * 100
        buyAndHold = dfBuyAndHold.finalBalance.sum()
        vsHoldPercentage = ((walletFinal/buyAndHold)-1)*100
        bestTrade = str(round(dfTrades['performance'].max(), 2))
        idbest = dfTrades['performance'].idxmax()
        worstTrade = str(round(dfTrades['performance'].min(), 2))
        idworst = dfTrades['performance'].idxmin()
        
        totalBadTrades = dfTrades.loc[dfTrades['resultat'] == 'bad'].count().symbol
        totalGoodTrades = dfTrades.loc[dfTrades['resultat'] == 'good'].count().symbol
        
        winRateRatio = (totalGoodTrades/(totalGoodTrades+totalBadTrades))
        tradesPerformance = round(dfTrades.performance.mean(), 3)
        AveragePercentagePositivTrades = round(dfTrades[dfTrades['performance'] > 0].performance.mean(), 3)
        AveragePercentageNegativTrades = round(dfTrades[dfTrades['performance'] <= 0 ].performance.mean(), 3)
        
        dfPosition = pd.concat([dfTrades.loc[dfTrades['position'] == 'stopLossHit'],dfTrades.loc[dfTrades['position'] == 'takeProfitHit'], dfTrades.loc[dfTrades['position'] == 'closeShort'], dfTrades.loc[dfTrades['position'] == 'closeLong']])
        dfPositionLong = []
        dfPositionShort = []
        for i in range(len(dfPosition)):
            date = dfPosition.iloc[i].whenBuy
            if dfTrades.loc[date].shape[0]!=15:
                for j in range(len(dfTrades.loc[date])):
                    if dfTrades.loc[date].iloc[j].position == "openLong" and dfTrades.loc[date].iloc[j].symbol == dfPosition.iloc[i].symbol:
                        dfPositionLong.append(dfPosition.iloc[i])
                    elif dfTrades.loc[date].iloc[j].position == "openShort" and dfTrades.loc[date].iloc[j].symbol == dfPosition.iloc[i].symbol:
                        dfPositionShort.append(dfPosition.iloc[i])
            else:
                if dfTrades.loc[date].position == "openLong" and dfTrades.loc[date].symbol == dfPosition.iloc[i].symbol:
                    dfPositionLong.append(dfPosition.iloc[i])
                elif dfTrades.loc[date].position == "openShort" and dfTrades.loc[date].symbol == dfPosition.iloc[i].symbol:
                    dfPositionShort.append(dfPosition.iloc[i])
        dfPositionLong = pd.DataFrame(dfPositionLong)
        dfPositionShort = pd.DataFrame(dfPositionShort)
        
        TotalLongTrades = dfPositionLong.shape[0]
        if TotalLongTrades !=0:                    
            AverageLongTrades = round(dfPositionLong.performance.sum()
                                    / dfPositionLong.performance.count(), 2)
            idBestLong = dfPositionLong.performance.idxmax()
            bestLongTrade = str(round(dfPositionLong.performance.max(), 2))
            idWorstLong = dfPositionLong.performance.idxmin()
            worstLongTrade = str(round(dfPositionLong.performance.min(), 2))
            totalGoodLongTrade = dfPositionLong.loc[dfPositionLong['resultat'] == 'good'].count().symbol
            totalBadLongTrade = dfPositionLong.loc[dfPositionLong['resultat'] == 'bad'].count().symbol
            winRateLong = round(totalGoodLongTrade/TotalLongTrades*100, 2)
        else:
            AverageLongTrades = "nan"
            idBestLong = "nan"
            bestLongTrade = "nan"
            idWorstLong = "nan"
            worstLongTrade = "nan"
            totalGoodLongTrade = 0
            totalBadLongTrade = 0
            winRateLong = 0
            
        
        TotalShortTrades = dfPositionShort.shape[0]
        if TotalShortTrades !=0:
            AverageShortTrades = round(dfPositionShort.performance.sum()
                                / dfPositionShort.performance.count(), 2)
            idBestShort = dfPositionShort.performance.idxmax()
            bestShortTrade = str(round(dfPositionShort.performance.max(), 2))
            idWorstShort = dfPositionShort.performance.idxmin()
            worstShortTrade = str(round(dfPositionShort.performance.min(), 2))
            totalGoodShortTrade = dfPositionShort.loc[dfPositionShort['resultat'] == 'good'].count().symbol
            totalBadShortTrade = dfPositionShort.loc[dfPositionShort['resultat'] == 'bad'].count().symbol
            winRateShort = round(totalGoodShortTrade/TotalShortTrades*100, 2)
        else:
            AverageShortTrades = "nan"
            idBestShort = "nan"
            bestShortTrade = "nan"
            idWorstShort = "nan"
            worstShortTrade = "nan"
            totalGoodShortTrade = 0
            totalBadShortTrade = 0
            winRateShort = 0
            
            
        
        print("")
        print("Trading Bot on :", len(symbols), 'coins | Timeframe :', timeframe)
        print("Starting date : [" + str(start_date) + "]")
        print("Ending date : [" + str(end_date) + "]")
        print("Starting balance :", usd, "$")
        print("Leverage use :", leverage )
        
        print("\n----- General Informations -----")
        print("Total balance :", round(walletFinal, 2), "$")
        print("Total fees : ", round(dfTrades['fees'].sum(), 2), "$")
        print("Final Balance :", round(walletFinal-dfTrades['fees'].sum(), 2), "$")
        print("Performance :", round(algoPercentage, 2), "%")
        print("Buy and Hold :", round(buyAndHold, 2), "$")
        print("Performance vs Buy and Hold :", round(vsHoldPercentage, 2), "%")
        print("Best trade : +"+bestTrade, "%, the", idbest)
        print("Worst trade :", worstTrade, "%, the", idworst) 
        
        print("\n----- Trades Informations -----")
        print("Number of trades :", TotalShortTrades+TotalLongTrades)
        print("Number of positive trades :", totalGoodTrades)
        print("Number of negative trades : ", totalBadTrades)
        print("Trades win rate ratio :", round((winRateRatio) * 100, 2), '%')
        print("Average trades performance :", tradesPerformance, "%")
        print("Average positive trades :", AveragePercentagePositivTrades, "%")
        print("Average negative trades :", AveragePercentageNegativTrades, "%")
        
        print("\n----- LONG Trades Informations -----")
        print("Number of Long trade :", TotalLongTrades, "trades")
        print("Average LONG trades performance :",AverageLongTrades, "%")
        print("Best  LONG trade +",bestLongTrade, "%, the ", idBestLong)
        print("Worst LONG trade", worstLongTrade, "%, the ", idWorstLong)
        print("Number of positive LONG trades :",totalGoodLongTrade)
        print("Number of negative LONG trades :",totalBadLongTrade)
        print("LONG trade win rate ratio :", winRateLong, '%')

        print("\n----- SHORT Trades Informations -----")
        print("Number of Short trade :", TotalShortTrades, "trades")
        print("Average SHORT trades performance :",AverageShortTrades, "%")
        print("Best  SHORT trade +",bestShortTrade, "%, the ", idBestShort)
        print("Worst SHORT trade", worstShortTrade, "%, the ", idWorstShort)
        print("Number of positive SHORT trades :",totalGoodShortTrade)
        print("Number of negative SHORT trades :",totalBadShortTrade)
        print("SHORT trade win rate ratio :", winRateShort, '%')
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
            if pairTotalTrade == 0:
                pairWinRate = 'None'
            else:
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
    analysis.analyzeBacktest(pairList, '1h', usd = 100, start_date='2023-01-01',end_date = '2023-02-28', leverage = 1.5)