def hailstone(n):
    """Recall the halistone function from homework1.
    If n is even, divide by 2, if n is odd, mutiply it by 3 and add 1.
    Repeat the process unitil n is 1."""
    if n < 0:
        print("Invalid input")
        return 
    if n == 1:
        print(1)
        return 
    if n % 2 == 0:
        print(n)
        hailstone(n//2)
        return 
    if n % 2 == 1:
        print(n)
        hailstone((n * 3) + 1)
        return 

