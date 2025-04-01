from swap_meet.item import Item

class Electronics(Item):
    def __init__(self, id=None, type=None, condition=None):
        super().__init__(id, condition)
        self.type = "Unknown" if type is None else type

    def get_category(self):
        return f"Electronics"
    
    def __str__(self):
        return f'An object of type Electronics with id {self.id}. This is a {self.type} device.'
        

# -------------------------------------------------
# ---- Questions for code review w/ Jeslyn --------
# -------------------------------------------------

# What is the difference between: 
# class Electronics(Item):
    # pass
    ## Makes child class Electronics inherit all inherit all
    ## the properties and methods from the parent class Item.

# And

# class Electronics(Item):
    # def __init__(self,id=None,type = None,condition = None):
    ## Adds an __init__() function to the child class that overrides 
    ## the inheritance of the parent's __init__() function.

    ## ** Note: The difference is that the first one is used
    ## when you don't want to add any other methods or properties to 
    ## the child class. Else, you add an __init__() function to add
    ## in this case, type property, to Electronics child class. This 
    ## is because we want to add more methods to this class.
