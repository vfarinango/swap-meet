import uuid
class Item:
    def __init__(self,id = None,condition = None):
        self.id = uuid.uuid4().int if id is None else id
        self.condition = 0 if condition is None else condition
    
    def get_category(self):
        return self.__class__.__name__
    
    def __str__(self):
        return f'An object of type Item with id {self.id}.'
    
    def condition_description(self):
        #I assume condition 5 is the best?
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
    