import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import csv
import pandas as pd
import twstock
import pandas_datareader as pdr
import datetime as datetime
import mpl_finance as mpf
# with open('day06-csv.csv','w',newline='') as csvfile:
#     writer = csv.writer(csvfile)
#     writer.writerow(['股票','收盤價','單量'])

# with open('day06-csv.csv',newline='') as csvfile:
#     rows = csv.reader(csvfile)
#     print(type(rows))
#     for row in rows:
#         print(type(row))
#         print(row)
# close = 0
# while(close == 0):
#     name = input('Please what you want to search,if you want to leave,enter number 0 -->')
#     if(name == '0'):
#         close = 1
#     elif(name == 'help'):
#         with open('STOCK_DAY_ALL.csv',newline='',encoding='utf8') as stockfile:
#             rows = csv.reader(stockfile)
#             for row in rows:
#                 print(row[1])
#     else:
#         with open('STOCK_DAY_ALL.csv',newline='',encoding='utf8') as stockfile:
#             rows = csv.reader(stockfile)
#             for row in rows:
#                 if(row[1] == name):
#                     print(row)
#                     break
#         break
            # rows_list = list(rows)
            # print(rows_list[1][1])
            # for row in rows:
            #     print(row[1])


        

# mylist_zeros = np.zeros(10)   # ndarray
# mylist_zeros2 = np.zeros((3,5),dtype=int)
# print(mylist_zeros2)
# print(mylist_zeros2[0])

# mylist_arange = np.arange(0,20,2)
# print(mylist_arange)
# mylist_linespace = np.linspace(0,1,5)
# print(mylist_linespace)

# %matplotlib inline

# mylist_linespace = np.linspace(-10,10,100)
# mylist_linespace2 = np.linspace(0,10,1000)
# fig = plt.figure()
# fig , ax = plt.subplots()
# plt.plot(mylist_linespace2,np.cos(mylist_linespace2),color="#ffaa00",ls='dotted',label='Cos')
# plt.plot(mylist_linespace2,np.sin(mylist_linespace2),color="#00aacc",ls='dotted',label='Sin')
# ax.axis('equal')
# leg = ax.legend(loc='upper right',shadow=True)
# plt.style.use('ggplot')
# plt.xlim(-15,15)
# plt.title('對阿')
# plt.xlabel('x')
# plt.ylabel('sin')
# plt.plot(mylist_linespace,np.sin(mylist_linespace),linestyle='solid',color='#ffaa00')
# fig = plt.figure()
# ax = plt.axes()

# plt.xticks(range(7),['A','B','C','D','E','F','G'])
# myhist = np.random.randn(1000)
# mygrades = [80,80,80,80,65,40,75,75,90,100]
# mygrades.sort()
# print(mygrades)
# print(len(mygrades))
# plt.hist(mygrades,bins=len(mygrades),color='#00ffaa',edgecolor='#ffffff')
# plt.plot(mygrades,ls='solid',color="#ffaa00")
# plt.show()   #在jupyter notebook可以在最一開始引入%matplotlib inline，就不用上plt.show()
# print(plt.style.available)



# fig = plt.figure()
mylist = np.linspace(-10,10,1000)
mylist2 = np.linspace(0,10,1000)
mylist3 = list(range(10))
mylist4 = list(range(10))
# print(mylist)
# print(mylist2)
# plt.plot(mylist,np.cos(mylist),color='#ffaa00',ls='dotted',label='cos')
# plt.plot(mylist,np.sin(mylist),color='#00aaff',ls='dotted',label='sin')
# plt.plot(mylist4,mylist3,label='test',ls='solid')
# plt.title('Test Practice',loc='right')
# plt.xlabel('test')
# plt.ylabel('practice')
# plt.grid(True,axis='y')
# plt.ylim(-10,10)
# plt.xlim(-10,100)
# plt.legend(loc='upper left')

# plt.show()

# mylist_index = ['a','b','c','d','e','f']
# mylist = pd.Series([1,2,3,4,5,6],index=mylist_index)
# print(mylist)
# mylist_dict = {'A':1,'B':2,'C':3}
# print(mylist_dict)
# mylist_dict_to_Series = pd.Series(mylist_dict)
# print(mylist_dict_to_Series)
# print(mylist_dict['A'])
# my_Series = pd.Series([0.11,0.22,0.33,0.44], index=[1,3,5,7])
# my_Series = pd.Series([0.11,0.22,0.33,0.44])
# my_Series_df = pd.DataFrame({'Date':my_Series})
# number = pd.Series({'taipei':200,'taichung':300,'changhua':400,'Kaohsiung':150})
# mayor = pd.Series({'taipei':'Kui','taichung':'Ha','changhua':'Chin','Kaohsiung':'Lui'})
# print(my_Series)
# print(my_Series_df)
# mypanda_df = pd.DataFrame({'number':number,'mayor':mayor})
# print(mypanda_df)
# print(number[0:3])
# print(number['taipei':'taichung'])
# print(number > 200)
# print(mylist_dict_to_Series > 2)
# print(number[['taipei','kaohsiung']])
# print(my_Series.loc[1:3])


