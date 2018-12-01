try:

    age = int(input("Enter your age man !!\n"))
    if age > 21:
        print("You are eligible for the vote !!")
    else:
        print('You are under age man !!')
except ValueError:
    print('Invalid value of the age !!')
except ZeroDivisionError:
    print('Divide by Zero not allowed !!')
except:
    print('This is the generic error')

finally:
    print('This is final block !!')
