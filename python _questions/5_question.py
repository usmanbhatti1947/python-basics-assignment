# Question: Define a class which has at least two methods: 
# getString: to get a string from console input
#  printString: to print the string in upper case.
# Also please include simple test function to test the class methods.

# Hints: Use init method to construct some parameters
class StringManipulator:
    def __init__(self):
        self.input_string = ""

    def getString(self):
        self.input_string = input("Enter a string: ")

    def printString(self):
        print(self.input_string.upper())
def test_string_manipulator():
    sm = StringManipulator()
    sm.getString()
    sm.printString()
# Test the class methods
if __name__ == "__main__":
    test_string_manipulator()
# This will prompt the user to enter a string and then print it in uppercase.
# You can run this code in a Python environment to see how it works.