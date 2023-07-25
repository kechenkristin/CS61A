""" Sequence Iteration."""
def count_while(s,value):
    """Count the number of occurance of value in sequence s."""
    total, index = 0, 0
    while index < len(s):
        if s[index] == len(s):
            total += 1
        index += 1
    return total

def count_for(s, value):
    """Count the number of occurance of value in sequence s."""
    total = 0
    for element in s:
        if element == value:
            total += 1
    return total

# sequence unpacking
pairs = [[1,2],[2,2],[2,3],[4,4]]
same_count = 0

for x,y in pairs:
    if x == y:
        same_count += 1