# mylist_pd_DataFrame = pd.DataFrame({'number':number,'mayor':mayor})
# mylist_pd_DataFrame = pd.DataFrame(number,columns=['number']) #Use this way
# mylist_pd_DataFrame = pd.DataFrame({'number':number})  #Use Series
# mylist_pd_DataFrame = pd.DataFrame({'number':{'taipei':200,'taichung':300,'changhua':400,'kaohsiung':150}})  #Use dict
# team =np.zeros(4,dtype={'names':('name','number','team'),'formats':('U10','i2','U10')})
# team['name'] = ['彭政閔','林智勝','蘇偉達','陽耀勳']
# team['number'] = [23,32,96,23]
# team['team'] = ['兄弟象','兄弟象','兄弟象','lamigo']
# mylist_pd_DataFrame = pd.DataFrame(team) #Use structured array
# mylist_pd_DataFrame = pd.DataFrame(number)   #當沒有給index的時候索引值是預設數字
# print(mylist_pd_DataFrame)
# print(mylist_pd_DataFrame)
# print(mylist_pd_DataFrame.iloc[:2])

#About Time
# mytime_pd = pd.to_datetime('2019-05-21')
# mytime_pd += pd.to_timedelta(np.arange(5),'D')
# mytime_index = pd.DatetimeIndex(mytime_pd)
# mytime_index2 = pd.DatetimeIndex(['2018-10-11','2018-10-12','2017-10-11','2017-10-12','2017-10-13'])
# mytime_data = pd.Series(np.arange(5),index=mytime_index2)
# mytime_pd2 = pd.to_timedelta(np.arange(5),'D')
# mytime_pd3 = mytime_pd + mytime_pd2
# print(mytime_pd)
# print(mytime_data)
# print(mytime_data['2018'])

# fig = plt.figure()
# plt.plot(mytime_data,ls='solid',color='#ffaa00')
# plt.show()

#read .csv file 
# with open('STOCK_DAY_ALL.csv',newline='',encoding='utf8') as stockfile:
#     rows = csv.reader(stockfile)
#     rows_list =list(rows)
#     for row in rows_list:
#         print(row)






#About twtock
# price
# close
# open
# low
# high
# date

# print(twstock.codes['6207'])
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


#df_2377
start = datetime.datetime(2019,3,1)
df_2377 = pdr.DataReader('2377.TW','yahoo',start=start)
df_2377.index = df_2377.index.format(formatter=lambda x: x.strftime('%Y-%m-%d'))
print(len(df_2377.index))
print(df_2377.index[::10])
fig = plt.figure(figsize=(48,8))

ax = fig.add_subplot(1,1,1)
ax.set_xticks(range(0,len(df_2377.index),10))
ax.set_xticklabels(df_2377.index[::10])
mpf.candlestick2_ochl(ax,df_2377['Open'],df_2377['Close'],df_2377['High'],df_2377['Low'],width=0.6,colorup='r',colordown='g',alpha=0.75)
plt.show()


#pdr
# start = datetime.datetime(2019,4,1)
# df_2330 = pdr.DataReader('2330.TW','yahoo',start=start)
# df_2376 = pdr.DataReader('2376.TW','yahoo',start=start)
# print(df_2376)
# fit = plt.figure(figsize=(15,6))
# plt.plot(df_2376['Adj Close'],ls='solid',color='#ffaa00',label='技嘉2376')
# plt.title('2376',loc='right')
# plt.xlabel('Date')
# plt.ylabel('Price')
# plt.show()
# print(df_2330)



# 雷科 Stock_6207 open&close 製圖
# fit = plt.figure(figsize=(10,6))
# plt.plot(stock_6207_2019_pd.open,ls='solid',color="#ffaa00",label="Open-price")
# plt.plot(stock_6207_2019_pd.close,ls='solid',color="#00aaff",label="Close-price")
# plt.title('stock-6207',loc='right')
# plt.xlabel('date')
# plt.ylabel('Price')
# plt.grid(True,axis='y')
# plt.legend()
# plt.show()






# 報告
# 直接使用csv.reader出來的rows拿來for或是做其他事情的話，做一次rows裡面就會變成空值[]，所以先存在list裡面
# with open('STOCK_DAY_ALL.csv',newline='',encoding='utf8') as stockfile:
#     rows = csv.reader(stockfile)
#     rows_list = list(rows)
#     close = 1
#     while(close != 0):
#         row_item = []
#         # print(row_item)
#         # print(row_item[0])
#         name = input('Please what you want to search,if you want to leave,enter number 0 -->')
#         if(name == '0'):
#             close = 0
#         elif(name == 'help'):
#             for row in rows_list:
#                 print(row[1])
#         else:
#             for row in rows_list:
#                 if(row[1] == name or row[0] == name):
#                     row_item = row
#                     break
#             if(row_item != []):
#                     print(row_item[2:len(row_item)-1])
#             else:
#                 print('查無資訊')




