import pandas as pd
import matplotlib.pyplot as plt

def readprintcsv():
  df = pd.read_csv('sacramento.csv')
  #print(df[['sq__ft', 'price']])
  df_sel = df[['sq__ft', 'price']]
  print(df_sel[0:1]['price'])
  print("--------")
  print(df_sel['price'][0:1])

  
  #plt.plot(df[['sq__ft', 'price']].sort_values(by=['sq__ft']))
  #plt.show()
  # df[['sq__ft', 'price']] - to print multiple col data
  # df[0:10] - indices 0 to 9
  # df['price'] - all the values for 'price'
  # df.head(3) - first 3 from top (.tail(2) - last 2 from bottom)
  

if __name__ == '__main__':
  readprintcsv()
