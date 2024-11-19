#task 1
def groups_of_3(numbers):
    """
    Groups the elements of the input list into sublists of three elements each.
    input: (list[int]) A list of integers to be grouped.
    output: (list[list[int]]) A list of lists where each sublist contains up to three elements.
    """
    return [numbers[i:i + 3] for i in range(0, len(numbers), 3)]
