import pandas as pd
import matplotlib.pyplot as plt

def stock_data():
    stocks = ['NVDA', 'AMD', 'NIO', 'TSLA']

    i_date = '2018-09-02'
    f_date = '2018-09-28'
    date_range = pd.date_range(i_date, f_date)
    df_base = pd.DataFrame(index = date_range)
    df = pd.read_csv('TSLA.csv', index_col='Date', parse_dates = True,
                     usecols = ['Date', 'Adj Close'], na_values = ['nan'])
    df_base = df_base.join(df)
    df_base = df_base.dropna()
    df_base = df_base.rename(columns = {'Adj Close' : 'TSLA'})
    plt.subplot(2,2,1)
    plt.plot(df_base.index, df_base['TSLA'])
    i=2
    
    for comp in stocks[0:3]:
        df = pd.read_csv('{}.csv'.format(comp), index_col='Date',
                         usecols = ['Date', 'Adj Close'], parse_dates = True,
                         na_values = ['nan'])
        df = df.rename(columns={'Adj Close' : comp})
        df_base = df_base.join(df)
        plt.subplot(2,2,i)
        plt.plot(df_base.index, df_base[comp])
        i+=1
        
    print(df_base)
    plt.show()        
        

if __name__ == '__main__':
    stock_data()
        
    
