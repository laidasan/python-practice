import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import csv
import pandas as pd
import twstock
import pandas_datareader as pdr
import datetime as datetime
import mpl_finance as mpf
import talib


def searchDF(df_name):
    start = datetime.datetime(2018,12,1)
    df_xxxx = pdr.DataReader(df_name,'yahoo',start=start)
    df_xxxx.index = df_xxxx.index.format(formatter=lambda x: x.strftime('%Y-%m-%d'))
    df_xxxx['k'],df_xxxx['d'] =talib.STOCH(df_xxxx['High'],df_xxxx['Low'],df_xxxx['Close'])
    df_xxxx['k'].fillna(value=0, inplace=True)
    df_xxxx['d'].fillna(value=0, inplace=True)


    sma_10 = talib.SMA(np.array(df_xxxx['Close']),20)
    sma_30 = talib.SMA(np.array(df_xxxx['Close']),60)

    fig = plt.figure(figsize=(30,20))
    # ax = fig.add_subplot(1,1,1)
    ax = fig.add_axes([0.05,0.6,0.9,0.4])
    ax2 = fig.add_axes([0.05,0.49,0.9,0.1])
    ax3 = fig.add_axes([0.05,0.15,0.9,0.3])
    plt.title('df_xxxx',loc='right')
    
    ax.set_xticks(range(0,len(df_xxxx.index),10))
    ax.set_xticklabels(df_xxxx.index[::10])
    mpf.candlestick2_ochl(ax,df_xxxx['Open'],df_xxxx['Close'],df_xxxx['High'],df_xxxx['Low'],width=0.6,colorup='r',colordown='g',alpha=0.75)

    ax.plot(sma_10,label='sma_20')
    ax.plot(sma_30,label='sma_60')

    ax2.plot(df_xxxx['k'],label='K')
    ax2.plot(df_xxxx['d'],label='D')
    ax2.set_xticks(range(0,len(df_xxxx.index),10))
    ax2.set_xticklabels(df_xxxx.index[::10])

    mpf.volume_overlay(ax3, df_xxxx['Open'], df_xxxx['Close'], df_xxxx['Volume'], colorup='r', colordown='g', width=0.5, alpha=0.8)
    ax3.set_xticks(range(0,len(df_xxxx.index),10))
    ax3.set_xticklabels(df_xxxx.index[::10])

    ax.legend(loc='upper right')
    ax2.legend(loc='upper right')
    plt.show()



#進入點 main
leave = '0'
while(leave == '0'):
    df_name = input('Enter What you want to look(leave = 0) --> ') + '.TW'
    if(df_name == '0.TW'):
        leave = '1'
    else:
        searchDF(df_name)