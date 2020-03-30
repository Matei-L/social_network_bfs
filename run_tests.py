import social_network.Reader as reader


def run_test_case_from_file(file_name):
    expected_response, graph, starting_index, target_index = reader.read_test_file(file_name)
    return expected_response, graph.get_shortest_path(starting_index, target_index)


def test_isolated():
    expected_response, given_response = run_test_case_from_file('./tests/isolated')
    assert expected_response == given_response


def test_complete():
    expected_response, given_response = run_test_case_from_file('./tests/complete')
    assert expected_response == given_response


def test_multiple_paths():
    expected_response, given_response = run_test_case_from_file('./tests/multiple_paths')
    assert expected_response == given_response


def test_a_and_b_are_the_same():
    expected_response, given_response = run_test_case_from_file('./tests/A_and_B_are_the_same')
    assert expected_response == given_response
