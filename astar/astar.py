import math

def astar(start, goal, neighbor_nodes, dist_between, heuristic_cost_estimate):
    closedset = []
    openset   = [start]
    came_from = {}
    g_score   = {}
    f_score   = {}
    g_score[start] = 0
    f_score[start] = g_score[start] + heuristic_cost_estimate(start, goal)
    while openset:
        current = min((f_score[node], node) for node in openset)[1]
        #print(f_score)
        #print(current)
        if current == goal:
            return reconstruct_path(came_from, goal)
        openset.remove(current)
        closedset.append(current)
        for neighbor in neighbor_nodes(current):
            tentative_g_score = g_score[current] + dist_between(current, neighbor)
            tentative_f_score = tentative_g_score + heuristic_cost_estimate(neighbor, goal)
            if neighbor in closedset and tentative_f_score >= f_score[neighbor]:
                continue
            if neighbor not in openset or tentative_f_score < f_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                #print(tentative_f_score)
                f_score[neighbor] = tentative_f_score
                if neighbor not in openset:
                    openset.append(neighbor)

    return None

def reconstruct_path(came_from, current_node):
    path = [current_node]
    #print(current_node)
    while current_node in came_from:
        current_node = came_from[current_node]
        #print(current_node)
        path.append(current_node)
    return path
