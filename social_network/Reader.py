import social_network.Graph as graphs
import social_network.Node as nodes


def read_network(file_name):
    """
    This function is used in order to read the social_network representing the social network.
    :param: filename represents the name of a file having the following structure:
            - an integer representing the number of nodes inside the social_network
            - two integers separated by one white space representing the starting node and the target node
            - a list of friendships, one on each row. A friendship is a pair of two nodes and is represented by
              two integers separated by one white space
    :except: "Invalid formatting", if the file doesn't respect the rules presented above
    :return: a dictionary representing the social_network's representation for the following steps
    """
    INVALID_FORMATTING = "Invalid formatting"
    graph = graphs.Graph()
    with open(file_name) as f:
        try:
            # reading the social_network size
            first_line = f.readline()
            graph.number_of_nodes = int(first_line)

            # saving the starting node and the target node
            second_line = f.readline()
            starting_node = int(second_line.split()[0]) - 1
            target_node = int(second_line.split()[1]) - 1
            # checking that the starting node and the target node are inside our social_network
            if not 0 <= starting_node < graph.number_of_nodes or \
                    not 0 <= target_node < graph.number_of_nodes:
                raise Exception("The starting and target nodes must be inside the social_network")

            # creating an empty social_network with "social_network size" nodes and and no edges
            graph.nodes = [nodes.Node() for _ in range(graph.number_of_nodes)]
            # reading the edges one by one
            for line in f.readlines():
                # reading the edge and checking it is inside our social_network
                first_index, second_index = (int(index) - 1 for index in line.split())
                if not 0 <= first_index < graph.number_of_nodes and \
                        not 0 <= first_index < graph.number_of_nodes:
                    raise Exception("The neighbours must be inside the social_network")

                # adding the edge in both the first node's list
                # and the second one's list
                graph.nodes[first_index].neighbours += [second_index]
                graph.nodes[second_index].neighbours += [first_index]

        except Exception as e:
            raise Exception(INVALID_FORMATTING, *e.args)

    return graph, starting_node, target_node
