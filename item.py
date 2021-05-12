class Item:
    def __init__(self, item_name: str, item_price: int, item_hashtags: list, item_description: str):
        self.name = item_name
        self.price = item_price
        self.hashtags = item_hashtags
        self.description = item_description

    '''function to compare between two items
      params:
        self - current instance of item
        other - iten
      :return boolean    
    '''

    def __eq__(self, other):
        return self.name == other.name and self.price == other.price and self.hashtags == other.hashtags and self.description == other.description

    def __str__(self) -> str:
        return f'Name:\t\t\t{self.name}\n' \
               f'Price:\t\t\t{self.price}\n' \
               f'Description:\t{self.description}'
