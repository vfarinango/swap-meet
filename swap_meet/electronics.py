from swap_meet.item import Item

class Electronics(Item):
    def __init__(self, id=None, type=None, condition=None, age=None):
        super().__init__(id, condition, age)
        self.type = "Unknown" if type is None else type
    
    def __str__(self):
        return f'An object of type Electronics with id {self.id}. This is a {self.type} device.'
        