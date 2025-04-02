import uuid
class Item:
    def __init__(self,id=None,condition=0, age=0):
        if id is not None and not isinstance(id, int):
            raise TypeError ("id must be an integer")
        self.id = uuid.uuid4().int if id is None else id
        self.condition = condition 
        self.age = age 
    

    def get_category(self):
        #return self.__class__.__name__
        return "Item"
    

    def __str__(self):
        return f'An object of type {self.get_category()} with id {self.id}.'
    

    def condition_description(self):
        if self.condition == 5:
            return "New"
        elif self.condition == 4:
            return "Like new"
        elif self.condition == 3:
            return "Very Good"
        elif self.condition == 2:
            return "Good"
        elif self.condition == 1:
            return "Acceptable"
        elif self.condition == 0:
            return "Heavily Used"
        
    