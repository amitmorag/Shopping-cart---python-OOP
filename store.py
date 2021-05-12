import yaml
import errors
from item import Item
from shopping_cart import ShoppingCart


class Store:
    def __init__(self, path):
        with open(path) as inventory:
            items_raw = yaml.load(inventory, Loader=yaml.FullLoader)['items']
        self._items = self._convert_to_item_objects(items_raw)
        self._shopping_cart = ShoppingCart()

    '''
    convert the text to items
    '''
    @staticmethod
    def _convert_to_item_objects(items_raw):
        return [Item(item['name'],
                     int(item['price']),
                     item['hashtags'],
                     item['description'])
                for item in items_raw]

    '''return list of all the items in the current store'''

    def get_items(self) -> list:
        return self._items

    ''' we use this function to count the number of hashtags in lst1 that appears in lst2
      params:
            self
             lst1 - list of hashtags
             lst2 - list of hashtags
      :return int - the number of hashtags in lst1 that appears in lst2   
    '''

    def tags_calc(self, lst1: list, lst2: list) -> int:
        count = 0
        for i in lst1:
            count += lst2.count(i)
        return count

    ''' we use this function to sort the list of items by: first number of common hashtags, second by lexicographic order 
      params:
            self
            lst - list of items

      :return list - sorted list of items, first by common hashtags than by name 
    '''

    def sort_list(self, lst: list) -> list:
        # list of items that in the given list and not in the current instance of shopping cart items
        lst = [i for i in lst if i not in self._shopping_cart.get_items()]
        all_hashtags = [[tag for tag in i.hashtags] for i in self._shopping_cart.get_items()]
        all_hashtags = [tag for tags in all_hashtags for tag in tags]  # flatten the list of hashtags
        tmp = []
        for i in lst:
            # tuples of (item, sum of hashtags,name of item)
            tmp.append((i, self.tags_calc(i.hashtags, all_hashtags), i.name))
        tmp.sort(key=lambda i: i[2])  # sort by name
        tmp.sort(key=lambda i: i[1], reverse=True)  # sort by common hashtags - high first
        return [i[0] for i in tmp]

    ''' we use this function to search by given name(string) from the store with instance of string 
      the function returns a sorted list of all the items that match the search term 
      params:
            self
            item_name - string
      :return sorted list of items   
    '''

    def search_by_name(self, item_name: str) -> list:
        lst = [i for i in self.get_items() if item_name in i.name]
        return self.sort_list(lst)

    ''' we use this function to search by given hashtag from the store with instance of string 
      the function returns a sorted list of all the items that match the search term 
      params:
            self
            hashtag - string
      :return sorted list of items   
    '''

    def search_by_hashtag(self, hashtag: str) -> list:
        lst = [i for i in self.get_items() if hashtag in i.hashtags]
        return self.sort_list(lst)

    ''' we use this function to add an item to the store by given the item name  
      params:
            self
            item_name - string
      :return none  
    '''

    def add_item(self, item_name: str):
        lst = [i for i in self._items if item_name in i.name and i not in self._shopping_cart.get_items()]  # list of the item name matches
        if len(lst) == 0:
            raise errors.ItemNotExistError
        if len(lst) > 1:
            raise errors.TooManyMatchesError
        self._shopping_cart.add_item(lst[0])  # the method from the shopping cart class will check the itemAlradyExist
        return lst[0]

    ''' we use this function to remove an item to the store by given the item name  
      params:
            self
            item_name - string
      :return none  
    '''

    def remove_item(self, item_name: str):
        lst = [i for i in self._shopping_cart.get_items() if item_name in i.name]  # list of the item name matches
        if len(lst) == 0:
            raise errors.ItemNotExistError
        if len(lst) > 1:
            raise errors.TooManyMatchesError
        self._shopping_cart.remove_item(lst[0].name)
        return lst[0].name

    ''' we use this function to sum all the items in the current shopping cart  
      params: self
      :return sum - int  
    '''

    def checkout(self) -> int:
        return sum(i.price for i in self._shopping_cart.get_items())
