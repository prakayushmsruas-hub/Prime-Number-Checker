# Prime-Number-Checker
Prime Number Checker in Python
Overview

This program checks whether a number is a Prime Number or not using:

Functions
Loops
Boolean Flagging
User Menu System

A prime number is a number greater than 1 that has only:

1
itself

as factors.

Examples:

2 → Prime
3 → Prime
4 → Not Prime
7 → Prime
How the Program Works
Step 1 — Function Creation
def Prime_number_checker():

A function is created to handle prime number checking.

Step 2 — User Input
num = int(input("Enter the number you want to check for prime: "))

The user enters a number.

Step 3 — Check Numbers Less Than or Equal to 1
if num <= 1:
    print("Not a Prime Number")
    return

Numbers less than or equal to 1 are not prime.

Why?
Because prime numbers must have exactly 2 factors.

Step 4 — Flag Variable
prime = True

A flag variable is used.

Initially:

Assume the number is prime.

If any factor is found:

Change it to False.
Step 5 — Loop for Factor Checking
for j in range(2, num):

The loop checks every number from:

2 → num-1
Step 6 — Divisibility Check
if num % j == 0:

If remainder is 0:

Number is divisible
So it is NOT prime
Step 7 — Break Statement
break

Stops the loop immediately after finding a factor.

This improves efficiency.

Step 8 — Final Result
if prime:

If flag is still True
→ Prime Number

Else
→ Not Prime

Menu Driven System

The program runs continuously using:

while True:

Menu options:

Check Prime Number
Exit
Concepts Used
Concept	Purpose
Function	Reusable code
while loop	Infinite menu
for loop	Factor checking
if-else	Decision making
Flag Variable	Track prime status
break	Stop loop early
Time Complexity

Current Complexity:

O(n)

Because loop runs from:
2 → num-1
