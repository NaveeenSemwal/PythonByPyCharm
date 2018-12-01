class Parent:

    def dispaly_last_name(self):
        print("semwal")


class Child():

    def display_first_name(self):
        print("naveen")


# This is the example of multiple inheritance
class Dada(Parent, Child):
    pass    # This is keyword if your class is empty.


pa = Dada()
pa.display_first_name()
pa.dispaly_last_name()
