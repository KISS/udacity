import math 

def shortest_path(graph, start_node, end_node):
    if start_node == end_node:
        return [start_node]
    
    node_distances = dict() 
    unvisited = set() 
    
    # build our result and unvisited dictionaries
    for node in graph.intersections:
        cost_to_goal = get_cost_to_goal(graph, node, end_node)
        node_distances[node] = [float('inf'), cost_to_goal]
        unvisited.add(node)
        
    # update start_node path cost to 0 
    node_distances[start_node][0] = 0 
        
    # create path dictionary to track which nodes connect
    path = dict() 
    
    while unvisited:
        # select the next node to visit based on which one has the smallest path cost
        min_node = None 
        for node in unvisited:
            if not min_node:
                min_node = node
            else:
                if node_distances[min_node][0] > node_distances[node][0]:
                    min_node = node 
        
        # visit all neighbors (connecting intersections) of the node selected below
        neighbors = graph.roads[min_node]
        for neighbor in neighbors:
            if neighbor in unvisited:
                # calculate updated path cost of traveling to neighbor from current node 
                path_cost = node_distances[min_node][0] + get_cost_to_goal(graph, min_node, neighbor)
                heuristic = node_distances[neighbor][1]
                distance_to_neighbor = path_cost + heuristic
            
                if node_distances[neighbor][0] > distance_to_neighbor:
                    # update the path cost associated with visiting this neighbor next 
                    node_distances[neighbor][0] = distance_to_neighbor
                    # update our path from min_node -> neighbor 
                    path[neighbor] = min_node

        # mark selected node as visited 
        unvisited.remove(min_node)
    
    # iterate through path to build output 
    output = []
    # start at end_node
    node = end_node
    while node != start_node:
        if node in path:
            output.insert(0, node)
            node = path[node]
    # insert start node so long as we're sure a path exists
    if len(output):
        output.insert(0, start_node)
            
    # return path 
    return output     
    

# Uses Euclidean Distance to calculate cost to goal heuristic 
def get_cost_to_goal(graph, start_node, end_node):
    start_x_y = graph.intersections[start_node]
    goal_x_y = graph.intersections[end_node]
    dist = math.sqrt(math.pow(start_x_y[0] - goal_x_y[0], 2) + math.pow(start_x_y[1] - goal_x_y[1], 2))
    return round(dist)