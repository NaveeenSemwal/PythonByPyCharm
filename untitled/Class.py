class Person:
    # This is class variable
    gender = 'Male'

    # This age is instance variable

    def __init__(self, x):
        self.age = x

    def validate_age(self):
        if self.age > 21:
            print('You are eligible for voting')
        else:
            print('You are not eligible for voting')


obj1 = Person(12)
obj1.validate_age()

obj2 = Person(32)
obj2.validate_age()
