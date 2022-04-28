from collections import deque

from network import Network
from person import Person


def find_shortest_path(nw: Network, start: Person, end: Person):
    if type(nw) != Network:
        print('ERROR: Network type does not fit')
        return -1
    if start not in nw.people.values():
        print('ERROR: starting node is not in the network')
        return -2
    if end not in nw.people.values():
        print('ERROR: end node is not in the network')
        return -3

    visited = {}
    distances = {}
    previous_path_node = {}
    for person in nw.people.values():
        visited[person] = False
        distances[person] = float('+inf')
    distances[start] = 0
    """all distances except the starting one is initiated with infinity as an upper bound"""

    def dijkstra(vertex: Person):
        """iterating through all the friends of the current person, the distance is updated"""
        for friend in vertex.friends:
            if distances[vertex] + 1 < distances[friend]:
                distances[friend] = distances[vertex] + 1
                previous_path_node[friend] = vertex

        """name and id are irrelevant for this node, it is used just as a first comparison"""
        min_distance_node = Person('fic', 13)
        fictional_node = min_distance_node
        distances[min_distance_node] = float('+inf')
        """the next smallest distance person is chosen"""
        for person in visited:
            if not visited[person] and distances[person] < distances[min_distance_node]:
                min_distance_node = person
        if min_distance_node == fictional_node:
            distances.pop(fictional_node)
            return

        distances.pop(fictional_node)
        visited[vertex] = True
        """the algorithm calls itself until there's no more unvisited nodes"""
        dijkstra(min_distance_node)

    dijkstra(start)

    """if there is no connection between the two people, the function returns 0"""
    if distances[end] == float('+inf'):
        return 0
    person = end
    path = deque()
    while person != start:
        path.appendleft(person)
        person = previous_path_node[person]
    path.appendleft(start)

    return list(path)


