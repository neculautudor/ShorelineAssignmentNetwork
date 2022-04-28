class Network:
    def __init__(self, name, people: dict):
        self.name = name
        self.people = people

    def add_people(self, person):
        self.people[person.id] = person

    def add_multiple_people(self, people: list):
        for person in people:
            if person.id in self.people:
                print('ERROR: Person with id ', person.id, 'already exists!')
            self.add_people(person)

