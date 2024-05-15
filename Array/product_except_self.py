# example
# Input: arr[]  = {10, 3, 5, 6, 2}
# Output: prod[]  = {180, 600, 360, 300, 900}
# 3 * 5 * 6 * 2 product of other array 
# elements except 10 is 180
# 10 * 5 * 6 * 2 product of other array 
# elements except 3 is 600
# 10 * 3 * 6 * 2 product of other array 
# elements except 5 is 360
# 10 * 3 * 5 * 2 product of other array 
# elements except 6 is 300
# 10 * 3 * 6 * 5 product of other array 
# elements except 2 is 900
def find_product(arr,n):
    result = []
    for i in range(0,n):
        product = 1
        for j in range(0, n):
            if i != j:
                product = product*arr[j]

        result.append(product)
    return result
arr = []
n= int(input("Enter the number of elements in array:"))
for i in range(0,n):
    element = int(input())
    arr.append(element)
product = find_product(arr,n)
print(product)