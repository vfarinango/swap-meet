from swap_meet.item import Item
class Clothing(Item):
    def __init__(self,id = None,fabric = None, condition = None, age=None):
        super().__init__(id, condition, age)  #when using super, no need to pass in self again
        self.fabric = "Unknown" if fabric is None else fabric

    def __str__(self):  #override the __str__ in Item class as we need to print in different format
        return f"An object of type Clothing with id {self.id}. It is made from {self.fabric} fabric."