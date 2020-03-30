import social_network.Graph as graphs
import social_network.Node as nodes


def read_test_file(file_name):
    """
    This function is used in order to read a social_network test.
    :param: filename represents the name of a file having the following structure:
            - an integer representing the correct response
            - an integer representing the number of nodes inside the social_network
            - two integers separated by one white space representing the starting node and the target node
            - a list of friendships, one on each row. A friendship is a pair of two nodes and is represented by
              two integers separated by one white space
    :except: "Invalid formatting", if the file doesn't respect the rules presented above
    :return: expected_response, a graph object, start_node_index, target_node_index
    """
    INVALID_FORMATTING = "Invalid formatting"
    graph = graphs.Graph()
    with open(file_name) as f:
        try:
            # reading the social_network size
            first_line = f.readline()
            expected_response = int(first_line)

            second_line = f.readline()
            number_of_nodes = int(second_line)

            # saving the starting node and the target node
            third_line = f.readline()
            starting_node = int(third_line.split()[0]) - 1
            target_node = int(third_line.split()[1]) - 1
            # checking that the starting node and the target node are inside our social_network
            if not 0 <= starting_node < number_of_nodes or \
                    not 0 <= target_node < number_of_nodes:
                raise Exception("The starting and target nodes must be inside the social_network")

            # creating an empty social_network with "social_network size" nodes and and no edges
            for _ in range(number_of_nodes):
                graph.add_node(nodes.Node())
            # reading the edges one by one
            for line in f.readlines():
                # reading the edge and checking it is inside our social_network
                first_index, second_index = (int(index) - 1 for index in line.split())
                if not 0 <= first_index < graph.number_of_nodes and \
                        not 0 <= first_index < graph.number_of_nodes:
                    raise Exception("The neighbours must be inside the social_network")

                # adding the edge in both the first node's list
                # and the second one's list
                graph.add_edge(first_index, second_index)

        except Exception as e:
            raise Exception(INVALID_FORMATTING, *e.args)

    return expected_response, graph, starting_node, target_node
