class Parent:

    def dispaly_last_name(self):
        print("semwal")


# This is the example of Inheritance
class Child(Parent):

    # If you declare same name function in child class that is function overridding

    # def dispaly_last_name(self):
    # print("sharma")

    def display_first_name(self):
        print("naveen")


pa = Child()
pa.display_first_name()
pa.dispaly_last_name()
