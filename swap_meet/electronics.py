from swap_meet.item import Item

class Electronics(Item):
    def __init__(self, id=None, type="Unknown", condition=0, age=0):
        super().__init__(id, condition, age)
        self.type = type
    
    def get_category(self):
        return "Electronics"

    def __str__(self):  
        item_message = super().__str__()
        electronics_message = f"This is a {self.type} device."
        return " ".join((item_message,electronics_message))
    
    # def __str__(self):
    #     return f'An object of type Electronics with id {self.id}. This is a {self.type} device.'
        