# Iterative python program to reverse an array

# Function to reverse A[] from start to end
def reverseList(A, start, end):
	while start < end:
		A[start], A[end] = A[end], A[start]
		start += 1
		end -= 1

# Driver function to test above function
A = [1, 2, 3, 4, 5, 6]
print(A)
reverseList(A, 0, 5)
print("Reversed list is")
print(A)

"""
#Iterative python program to reverse a string
def reverse(str):
    string = " "
    for i in str:
        string = i + string
    return string
str = "PythonGuides"
print("The original string is:",str)
print("The reverse string is:", reverse(str)) """
