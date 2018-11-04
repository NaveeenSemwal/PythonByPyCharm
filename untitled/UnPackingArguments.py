def describe_myself(name, age, address):
    print(name, age, address)


describe_myself('naveen', '30', 'delhi')


# This is called unpacking of variables

myData = ['umesh', '32', 'U.P']
describe_myself(*myData)


