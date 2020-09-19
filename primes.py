#Prime number sieve in Python

MAXNUMBER = 1000                #Total number of numbers to test
results = []                    #Create list to store the results

for x in range (1,MAXNUMBER):   #Begin outer for loop to test all numbers between 1 and MAXNUMBER
    isprime = True              #Set boolean variable isprime to True
    for y in range (2, x - 1):  #Begin inner for loop. The divisiors shall be every number between (but not including) 1 and the number itself
        if x % y == 0:          #Check to see if the remainder of x divided by y is 0. If so, carry out next bit of code.
            isprime = False     #If so, set isprime to False. It's not a prime, in other words.
            break               #Break out of the loop if the number isn't prime. There's no point of continuing to test this number.
    if isprime == True:         #Following the tests, if x/y was never found to have a remainder of 0, set isprime to True
        results.append(x)       #If so, add the prime number to the list
        message = str(x) + " is a prime"; #Create notification string that current number is prime
        print (message)         #Print notification that current number is prime

def show_results():             #Define a funtion to show the results
    print ("The complete list of primes between 1 and "+str(MAXNUMBER)) # Print text explaining what the list is
    for x in results:           #Begin a for loop that visits every result in the list
        print (x),              #Print current entry in the list

show_results()                  #Call the function that shows the results that are stored in the list
