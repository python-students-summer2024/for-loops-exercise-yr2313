"""
Helper functions for common unit test needs.
"""

# help debug the tests
import logging

logging.basicConfig(level=logging.DEBUG)


def get_fresh_function_mock_data():
    """
    Data used to track the behavior of a single function that will be tested.

    :returns: A blank data set to be used for one function.
    """
    data = {
        "params": {"actual": [], "expected": []},
        "returns": {"actual": [], "expected": []},
        "call_counter": 0,
    }
    return data


def get_fresh_mock_data(function_names):
    """
    Data used to track the behavior of all functions to be tested in this file.

    :returns: A blank data set to be used for all functions in this set of tests.
    """
    data = {}
    for f in function_names:
        data[f] = get_fresh_function_mock_data()
    return data


def get_mock_function(mock_data, function_name):
    log = logging.getLogger(function_name)
    log.debug("generating mock function")

    # create clean mock data, if none exists
    function_names = list(mock_data.keys())
    if function_name not in function_names:
        # create it
        log.debug("initializing data")
        mock_data[function_name] = get_fresh_function_mock_data()

    # create a mock function to return
    def smock(f_name, *args):
        log = logging.getLogger(f_name)
        mock_data[f_name]["call_counter"] += 1
        mock_data[f_name]["params"]["actual"] += args[0]
        # log.debug('call counter: {}'.format(mock_data[f_name]['call_counter']))
        # if f_name == 'loopy_turtles.pick_up_and_move_turtle':
        #   log.debug('params: {}'.format(mock_data[f_name]['params']))

    # return it
    return smock
