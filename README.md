# Birthdate-Day-Calculator
-----
Do you know on what day of the week you were born?  Today you will write a program to calculate it.
## Your Task
-----
Use the algorithm to calculate the day of the week on which you were born.

Write a function in Python named `zeller_function(month: int, day: int, year:int )` that: 
* Calculates and returns the appropriate day of the week that you were born on as a String.

Write a function called `main()` that:
* Asks the user for their birth month, day, and year.
* Then uses the reponses from the user and your `zeller_function(month: int, day: int, year:int )` function to calculate the day of the week the user was born on.
* Finally prints: "You were born on a *Monday*

### Rubric
Style - code format, whitespace and PEP-8 style is followed making code easy to read.

Comments - blocks of code are well commented.  Every function has a descriptive comment.

Tests - The program runs as described in the specifications without errors(passes all tests).

### Zeller’s Algorithm
-----
Zeller’s Algorithm is a way to calculate what day of the week a given date was.

Let month number = M
day number = D
year = Y

If M is 1 or 2, add 12 to M, and subtract 1 from Y.

Let C be the first two digits of Y and K be the last two digits of Y.

Add together the integer parts of (2.6M—5.39), (K/4) and (C/4). 

Add to this D and K, and subtract 2C. (The integer part of a number is the whole number part: integer part of 2.3 is 2, and of 6.7 is 6. Note that the integer part of –1.7 is –2).

Find the remainder when this number is divided by 7.

If this remainder is 0 the day is Sunday, 1 is Monday, 2 is Tuesday, etc.

### Example: May 15, 1991
-----
M = 5

D = 15

Y = 1991

C = 19

K = 91

(2.6M—5.39) = 7.61 = 7

(K/4) = 22.75 = 22

(C/4) = 4.75 = 4

7 + 22 + 4 + 15 + 91—38 = 101

101 ÷ 7 = 14 r 3

Remainder is 3, so May 15, 1991 was a Wednesday.


