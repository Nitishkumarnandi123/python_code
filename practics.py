# import calendar
# yy = 1995
# mm = 3
# dd= 5
# print(calendar.month(yy,mm,dd))
########
# p= int(input("enter the number"))
# t=int(input("enter the time"))
# r=int(input("enter the number"))
# def m1(p,t,r):
#
#     si=(p*t*r)/100;
#     print (si)
# m1(p,t,r)
#####################################
class State:
    def __init__(self, name):
        self.name = name
        self.transportation = []

    def add_transportation(self, transport):
        self.transportation.append(transport)

    def __str__(self):
        return self.name


class Transportation:
    def __init__(self, mode):
        self.mode = mode
        self.data = {}

    def add_data(self, gender, men, women, children):
        self.data[gender] = {
            "Men": men,
            "Women": women,
            "Children": children
        }

    def __str__(self):
        return self.mode


# Creating instances of states
bihar = State("Bihar")
orissa = State("Orissa")
up = State("U.P")
jharkhand = State("Jharkhand")

# Creating instances of transportation
train = Transportation("Train")
bus = Transportation("Bus")

# Adding data to transportation instances
train.add_data("Men", 23500, 22658, 5927)
train.add_data("Women", 17237, 24555, 2364)
bus.add_data("Men", 36517, 23254, 19845)
bus.add_data("Women", 6314, 1336, 6314)

# Adding transportation to states
bihar.add_transportation(train)
orissa.add_transportation(train)
up.add_transportation(bus)
jharkhand.add_transportation(bus)

# Printing the data
for state in [bihar, orissa, up, jharkhand]:
    print(f"Destination State: {state}")
    for transport in state.transportation:
        print(f"{transport}:")
        for gender, data in transport.data.items():
            print(f"  {gender}: {data}")

