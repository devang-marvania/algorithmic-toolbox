def change(money):
    #Create a list with some safe values(infinity here) as default. We will replace infinity with actual change value eventually. Here MinNumCoins[idx]=value, 
    # idx represents the money to be changed, value represents the min number of coins needed to replace original money
    MinNumCoins=[float('inf')]* (money+1)
    
    #list of available denominations
    coins=[1,3,4]

    #Min number of coins to change 0 dollar is 0, reflecting same here
    MinNumCoins[0]=0

    #Loop from 1 to money and whenever change amount is more than coin value, find out the min number of coins using previously stored MinNumCoins value
    for m in range(1,money+1):
        for coin in coins:
            if m>=coin:
                NumCoins=MinNumCoins[m-coin]+1
                if NumCoins<MinNumCoins[m]:
                    MinNumCoins[m]=NumCoins


    return MinNumCoins[money]


if __name__ == '__main__':
    m = int(input())
    print(change(m))
