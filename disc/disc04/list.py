def even_weighted(s):
    """A function that takes a list s and returns a new list that keeps only the even-indexed elements of s and mutiplies them by their corresponding index."""
    return [i * s[i] for i in range(0,len(s)) if i % 2 == 0]

