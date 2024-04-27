from heapq import heappop, heappush


def find_path(node_list, goal):
    parent = goal
    path = []
    while parent is not None:
        path.append(parent)
        parent = node_list[parent].parent
        if parent in path:
            break
    return {'path': path}


def a_star(start, goal, node_list, heurestic_function):
    '''
    Finds the best path in node_list. Returns a dict with {'cost': , 'path': , 'closed_list': }

        Parameters:
            start (int): A integer indicating from where on the node list to start.
            goal (int): A integer indicating a goal in the node_list.
            node_list (list): List of nodes that have verticies and some values. (See src/algorithms/objects/node.py)
            heurestic_function (function): a function that takes in three inputs (position, goal, node_list) and spits out a heurestic estimate for the length of the route.

        Returns:
            Result (dict): A dictionary containing path, cost and closed_list aka. visited cells.
    '''
    size = len(node_list)
    closed_list = [False for _ in range(size)]
    open_list = []
    node_list[start].g = 0
    heappush(open_list, (0, start))
    while open_list:
        _, p = heappop(open_list)
        g = node_list[p].g
        closed_list[p] = node_list[p].g+1
        if goal == p:
            result = find_path(node_list, goal)
            result['cost'] = node_list[p].g
            result['closed'] = closed_list
            return result
        for cost, new_p in node_list[p].edges:
            if not closed_list[new_p]:
                new_g = cost + g
                h = heurestic_function(node_list, new_p, goal)
                new_f = h + new_g
                if node_list[new_p].f == float('inf') or node_list[new_p].f > new_f:
                    heappush(open_list, (new_f, new_p))
                    node_list[new_p].f = new_f
                    node_list[new_p].g = new_g
                    node_list[new_p].parent = p
    return False
