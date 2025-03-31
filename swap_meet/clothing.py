import uuid

class Clothing:
    def __init__(self,id = None,fabric = None):
        self.id = uuid.uuid4().int if id is None else id
        self.fabric = "Unknown" if fabric is None else fabric

    def get_category(self):
        return "Clothing"
    
    def __str__(self):
        return f"An object of type Clothing with id {self.id}. It is made from {self.fabric} fabric."