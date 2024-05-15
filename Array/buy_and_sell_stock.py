# Given an array prices[] of length N, representing the prices of the stocks on different days, the task is to find the maximum profit possible by buying and selling the stocks on different days when at most one transaction is allowed.

# Note: Stock must be bought before being sold.
# Input: prices[] = {7, 1, 5, 3, 6, 4}
# Output: 5
# Explanation:
# The lowest price of the stock is on the 2nd day, i.e. price = 1. Starting from the 2nd day, the highest price of the stock is witnessed on the 5th day, i.e. price = 6. 
# Therefore, maximum possible profit = 6 – 1 = 5. 

# Input: prices[] = {7, 6, 4, 3, 1} 
# Output: 0
# Explanation: Since the array is in decreasing order, no possible way exists to solve the problem.
def max_profit(prices,n):
    buy = prices[0]
    profit = 0
    for i in range(0,n):
        if(buy > prices[i]):
            buy = prices[i]
        elif(prices[i] - buy > profit):
            profit = prices[i] - buy
    return profit

prices = []
n= int(input("Enter the number of elements in array:"))
for i in range(0,n):
    element = int(input())
    prices.append(element)
profit = max_profit(prices,n)
print("Max Profit:",profit)

        
