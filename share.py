def maxProfit(price, start, end):
    if (end <= start):
        return 0
    profit = 0
    for i in range(start, end, 1):
        for j in range(i+1, end+1):
            if (price[j] > price[i]):
                curr_profit = price[j] - price[i] +\
                            maxProfit(price, start, i - 1)+ \
                            maxProfit(price, j + 1, end)
                profit = max(profit, curr_profit)

def start():
    days = int(input())
    sharesPerDay = [int(x) for x in input().split()]
    print(maxProfit(sharesPerDay, 0, days - 1))

start()