# compute the minimum perimeter of a rectangle, given its area
def width(area, height):
    assert area % height == 0
    return area // height


def perimeter(width, height):
    return 2 * width + 2 * height


def minimum_perimeter(area):
    heights = divisors(area)
    perimeters = [perimeter(width(area,h),h) for h in heights]
    return min(perimeters)