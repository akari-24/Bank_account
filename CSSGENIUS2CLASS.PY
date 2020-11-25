# Python program to show that we can create
# instance variables inside methods

# Class for Computer Science Student
class CSSGenius2:

    # Class variable
    stream = 'Computer Science'

    # THe init method or constructor
    def __init__(self, classCode):

        # instance variable
        self.classCode = classCode

    # Adds and instance variable
    def setAddres =(self, address):
        self.address = address

    # Retrives instance variable
    def getAddress(self):
        return self.address
# Driver Code
a = CSSGenius2
a.setAddress("Noida, UP")
print(a.getAddress())
