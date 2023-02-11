# Create a python class

class Point():
    # Define a method to create points:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

# Create an object
# p = Point(2, 8)

# print(f'{p.x} {p.y}')


class flight():
    # Method to create a new flight with a given capacity:
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []

   # Method to add a passenger to a flight:
    def add_passenger(self,name):
       if not self.open_seats():
          return False
       self.passengers.append(name)
       return True
    # Method to return number of open seats
    def open_seats(self):
        return self.capacity - len(self.passengers)   

# create a new flight with 3 passengers
flight = flight(3)

# create list of people
people = ['Harry','Ron','Hermoine','Ginny']

# attempt to add each in the list to a flight
for person in people:
    if flight.add_passenger(person):
       print(f'Added {person} to flight successfully')
    else:
        print(f'No available seats for {person}')   
