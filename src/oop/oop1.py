# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class

'''
parent class
'''


class Vehicle:
    def __init__(self):
        pass


'''
child classes: Base class is Vehicle for the following classes
'''


class FlightVehicle(Vehicle):
    def __init__(self):
        pass


class GroundVehicle(Vehicle):
    def __init__(self):
        pass


'''
Base class is FlightVehicle for the following classes
'''


class Starship(FlightVehicle):
    def __init__(self):
        pass


class Airplane(FlightVehicle):
    def __init__(self):
        pass


'''
Base class is GroundVehicle for the following classes
'''


class Car(GroundVehicle):
    def __init__(self):
        pass


class Motorcycle(GroundVehicle):
    def __init__(self):
        pass
