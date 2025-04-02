from swap_meet.item import Item
class Clothing(Item):
    def __init__(self,id=None,fabric="Unknown", condition=0, age=0):
        super().__init__(id, condition, age)  
        self.fabric = fabric

    def get_category(self):
        return "Clothing"

    def __str__(self):  
        item_message = super().__str__()
        clothing_message = f"It is made from {self.fabric} fabric."
        return " ".join((item_message,clothing_message))
    
