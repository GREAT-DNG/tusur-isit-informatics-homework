def read_sharks(path):
    data = open(path, "r").read().splitlines()
    sharks = {}
    levels_buffer = [""] * 3
    for i in data:
        level = -1
        for j in range(4, 0, -1):
            if i.startswith(" " * 4 * (j-1)):
                level = j
                break
        if level < 4:
            levels_buffer[level-1] = i.lstrip()
            if level == 1: sharks[levels_buffer[0]] = {}
            elif level == 2: sharks[levels_buffer[0]][levels_buffer[1]] = {}
            elif level == 3: sharks[levels_buffer[0]][levels_buffer[1]][levels_buffer[2]] = {}
        else:
            i = i.lstrip()
            name, nickname = i.split(" : ")
            sharks[levels_buffer[0]][levels_buffer[1]][levels_buffer[2]][name] = nickname
    return sharks
