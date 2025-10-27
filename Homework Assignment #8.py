Python 3.13.7 (v3.13.7:bcee1c32211, Aug 14 2025, 19:10:51) [Clang 16.0.0 (clang-1600.0.26.6)] on darwin
Enter "help" below or click "Help" above for more information.
>>>         #HOMEWORK ASSIGNMENT #7
>>>     #CHAPTER 8 DISCUSSION QUESTION 1
>>> #1a)    A definite loop runs a specific number of times, usually using a for loop when the number of repetitions is known in advance. An indefinite loop, usually written with a while loop. It keeps running until a certain condition is met, making the number of repetitions unpredictable.
>>> #1b)    A for loop is used when you know in advance how many times you want to repeat a set of statements, usually looping through a sequence or range of numbers. But a while loop is used when you don’t know beforehand how many times the loop should run, it continues executing as long as a given condition remains true.
>>> #1c)    An interactive loop keeps running until the user decides otherwise, after each repitition the program will "ask the user" if they want to continue running the loop. While a sentinel loop repeats until a specific value, called a sentinel is entered. this will signal the program to stop repeating the code
>>> #1d)    Like i said above the sentinel loop runs until a sentinel value is entered by the user and the program will then stop repeating the code. but an end-of-file loop continues to read the input until it reaches the end of the file like the title says, or the end of the input stream. where it will then stop running automatically once there is no more data available, rather than relying on a special sentinel value
>>>     #CHAPTER 8 DISCUSSION QUESTION 2
>>> #2a) only True when both P and Q are not true
>>> #2b) True only if P is false and Q is true
>>> #2c) True if at least one of either P or Q is false
>>> #2d) True if either both P and Q are true or R is false
>>> #2e) True if P or R is true and q or R is true
>>>     #CHAPTER 8 DISCUSSION QUESTION 3
>>> #3a) n =int(input("Enter a positive integer n: ")) #this gets the n from user
>>> #    total =0
>>> #    i =1 #this starts the counting from 1 rather than 0
>>> #    while i <=n:
>>> #         total = total +i #this adds the current value to the recurring total
>>> #         i =i+1 #this moves onto the next number in sequence after we add the current number to our total
>>> #    print("The sum of the first", n, "counting numbers is: ", total)
>>> #3b) total =0
>>> #    number =int(input("Enter a number(999 to stop): "))
#    while number !=999:
#         total =total+number #add curent number to our total
#         number =int(input("Enter a number(999 to stop): ")) #this gets our next number from the user
#    print("The sum of the numbers entered is: ", total)
    #CHAPTER 8 PROGRAMMING EXERCISE 1
def ch8_prg1():
    n =int(input("Enter which Fibonacci number you want: ")) #getting user input
    first =1
    second =1 #first two terms in the sequence is 1
    
    if n <=2: #this is for if they want the first or second term in the sequence cus they dont follow the rest of the terms pattern
        fib =1
    else:
        count =3 #we start at 3 cus its the 3rd term and we are adding based off of that 3rd term
        while count <=n:
            fib =first+second
            first =second
            second -fib
            count =count+1
    print("The", n, "th term in the Fibonacci sequence is: ", fib)

    
ch8_prg1
<function ch8_prg1 at 0x105b45260>
ch8_prg1()
Enter which Fibonacci number you want: 5
The 5 th term in the Fibonacci sequence is:  2
ch8_prg1()
Enter which Fibonacci number you want: 7
The 7 th term in the Fibonacci sequence is:  2
def ch8_prg1():
    n =int(input("Enter which Fibonacci number you want: ")) #getting user input
    first =1
    second =1 #first two terms in the sequence is 1

    if n <=2: #this is for if they want the first or second term in the sequence cus they dont follow the rest of the terms pattern
        fib =1
    else:
        count =3 #we start at 3 cus its the 3rd term and we are adding based off of that 3rd term
        while count <=n:
            fib =first+second
            first =second
            second =fib
            count =count+1
    print("The", n, "th term in the Fibonacci sequence is: ", fib)

    
ch8_prg1()
Enter which Fibonacci number you want: 7
The 7 th term in the Fibonacci sequence is:  13
#had a typo, put "second -fib" instead of "second =fib"
    #CHAPTER 8 PROGRAMMING EXERCISE 4
def ch8_prg4():
    n =int(input("Enter a starting value for the Syracuse sequence: "))#get our user input
    print("Syracuse Sequence:") #looks better having the title of our list on a different line than the actual list
    while n !=1:
        print(n, end="->")#arrows between each number for easier undersatnding
        if n %2 ==0: #checks if n is even cus all numbers that are divisible by 2, or in this case have no remainders when dividing by 2
        n =n//2 #use int division
        
SyntaxError: expected an indented block after 'if' statement on line 6
def ch8_prg4():
    n =int(input("Enter a starting value for the Syracuse sequence: "))#get our user input
    print("Syracuse Sequence:") #looks better having the title of our list on a different line than the actual list
    while n !=1:
        print(n, end="->")#arrows between each number for easier undersatnding
        if n %2 ==0: #checks if n is even cus all numbers that are divisible by 2, or in this case have no remainders when dividing by 2
            n =n//2 #use int division
        else:
            n = 3*n +1 #for when n is odd
    print(n) #display the list of numbers in order

    
ch8_prg4()
Enter a starting value for the Syracuse sequence: 45
Syracuse Sequence:
45->136->68->34->17->52->26->13->40->20->10->5->16->8->4->2->1
