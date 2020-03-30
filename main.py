import sys
import social_network.Reader as reader

"""
Q&A:
1.  How did you represent the social network?  Why did you choose this representation?
    I have chosen to represent it as a social_network. Each user is a node  and the friendship relationship is represented
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
    - "complete" contains a complete social_network with 9 nodes.
    - "isolated" contains a test case which has as target an isolated node.
    - "A_and_B_are_the_same" contains a test case where A == B.
    - "multiple_paths" contains a random social_network with 9 nodes. There are multiple paths between A and B and also multiple 
    solutions.
"""

if __name__ == '__main__':
    if len(sys.argv) > 1:
        file_name = sys.argv[1]
        expected_response, graph, starting_index, target_index = reader.read_test_file(file_name)
        print(f'{expected_response} = {graph.get_shortest_path(starting_index, target_index)}')
    else:
        print("Please provide the name of the file having the social_network's structure as the first parameter.")
