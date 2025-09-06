
""" 1.1 Write a short Python function, is multiple(n, m), that takes two integer
        values and returns True if n is a multiple of m, that is, n = mi for some
        integer i, and False otherwise."""
    

def is_multiple(n,m):
        if n % m == 0:
            return True
        else:
            return False
        
c=is_multiple(15,3)
print(c)

""" 1.2 Write a short Python function, is even(k), that takes an integer value and
returns True if k is even, and False otherwise. However, your function
cannot use the multiplication, modulo, or division operators."""


def is_even(k):
    # Make negative numbers positive
    if k < 0:
        k = -k
    # Subtract 2 repeatedly until 0 or 1
    while k > 1:
        k = k - 2
    if k == 0:
        return True
    else:
        return False
no=is_even(4)   
print(no)
   
""" R-1.3 Write a short Python function, minmax(data), that takes a sequence of
one or more numbers, and returns the smallest and largest numbers, in the
form of a tuple of length two. Do not use the built-in functions min or
max in implementing your solution."""

def minmax(numbers):
    smallest = largest = numbers[0]
    
    for num in numbers:
        if num < smallest: #it will just compare with the next value that its smaller or not
            smallest = num
        if num > largest: #it will just compare with the next value that its bigger or not
            largest = num
            
    return (smallest, largest)

data= minmax([10,2,4,6,8])
print(data)
    

""" R-1.4 Write a short Python function that takes a positive integer n and returns
the sum of the squares of all the positive integers smaller than n."""

#Compute the sum of the squares of all positive integers smaller than n.
#Positive integers smaller than 5 are: 1, 2, 3, 4.
#Square each number: 1^2 = 1, 2^2 = 4, 3^2 = 9, 4^2 = 16

def sum_squares(n):
    total = 0
    for i in range(1, n):
        total += i * i  # square of i and add to total
    return total

n=sum_squares(5)
print(f" sum of square is: {n}")

""" R-1.5 Give a single command that computes the sum from Exercise R-1.4, rely-
ing on Python’s comprehension syntax and the built-in sum function."""

def summ_squares(n):
    return sum(i * i for i in range(1, n)) # this will give sum(1,4,9,16,25) and then sum will do (1+4+9+16+25)

n=summ_squares(6)
print(f" sum of square is: {n}")

""" R-1.6 Write a short Python function that takes a positive integer n and returns
the sum of the squares of all the odd positive integers smaller than n."""

def sum_of_oddsquares(n):
    total = 0
    for i in range(1, n):
        if i%2!=0:
            total += i * i  # square of i and add to total
    return total

n=sum_of_oddsquares(6)
print(f" sum of odd square is: {n}")

"""R-1.7 Give a single command that computes the sum from Exercise R-1.6, rely-
ing on Python’s comprehension syntax and the built-in sum function."""


def summ_of_oddsquares(n):
    return sum(i*i for i in range(1, n) if i % 2 != 0) # this will give sum(1,4,9,16,25) and then sum will do (1+4+9+16+25)

n=summ_of_oddsquares(8)
print(f" sum of odd square is: {n}")

            
