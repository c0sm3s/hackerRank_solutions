def cuboid_volume(l):
    if type(l) not in [int, float]:
        raise TypeError("Not int nor float")
    return (l*l*l)