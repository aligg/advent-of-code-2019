def file_to_map():
    f = open("day6input.txt", "r")
    contents = f.readlines()
    orbits = dict()
    for line in contents:
        line = line.strip()
        line_list = line.split(")")
        if line_list[0] in orbits:
            orbits[line_list[0]].append(line_list[1])
        else:
            orbits[line_list[0]] = [line_list[1]]
    return orbits


def count_planet_children(planet, orbits):
    count = 0
    if planet not in orbits:
        return count
    curr_children = orbits[planet]
    count += len(curr_children)
    for child in curr_children:
        count += count_planet_children(child, orbits)
    return count


def find_total_orbits(orbits):
    sum_of_orbits = 0
    for planet in orbits:
        sum_of_orbits += count_planet_children(planet, orbits)
    print(sum_of_orbits)
    return sum_of_orbits


def find_path(current, target, orbits):
    path = []
    if current == target:
        path.append(current)
        return path
    else:
        if current not in orbits:
            return None
        direct_children = orbits[current]
        for child in direct_children:
            paths = find_path(child, target, orbits)
            if paths is not None:
                paths.append(current)
                return paths
        return None


def find_path_to_santa(start, end, orbits):
    path_to_you = set(find_path("COM", start, orbits))
    path_to_santa = set(find_path("COM", end, orbits))
    hops = path_to_you.symmetric_difference(path_to_santa)
    return len(hops) - 2


if __name__ == "__main__":
    orbits = file_to_map()
    find_total_orbits(orbits)
    path = find_path_to_santa("YOU", "SAN", orbits)
    print(path)
