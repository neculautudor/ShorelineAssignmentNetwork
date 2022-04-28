class Person:
    def __init__(self, name, id):
        self.name = name
        self.friends = set()
        self.id = id

    def add_friend(self, friend):
        self.friends.add(friend)
        if self in self.friends:
            self.friends.remove(self)
        """in case that a person adds themselves, we remove them afterwards"""

    def add_friends(self, friends):
        self.friends |= set(friends)
        """in case that a person adds themselves, we remove them afterwards"""
        if self in self.friends:
            self.friends.remove(self)

    def __str__(self) -> str:
        return self.name + ' --> ' + str([friend.name for friend in self.friends])


