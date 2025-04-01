#import uuid

#version 1
# class Clothing:
#     def __init__(self,id = None,fabric = None):
#         self.id = uuid.uuid4().int if id is None else id
#         self.fabric = "Unknown" if fabric is None else fabric

#     def get_category(self):
#         return "Clothing"
    
#     def __str__(self):
#         return f"An object of type Clothing with id {self.id}. It is made from {self.fabric} fabric."
    


#version 2 - Using Inheritance
from swap_meet.item import Item
class Clothing(Item):
    def __init__(self,id = None,fabric = None, condition = None):
        super().__init__(id, condition)  #when using super, no need to pass in self again
        self.fabric = "Unknown" if fabric is None else fabric

    def __str__(self):  #override the __str__ in Item class as we need to print in different format
        return f"An object of type Clothing with id {self.id}. It is made from {self.fabric} fabric."