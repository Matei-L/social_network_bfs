class Graph:
    def __init__(self):
        self.number_of_nodes = 0
        self.nodes = []

    def add_node(self, node):
        self.nodes += [node]
        self.number_of_nodes += 1

    def add_edge(self, first_index, second_index):
        if 0 < first_index < self.number_of_nodes and 0 < second_index < self.number_of_nodes:
            self.nodes[first_index].neighbours += [second_index]
            self.nodes[second_index].neighbours += [first_index]

    def get_shortest_path(self, starting_index, target_index):
        """
        This function is used in order to get the shortest path between the starting_node and the target_node inside
        the given social_network. It uses a BFS implementation which also saves the parents during the search in order to return
        the path at the end by backtracking using those values.
        :param: - social_network: a social_network returned by read_network(file_name)
                - starting_node: an index representing the starting node
                - target_node: an index representing the target node
        :return: the shortest path between starting_node and target_node and its size. The size is first.
        """

        # creating an empty queue
        queue = []

        # visiting the first node and adding it to the queue
        self.nodes[starting_index].visited = True
        self.nodes[starting_index].parent = -1
        queue.append(starting_index)

        # loop while the queue isn't empty and our target wasn't visited
        while len(queue) > 0 and not self.nodes[target_index].visited:
            # getting the new current node from the queue
            current_node_index = queue.pop(0)

            # we are looking at all its neighbours
            for neighbour_noode_index in self.nodes[current_node_index].neighbours:
                # checking if that neighbour was ever visited
                if not self.nodes[neighbour_noode_index].visited:
                    # if not, visiting the neighbour node and adding it to the queue
                    self.nodes[neighbour_noode_index].visited = True
                    self.nodes[neighbour_noode_index].parent = current_node_index
                    queue.append(neighbour_noode_index)

        # if I finished visiting the starting node's cluster and I didn't find the target inside it,
        # it means that there is no possible path between the starting node and the target node
        if not self.nodes[target_index].visited:
            return -1
        else:
            # if the target was visited, I will backtrack using the "parent" values
            current_node_index = target_index
            revesed_path = []

            while current_node_index != -1:
                revesed_path += [current_node_index + 1]
                current_node_index = self.nodes[current_node_index].parent

            return len(revesed_path) - 1
