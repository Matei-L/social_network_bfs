import sys

"""
Q&A:
1.  How did you represent the social network?  Why did you choose this representation?
    I have chosen to represent it as a graph. Each user is a node  and the friendship relationship is represented
    by edges. This structure is intuitive for this kind of problem and also, it can be easily implemented even if
    the users are more complex than just some positive integer indices.
2.  What algorithm did you use to compute the shortest chain of friends?  What alternatives did you consider? 
    Why did you choose this algorithm over the alternatives?
    I used a "breadth search first" implementation. First reading the problem I immediately thought of the 
    Dijkstra algorithm but I realised that weighted edges BFS is enough. I also considered A* but only with the
    given information I couldn't create a function which would help targeting the search towards the endpoint faster.
    BFS assures the optimal solution by looking first at the neighbours of distance 1, then of distance 2 and so on
    until it finds the target of finishes its queue. It is also fairly fast in O(n + m) where n is the number of nodes 
    and m the number of edges. 
3.  Please enumerate the test cases you considered and explain their relevance.
    - "complete" contains a complete graph with 9 nodes. Here any search between A and B with A =/= B should 
    return (2, [A, B]).
    - "isolated" contains a test case which has as target an isolated node. The result should be: (0, []).
    - "A_and_B_are_the_same" contains a test case where A == B. The result should be: (1, [2]).
    - "multiple_paths" contains a random graph with 9 nodes. There are multiple paths between A and B and also multiple 
    solutions. The result should be (4, [2, 3, 7, 9]).
"""


def read_network(file_name):
    """
    This function is used in order to read the graph representing the social network.
    :param: filename represents the name of a file having the following structure:
            - an integer representing the number of nodes inside the graph
            - two integers separated by one white space representing the starting node and the target node
            - a list of friendships, one on each row. A friendship is a pair of two nodes and is represented by
              two integers separated by one white space
    :except: "Invalid formatting", if the file doesn't respect the rules presented above
    :return: a dictionary representing the graph's representation for the following steps
    """
    INVALID_FORMATTING = "Invalid formatting"
    graph = dict()
    with open(file_name) as f:
        try:
            # reading the graph size
            first_line = f.readline()
            graph["graph_size"] = int(first_line)

            # saving the starting node and the target node
            second_line = f.readline()
            starting_node = int(second_line.split()[0]) - 1
            target_node = int(second_line.split()[1]) - 1
            # checking that the starting node and the target node are inside our graph
            if not 0 <= starting_node < graph["graph_size"] or \
                    not 0 <= target_node < graph["graph_size"]:
                raise Exception("The starting and target nodes must be inside the graph")

            # creating an empty graph with "graph size" nodes and and no edges
            graph["nodes"] = [{"index": index, "neighbours": [], "visited": False}
                              for index in range(graph["graph_size"])]
            # reading the edges one by one
            for line in f.readlines():
                # reading the edge and checking it is inside our graph
                first_index, second_index = (int(index) - 1 for index in line.split())
                if not 0 <= first_index < graph["graph_size"] and \
                        not 0 <= first_index < graph["graph_size"]:
                    raise Exception("The neighbours must be inside the graph")

                # adding the edge in both the first node's list
                # and the second one's list
                graph["nodes"][first_index]["neighbours"] += [second_index]
                graph["nodes"][second_index]["neighbours"] += [first_index]

        except Exception as e:
            raise Exception(INVALID_FORMATTING, *e.args)

    return graph, starting_node, target_node


def get_shortest_path(graph, starting_node, target_node):
    """
    This function is used in order to get the shortest path between the starting_node and the target_node inside
    the given graph. It uses a BFS implementation which also saves the parents during the search in order to return
    the path at the end by backtracking using those values.
    :param: - graph: a graph returned by read_network(file_name)
            - starting_node: an index representing the starting node
            - target_node: an index representing the target node
    :return: the shortest path between starting_node and target_node and its size. The size is first.
    """

    # creating an empty queue
    queue = []

    # visiting the first node and adding it to the queue
    graph["nodes"][starting_node]["visited"] = True
    graph["nodes"][starting_node]["parent"] = -1
    queue.append(starting_node)

    # loop while the queue isn't empty and our target wasn't visited
    while len(queue) > 0 and not graph["nodes"][target_node]["visited"]:
        # getting the new current node from the queue
        current_node_index = queue.pop(0)

        # we are looking at all its neighbours
        for neighbour_noode_index in graph["nodes"][current_node_index]["neighbours"]:
            # checking if that neighbour was ever visited
            if not graph["nodes"][neighbour_noode_index]["visited"]:
                # if not, visiting the neighbour node and adding it to the queue
                graph["nodes"][neighbour_noode_index]["visited"] = True
                graph["nodes"][neighbour_noode_index]["parent"] = current_node_index
                queue.append(neighbour_noode_index)

    # if I finished visiting the starting node's cluster and I didn't find the target inside it,
    # it means that there is no possible path between the starting node and the target node
    if not graph["nodes"][target_node]["visited"]:
        return 0, []
    else:
        # if the target was visited, I will backtrack using the "parent" values
        current_node_index = target_node
        revesed_path = []

        while current_node_index != -1:
            revesed_path += [current_node_index + 1]
            current_node_index = graph["nodes"][current_node_index]["parent"]

        return len(revesed_path), list(reversed(revesed_path))


if __name__ == '__main__':
    if len(sys.argv) > 1:
        file_name = sys.argv[1]
        print(get_shortest_path(*read_network(file_name)))
    else:
        print("Please provide the name of the file having the graph's structure as the first parameter.")
