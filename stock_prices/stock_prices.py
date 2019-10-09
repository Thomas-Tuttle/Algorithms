#!/usr/bin/python

import argparse

def find_max_profit(prices):
    # highest price - lowest price = max profit possible 
    max_profit = prices[1] - prices[0]
    lowest = prices[0]
    # for every index for the length of the array
    for i in range(1, len(prices)):
        # if the current index is lower than the lowest number, make it the new lowest
        if prices[i] < lowest:
            lowest = prices[i]
        # if the index price - the lowest is more than the current max profit, make it the new max profit  
        elif prices[i] - lowest > max_profit:
            max_profit = prices[i] - lowest
    # return the max profit
    return max_profit

test = [10, 57, 25, 78, 111, 19]
x = find_max_profit(test)
print(f"\nYour max profit will be $", x)


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))