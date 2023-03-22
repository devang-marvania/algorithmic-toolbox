def change(money):
    
    #Initialize to 0 as currently we haven't done any calculation for coins needed
    num_coins=0

    #Ten dollar coins can be calculated by dividing money with 10 and taking the int of result
    ten_dollar_coins=int(money/10)
    
    #Once we change money with ten dollar coints, remaining amount can be from 0 to 9. We figure out how many five coins
    #we might need - can be either 0 or 1
    five_dollar_coins=int((money%10)/5)

    #After changing money with ten dollar and five dollar coins, if there is any remaining amount, change it using 1 dollar coins
    #This will be between 0 and 4
    one_dollar_coins=money%5

    #Calculate sum of all coins needed
    num_coins=ten_dollar_coins+five_dollar_coins+one_dollar_coins   


    return num_coins


if __name__ == '__main__':
    m = int(input())
    print(change(m))
