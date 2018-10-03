import pandas as pd
import matplotlib.pyplot as plt

def stock_data():
    stocks = ['NVDA', 'AMD', 'NIO', 'TSLA']

    i_date = '2018-09-10'
    f_date = '2018-09-17'
    date_range = pd.date_range(i_date, f_date)
    df_base = pd.DataFrame(index = date_range)
    df = pd.read_csv('TSLA.csv', index_col='Date', parse_dates = True,
                     usecols = ['Date', 'Adj Close'], na_values = ['nan'])
    df_base = df_base.join(df)
    df_base = df_base.dropna()
    print(df_base)
    plt.plot(df_base.index, df_base['Adj Close'])
    plt.show()
    #for comp in stocks:
     #   df = pd.read_csv('{}.csv'.format(comp), index_col='Date')
        

if __name__ == '__main__':
    stock_data()
        
    
