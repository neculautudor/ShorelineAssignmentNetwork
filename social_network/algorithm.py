from collections import deque
from logging import exception

from network import Network
from person import Person


def find_shortest_path_bfs(nw: Network, start: Person, end: Person):
    if type(nw) != Network:
        raise TypeError('ERROR: Network type does not fit')
    if start not in nw.people.values():
        raise TypeError('ERROR: starting node is not in the network')
    if end not in nw.people.values():
        raise TypeError('ERROR: end node is not in the network')

    visited = {}
    """visited: in this dictionary we save all the nodes and True if they've been visited, False otherwise """
    previous_path_node = {}
    """previous_path_node: Each node will have a corresponding previous node, the one who updated it last"""
    nodes_queue = deque([start])
    """in the nodes_queue we store the nodes that need to be iterated in a breadth first search"""
    path = deque([end])
    for person in nw.people.values():
        visited[person] = False
    visited[start] = True

    while len(nodes_queue):
        """when there are no more nodes in the queue, it stops"""
        cur_node = nodes_queue.popleft()
        """the first node in the queue is popped and used for adding its adjacent unvisited nodes to
        the queue and marking them as visited"""
        for node in cur_node.friends:
            if node == end:
                """if the end node is reached, it is certainly found through the shortest path, due to
                the BFS search and the fact that the graph is unweighted"""
                while cur_node != start:
                    """the path is being populated and returned"""
                    path.appendleft(cur_node)
                    cur_node = previous_path_node[cur_node]
                path.appendleft(cur_node)
                return list(path)

            if not visited[node]:
                visited[node] = True
                nodes_queue.append(node)
                previous_path_node[node] = cur_node
    """if the path hasn't been returned, then this code is reached and raises and exception"""
    raise BaseException('There is no path available between the two chosen nodes')




def find_shortest_path_dijkstra(nw: Network, start: Person, end: Person):
    if type(nw) != Network:
        raise exception('ERROR: Network type does not fit')
    if start not in nw.people.values():
        raise exception('ERROR: starting node is not in the network')
    if end not in nw.people.values():
        raise exception('ERROR: end node is not in the network')

    visited = {}
    """visited: in this dictionary we save all the nodes and True if they've been visited, False otherwise """
    distances = {}
    """distances: the shortest distances to a node from the starting one are saved and updated here"""
    previous_path_node = {}
    """previous_path_node: Each node will have a corresponding previous node, the one who updated it last"""
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


