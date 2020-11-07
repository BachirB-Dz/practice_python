# Creating a program that asks the user for a number and then prints out a list of all the divisors of that number.
# I know the program could be a lot shorter, but I wanted to handle all the possibilities that I could think of.


def divisors():
    # If the input is neither an integer nor a float, the user is notified and asked to continue or not.
    # Otherwise, we have three possibilities: zero, a positive integer, or a negative integer.
    try:
        number = int(input('Write a number to get its divisors: '))
        divisors =  []
        if number == 0:
            print('All non-zero numbers are divisors of 0.')
        elif number != 0:
            for n in range(1,abs(number) + 1):
                if number % n == 0:
                    divisors.append(n)
            print(f'The divisors of {number} are: ' + str(divisors).replace('[','').replace(']',''))
        
        if divisors == [1,number]:
            print('Uh-oh, you\'ve got a prime number there.')
    
    except ValueError:
        print('Your input is invalid.')


def another():
    # The user is given the choice to continue with another number or finish the program.
    decision = input('Write "y" or "yes" to continue or anything else to quit: ')
    
    if decision.lower() in ['y', 'yes']:
        divisors()
        another()
    else:
        pass

divisors()
another()