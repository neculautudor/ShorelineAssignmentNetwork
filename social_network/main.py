from algorithm import find_shortest_path
from network import Network
from person import Person


def create_network():
    """initializing all the persons and the connections between them and creating the network"""
    global social_network
    global andrei, ion, tudor, giga, chad, andra, alex, teo

    andrei = Person('Andrei', 0)
    ion = Person('Ion', 1)
    tudor = Person('Tudor', 2)
    giga = Person('Giga', 3)
    chad = Person('Chad', 4)
    andra = Person('Andra', 5)
    alex = Person('Alex', 6)
    teo = Person('Teo', 7)

    andrei.add_friends([ion, chad])
    ion.add_friends([andrei, chad, tudor])
    tudor.add_friends([ion, giga, teo])
    giga.add_friends([tudor, teo])
    chad.add_friends([andrei, ion, andra])
    andra.add_friends([chad, alex])
    alex.add_friends([andra, teo])
    teo.add_friends([alex, giga, tudor])

    social_network = Network('Social Network', dict())
    social_network.add_multiple_people([andrei, ion, tudor, giga, chad, andra, alex, teo])


if __name__ == '__main__':
    create_network()
    path = find_shortest_path(social_network, andrei, teo)
    if path:
        for person in path:
            print(person.name)
    else:
        print("There is no connection between the two people")
