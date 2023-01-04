from src.app.BackTest.Analysis import Analysis
import warnings
warnings.filterwarnings('ignore')

def main():
    analysis = Analysis()
    pairList = ['BTC/USDT', 'ETH/USDT', 'BNB/USDT', 'XRP/USDT', 'ADA/USDT']
    return(analysis.analyzeBacktest(pairList, '1h',usd = 100, start_date='2021-01-01', leverage = 1))

if __name__ == '__main__':
    print(main())