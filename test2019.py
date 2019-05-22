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
# stock_6207
# stock_6207 = twstock.Stock('6207')
# stock_6207_2019 = stock_6207.fetch_from(2018,7)
# stock_6207_2019_pd = pd.DataFrame(stock_6207_2019)
# stock_6207_2019_pd = stock_6207_2019_pd.set_index('date')

#stock_2330
# stock_2330 = twstock.Stock('2330')
# print(stock_2330.price[-5:])
# stock_2330_2019 = stock_2330.fetch_from(2019,1)
# stock_2330_2019_pd = pd.DataFrame(stock_2330_2019)
# stock_2330_2019_pd = stock_2330_2019_pd.set_index('date')

#stock_2492
# stock_2492 = twstock.Stock('2492')
# stock_2492_2019 = stock_2492.fetch_from(2019,1)
# stock_2492_2019_pd = pd.DataFrame(stock_2492_2019)
# stock_2492_2019_pd = stock_2492_2019_pd.set_index('date')
# print(stock_2330_2019[0])
# fig = plt.figure(figsize=(15,6))
# plt.plot()
# print(stock_6207_2019_pd)
# print(stock_6207_2019_pd.close)
# price_6207 = stock_6207.price[-5:]

#stock_2377
# stock_2377 = twstock.Stock('2377')
# stock_2377_2019_3 = stock_2377.fetch_from(2019,3)
# stock_2377_2019_3_pd = pd.DataFrame(stock_2377_2019_3)
# stock_2377_2019_3_pd = stock_2377_2019_3_pd.set_index('date')
# print(stock_2377_2019_3_pd)
#蠟燭

#製圖
# fig = plt.figure(figsize=(10,6))
# plt.plot(stock_2377_2019_3_pd.close,ls='solid',color='#00aaff',label='2377')
# plt.title('2377',loc='right')
# plt.xlabel('Date')
# plt.ylabel('Close-Price')
# plt.grid(True,axis='y')
# plt.show()


#df_2377 微星
# start = datetime.datetime(2019,3,1)
# df_2377 = pdr.DataReader('2377.TW','yahoo',start=start)
# df_2377.index = df_2377.index.format(formatter=lambda x: x.strftime('%Y-%m-%d'))
# print(len(df_2377.index))
# print(df_2377.index[::10])
# fig = plt.figure(figsize=(48,8))

# ax = fig.add_subplot(1,1,1)
# ax.set_xticks(range(0,len(df_2377.index),10))
# ax.set_xticklabels(df_2377.index[::10])
# mpf.candlestick2_ochl(ax,df_2377['Open'],df_2377['Close'],df_2377['High'],df_2377['Low'],width=0.6,colorup='r',colordown='g',alpha=0.75)
# plt.show()

#df_2357 華碩
# start = datetime.datetime(2018,12,1)
# df_2357 = pdr.DataReader('2357.TW','yahoo',start=start)
# df_2357.index = df_2357.index.format(formatter=lambda x: x.strftime('%Y-%m-%d'))
# print(df_2357)
# print(len(df_2357.index))
# print(df_2357.index[::10])
# sma_10 = talib.SMA(np.array(df_2357['Close']),20)
# sma_30 = talib.SMA(np.array(df_2357['Close']),60)
# fig = plt.figure(figsize=(48,8))
# ax = fig.add_subplot(1,1,1)
# ax.set_xticks(range(0,len(df_2357.index),10))
# ax.set_xticklabels(df_2357.index[::10])
# mpf.candlestick2_ochl(ax,df_2357['Open'],df_2357['Close'],df_2357['High'],df_2357['Low'],width=0.6,colorup='r',colordown='g',alpha=0.75)
# ax.plot(sma_10,label='sma_20')
# ax.plot(sma_30,label='sma_60')
# plt.legend(loc='upper right')
# plt.show()

def searchDF(df_name):
    start = datetime.datetime(2018,12,1)
    df_xxxx = pdr.DataReader(df_name,'yahoo',start=start)
    df_xxxx.index = df_xxxx.index.format(formatter=lambda x: x.strftime('%Y-%m-%d'))
    sma_10 = talib.SMA(np.array(df_xxxx['Close']),20)
    sma_30 = talib.SMA(np.array(df_xxxx['Close']),60)
    fig = plt.figure(figsize=(48,8))
    ax = fig.add_subplot(1,1,1)
    ax.set_xticks(range(0,len(df_xxxx.index),10))
    ax.set_xticklabels(df_xxxx.index[::10])
    mpf.candlestick2_ochl(ax,df_xxxx['Open'],df_xxxx['Close'],df_xxxx['High'],df_xxxx['Low'],width=0.6,colorup='r',colordown='g',alpha=0.75)
    ax.plot(sma_10,label='sma_20')
    ax.plot(sma_30,label='sma_60')
    plt.legend(loc='upper right')
    plt.show()

#進入點 main
leave = '0'
while(leave == '0'):
    df_name = input('Enter What you want to look(leave = 0) --> ') + '.TW'
    if(df_name == '0.TW'):
        leave = '1'
    else:
        searchDF(df_name)


#df_2376 技嘉
# start = datetime.datetime(2019,3,1)
# df_2376 = pdr.DataReader('2376.TW','yahoo',start=start)
# df_2376.index = df_2376.index.format(formatter=lambda x: x.strftime('%Y-%m-%d'))
# print(len(df_2376.index))
# print(df_2376.index[::10])
#均線
# sma_10 = talib.SMA(np.array(df_2353['Close']),10)
# sma_30 = talib.SMA(np.array(df_2353['Close']),30)
# fig = plt.figure(figsize=(48,8))
# ax = fig.add_subplot(1,1,1)
# ax.set_xticks(range(0,len(df_2376.index),10))
# ax.set_xticklabels(df_2376.index[::10])
# mpf.candlestick2_ochl(ax,df_2376['Open'],df_2376['Close'],df_2376['High'],df_2376['Low'],width=0.6,colorup='r',colordown='g',alpha=0.75)
# ax.plot(sma_10,label='sma_10')
# ax.plot(sma_30,label='sma_30')
# plt.legend(loc='upper right')
# plt.show()

#df_2353 宏碁
# start = datetime.datetime(2019,1,1)
# df_2353 = pdr.DataReader('2353.TW','yahoo',start=start)
# df_2353.index = df_2353.index.format(formatter=lambda x: x.strftime('%Y-%m-%d'))
# print(len(df_2353.index))
# print(df_2353.index[::10])
# #均線
# sma_10 = talib.SMA(np.array(df_2353['Close']),10)
# sma_30 = talib.SMA(np.array(df_2353['Close']),30)
# fig = plt.figure(figsize=(48,8))
# ax = fig.add_subplot(1,1,1)
# ax.set_xticks(range(0,len(df_2353.index),10))
# ax.set_xticklabels(df_2353.index[::10])
# mpf.candlestick2_ochl(ax,df_2353['Open'],df_2353['Close'],df_2353['High'],df_2353['Low'],width=0.6,colorup='r',colordown='g',alpha=0.75)
# ax.plot(sma_10,label='sma_10')
# ax.plot(sma_30,label='sma_30')
# plt.legend(loc='upper right')
# plt.show()