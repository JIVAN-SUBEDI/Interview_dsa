# Check if pair with given Sum exists in Array (Two Sum)
# Given an array A[] of n numbers and another number x, the task is to check whether or not there exist two elements in A[] whose sum is exactly x. 
# Example
# Input: arr[] = {0, -1, 2, -3, 1}, x= -2
# Output: Yes
# Explanation: If we calculate the sum of the output,1 + (-3) = -2

# Input: arr[] = {1, -2, 1, 0, 5}, x = 0
# Output: No
arr = []
n= int(input("Enter the number of elements in array:"))
for i in range(0,n):
    element = int(input())
    arr.append(element)
x = int(input("Enter the value of x:"))
exists = 0
for j in range(0,n):
    check = arr[j]
    for k in range(0,n):
        if(j != k):
            if(check+arr[k] == x):
                exists = 1
if(exists == 0):
    print("No")
else:
    print("Yes")

