# Tree Recursion
def fib(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    else:
        return fib(n - 2) + fib(n - 1)


def count_stair_ways(n):
    """
    You want to go up a flight of stairs that has n steps. You can either take 1
    or 2 steps each time. How many different ways can you go up this flight of
    stairs? 

    count_stair_ways(n - 1) represents the number of different ways to go up
    the last n ? 1 stairs (this is the case where we take 1 step as our move).
    count_stair_ways(n - 2) represents the number of different ways to go up
    the last n ? 2 stairs (this is the case where we take 2 steps as our move).
    Our base cases will take care of the remaining 1 or 2 steps.

    >>> count_stair_ways(3)
    3
    """

    if n == 0:
        return 1
    elif n == 1:
        return 1
    return count_stair_ways(n-1) + count_stair_ways(n-2)
