import astar

MAP_ROW = 7
MAP_COL = 5
map = [[1,1,1,1,1],
       [1,0,0,0,1],
       [1,1,1,0,1],
       [1,0,0,0,1],
       [1,0,1,1,1],
       [1,0,0,0,1],
       [1,1,1,1,1]]

def is_outside_map(x, y):
    if x < 0 or x > MAP_COL-1 or y < 0 or y > MAP_ROW-1:
        return True
    return False

def is_block(x, y):
    if map[y][x] == 1:
        return True
    return False

def is_movable(p):
    x, y = p
    if is_outside_map(x, y):
        return False
    if is_block(x, y):
        return False
    return True

def neighbor_nodes(p):
    x, y = p
    neighbors = [(x-1, y), (x, y-1), (x+1, y), (x, y+1)]
    return filter(is_movable, neighbors)

def heuristic_cost_estimate(p1, p2):
    return manhattan_distance(p1, p2)

def manhattan_distance(p1, p2):
    return abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)

if __name__ == '__main__':
    start = (2, 2)
    goal  = (1, 1)
    path  = astar.astar(start, goal, neighbor_nodes, heuristic_cost_estimate, heuristic_cost_estimate)
    if path:
        print("====")
        for position in reversed(path):
            x,y = position
            print(x,y)
