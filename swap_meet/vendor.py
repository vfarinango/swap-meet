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
        # ------- Vicky's practice -------------
        #other_vendor = the friend the vendor is swapping with
        # my_item = the item that this vendor will give friend
        #their_item = the item that friend vendor will give this vendor


        #If the vendor's inventory doesn't contain my_item or the friend's
        #inventory doesn't contain their_item, return False


        #Remove my_item from the Vendor's inventory and add it to friend's
        #Remove their_item from other Vendor's inventory
        # and adds to this Vendor's inventory, return True

        
    















    #Jeslyn's practice
    def swap_items(self, other_vendor, my_item, their_item):
        #If the vendor's inventory doesn't contain my_item or the friend's
        #inventory doesn't contain their_item, return False
        if my_item not in self.inventory or their_item not in other_vendor.inventory:
            return False
        #Remove my_item from the Vendor's inventory and add it to friend's
        #Remove their_item from other Vendor's inventory
        # and adds to this Vendor's inventory, return True
        self.inventory.remove(my_item)
        other_vendor.inventory.append(my_item)
        other_vendor.inventory.remove(their_item)
        self.inventory.append(their_item)
        return True