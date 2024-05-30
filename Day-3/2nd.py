class Student:
    def __init__(self, roll, name, phone, address):
        self.roll = roll
        self.name = name
        self.phone = phone
        self.address = address

    def displayInfo(self):
        print("Name:", self.name, "Phone:", self.phone)

# Creating instances with all required arguments
st1 = Student(1, 'Rohit', 93367999988, 'Address1')
st2 = Student(2, 'Dheeraj', 4749488448, 'Address2')

# Displaying information
st1.displayInfo()
st2.displayInfo()