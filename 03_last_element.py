"""
if lst == []:
        return None
    else:
        return lst[-1]
"""


def last_element(lst):
    """Return last item in list (None if list is empty.

        >>> nums = [1, 2, 3]
        >>> last_element(nums)
        3
        >>> last_element([]) is None
        True

    Make sure original list has not been mutated:

        >>> nums == [1, 2, 3]
        True
    """

# TODO: if lst (a truthy check)
    if len(lst) > 0:
        return lst[-1]
