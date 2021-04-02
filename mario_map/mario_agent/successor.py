class Successor:
    def __init__(self, element, position, father, g=None, h=None, f=None):
        self.position = position
        self.element = element
        self.h = h
        self.g = g
        self.f = g + h
        self.father = father

    def set_costs(self, h, g):
        self.h = h
        self.g = g
        self.f = g + h

