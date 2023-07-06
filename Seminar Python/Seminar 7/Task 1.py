from math import pi


def find_farthest_orbit(find_farthest):
    data = list(filter(lambda x: x[0] != x[1], find_farthest))
    print(data)
    result = list(map(lambda x: x[0]*x[1]*pi, data))
    print(result)
    return find_farthest[result.index(max(result))]


orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
print(find_farthest_orbit(orbits))
