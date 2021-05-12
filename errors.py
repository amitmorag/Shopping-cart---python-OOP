class ItemNotExistError(Exception):
    def __init__(self):
        self.message = "The item is not exist"


class ItemAlreadyExistsError(Exception):
    def __init__(self):
        self.message = "The item is alrady exist"


class TooManyMatchesError(Exception):
    def __init__(self):
        self.message = "too many matches"
