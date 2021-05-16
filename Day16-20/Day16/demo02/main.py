

#字典推导式
#字典推导式列表推导式思想的延续，语法差不多，只不过产生的是字典而已。
#语法：{k:v for 变量 in 字典 if条件}

prices = {
    'AAPL': 191.88,
    'GOOG': 1186.96,
    'IBM': 149.24,
    'ORCL': 48.44,
    'ACN': 166.89,
    'FB': 208.09,
    'SYMC': 21.29
}
# 用股票价格大于100元的股票构造一个新的字典
prices2 = {k:v   for k, v in prices.items() if v > 100}
print(prices2) #{'AAPL': 191.88, 'GOOG': 1186.96, 'IBM': 149.24, 'ACN': 166.89, 'FB': 208.09}




prices2 = {"N_"+k:2*v   for k, v in prices.items() if v > 100}
print(prices2) #{'N_AAPL': 383.76, 'N_GOOG': 2373.92, 'N_IBM': 298.48, 'N_ACN': 333.78, 'N_FB': 416.18}