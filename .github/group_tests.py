#task 1
from group import groups_of_3

def test_groups_of_3():
    """
    Tests the groups_of_3 function with various input cases.
    """
    #test 1
    assert groups_of_3([1, 2, 3, 4, 5, 6, 7, 8, 9]) == [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    #test 2
    assert groups_of_3([1, 2, 3, 4, 5, 6, 7, 8]) == [[1, 2, 3], [4, 5, 6], [7, 8]]

    #test 3
    assert groups_of_3([1, 2]) == [[1, 2]]

    print("All tests passed!")

if __name__ == "__main__":
    test_groups_of_3()



