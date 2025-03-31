class Vendor:
    def __init__(self,inventory=None):  #check the slides
        self.inventory = [] if inventory is None else inventory
        
    def add(self, item_to_add):
        self.inventory.append(item_to_add)
        return item_to_add
    
    def remove(self, item_to_remove):
        if item_to_remove not in self.inventory:
            return False
        else:
            self.inventory.remove(item_to_remove)
            return item_to_remove
    
    def get_by_id(self, item_id):
        for item in self.inventory:
            if item.id == item_id:
                return item
        return None
    
    def swap_items(self, other_vendor, my_item, their_item):
        #If the vendor's inventory doesn't contain my_item or the friend's
        #inventory doesn't contain their_item, return False
        

        #Remove my_item from the Vendor's inventory and add it to friend's
        #Remove their_item from other Vendor's inventory
        # and adds to this Vendor's inventory, return True

        
    
