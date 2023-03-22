from sys import stdin


def optimal_value(capacity, weights, values):
    value = 0
    # write your code here

    #create a python dictionary with key as rate(=values/weights) and value as available quantity(weights).
    value_dict={}

    for i in range(len(values)):
        value_dict[values[i]/weights[i]]=weights[i]

    #sort the dictionary in descending order of rate
    value_dict_sorted=dict(sorted(value_dict.items(), reverse=True))

    for rate,weight in value_dict_sorted.items():
        if capacity==0:
            break
         
        #thief will be able to take the min. of remaining space in knapsack or the item available 
        qty_to_take=min(capacity,weight)

        #Increment the value of loot
        value = value + rate*qty_to_take

        #Calculate remaining space in knapsack
        capacity=capacity-qty_to_take

    return value


if __name__ == "__main__":
    data = list(map(int, stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
