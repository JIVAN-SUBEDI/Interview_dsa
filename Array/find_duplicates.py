# Given an array of n elements that contains elements from 0 to n-1, with any of these numbers appearing any number of times
# example
# Input: n=7 , array[]={1, 2, 3, 6, 3, 6, 1}
# Output: 1, 3, 6
# Explanation: The numbers 1 , 3 and 6 appears more than once in the array.
def find_duplicates(arr,n):
    result = []
    for i in range(0,n):
        check = arr[i]
        for j in range(0, n):
            if i != j:
                if check == arr[j]:
                    if check not in result:
                     result.append(arr[j])
    
    return result
arr = []
n= int(input("Enter the number of elements in array:"))
for i in range(0,n):
    element = int(input())
    arr.append(element)
duplicate = find_duplicates(arr,n)
print(duplicate)