def merge(n1,n2):
    # length of the two numbers
    l1 = len(str(n1))
    l2 = len(str(n2))

    # Initial indexes of first and second subarrays
    a = 0
    j = 0

    # Initial index of merged subaray array
    k = 0
    arr = []
    while (a < l1 and j < l2):
        if str(n1)[a] <= str(n2)[j]:
            arr[k] = str(n1)[a]
            a += 1
        else:
            arr[k] = str(n2)[j]
            j += 1
        k += 1

    # copy remaining elements of n1 if any
    while a < l1:
        arr[k] = str(n1)[a]
        a += 1
        k += 1

    # copy remaining elements of n2 if any
    while j < l2:
        arr[k] = str(n2)[j]
        j += 1
        k += 1

