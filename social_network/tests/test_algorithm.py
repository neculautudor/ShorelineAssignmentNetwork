import unittest
from algorithm import find_shortest_path_dijkstra, find_shortest_path_bfs
from network import Network
from person import Person


class TestAlgorithm(unittest.TestCase):
    def create_network(self):
        self.andrei = Person('Andrei', 0)
        self.ion = Person('Ion', 1)
        self.tudor = Person('Tudor', 2)
        self.giga = Person('Giga', 3)
        self.chad = Person('Chad', 4)
        self.andra = Person('Andra', 5)
        self.alex = Person('Alex', 6)
        self.teo = Person('Teo', 7)

        self.andrei.add_friends([self.ion, self.chad])
        self.ion.add_friends([self.andrei, self.chad, self.tudor])
        self.tudor.add_friends([self.ion, self.giga, self.teo])
        self.giga.add_friends([self.tudor, self.teo])
        self.chad.add_friends([self.andrei, self.ion, self.andra])
        self.andra.add_friends([self.chad, self.alex])
        self.alex.add_friends([self.andra, self.teo])
        self.teo.add_friends([self.alex, self.giga, self.tudor])

        self.test_network = Network('Social Network', dict())
        self.test_network.add_multiple_people([self.andrei, self.ion, self.tudor, self.giga,
                                               self.chad, self.andra, self.alex, self.teo])

    def test_find_shortest_path_normal(self):
        self.create_network()
        result = find_shortest_path_bfs(self.test_network, self.andrei, self.teo)
        self.assertEqual(result, [self.andrei, self.ion, self.tudor, self.teo])

    def test_find_shortest_path_no_link(self):
        self.create_network()
        self.teo.friends = set()
        self.tudor.friends.remove(self.teo)
        self.giga.friends.remove(self.teo)
        self.alex.friends.remove(self.teo)
        """teo now has no friends, therefore there should be no link"""
        with self.assertRaises(BaseException) as context:
            find_shortest_path_bfs(self.test_network, self.andrei, self.teo)
        self.assertEqual('There is no path available between the two chosen nodes', str(context.exception))

    def test_find_shortest_path_improper_type(self):
        self.create_network()
        # result = find_shortest_path_bfs(None, self.andrei, self.teo)
        # self.assertEqual(result, -1)
        with self.assertRaises(TypeError) as context:
            find_shortest_path_bfs(None, self.andrei, self.teo)
        self.assertTrue('ERROR: Network type does not fit' in str(context.exception))


    def test_find_shortest_path_normal2(self):
        self.create_network()
        self.andrei.friends.remove(self.ion)
        self.ion.friends.remove(self.andrei)
        """the link between vertex 0 and 1 is removed, so the result should be different"""
        result = find_shortest_path_bfs(self.test_network, self.andrei, self.teo)
        possible_answers = [[self.andrei, self.chad, self.ion, self.tudor, self.teo],
                            [self.andrei, self.chad, self.andra, self.alex, self.teo]]
        self.assertIn(result, possible_answers)

    def test_find_shortest_path_normal3(self):
        self.create_network()
        result = find_shortest_path_bfs(self.test_network, self.ion, self.andra)
        possible_answer = [self.ion, self.chad, self.andra]
        self.assertEqual(result, possible_answer)

    def test_find_shortest_path_normal4(self):
        self.create_network()
        jon = Person('Jon', 8)
        jon.add_friends([self.andrei, self.andra])
        self.andra.add_friend(jon)
        self.andrei.add_friend(jon)
        self.test_network.add_people(jon)
        result = find_shortest_path_bfs(self.test_network, self.ion, jon)
        possible_answer = [self.ion, self.andrei, jon]
        self.assertEqual(result, possible_answer)

    def test_add_same_person(self):
        self.create_network()
        length = len(self.test_network.people)
        self.test_network.add_people(self.teo)
        new_length = len(self.test_network.people)
        self.assertEqual(length, new_length)

    def test_add_self_to_friends(self):
        jon = Person('jon', 9)
        jons_initial_friends = jon.friends
        jon.add_friend(jon)
        self.assertEqual(jons_initial_friends, jon.friends)

