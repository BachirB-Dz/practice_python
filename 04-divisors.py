# Creating a program that asks the user for a number and then prints out a list of all the divisors of that number.


def divisors():
    try:
        number = int(input('Write a number to get its divisors: '))
        divisorList =  []
        if number == 0:
            print('All non-zero numbers are divisors of 0.')
        else:
            for n in range(1,abs(number) + 1):
                if number % n == 0:
                    divisorList.append(n)
            print(f'The divisors of {number} are: ' + str(divisorList).replace('[','').replace(']',''))
        
        if divisorList == [1,number]:
            print('Uh-oh, you\'ve got a prime number there.')
        
        if input('Write "y" or "yes" to continue or anything else to quit: ').lower() in ['y', 'yes']:
            divisors()
        else:
            pass

    except ValueError:
        print('Your input is invalid.')
        divisors()


divisors()
