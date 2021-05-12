from item import Item
import errors


class ShoppingCart:

    '''
    constructor function, creates list of items
    :param self
    '''
    def __init__(self):
        self.cart = []

    '''
    return list of items of the current cart
    :param self
    :return self.cart
    '''

    def get_items(self):
        return self.cart

    '''
    Adds the given item to the shopping cart.
    if the item alrady exist raise ItemAlreadyExistsError
    :param
    self
    item - item 
    :return none
    '''

    def add_item(self, item: Item):
        if item in self.cart:
            raise errors.ItemAlreadyExistsError
        else:
            self.cart.append(item)

    '''
    removes the item from the shopping cart, if the function finds the item from given string.
    if the item doesnt exist raise ItemNotExistError
    :param
    self
    item name - string 
    :return none
    '''

    def remove_item(self, item_name: str):
        for i in self.cart:
            if i.name == item_name:
                self.cart.remove(i)
                return  # if we find item and delete so return
        raise errors.ItemNotExistError

    '''
    Returns the subtotal price of all the items currently in the shopping cart.
    :param
    self
    :return int
    '''

    def get_subtotal(self) -> int:
        return sum(i.price for i in self.cart)
