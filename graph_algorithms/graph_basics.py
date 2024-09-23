'''

    1. what is a graph? graph is just a collection of nodes and edges
            graph = nodes + edges
        nodes - visualise it as just a circle with some data inside them. (can also be called as vertices)
        edges - visualise it as a connection between pair of nodes.
    
    2. think of these nodes as just a things and edges as relationships, graph can simply be defined as a relationship
    between things. example: if nodes are considered as cities, then edges are the routes connecting them.

    3. directed graph - you can only move from source point to destination point if you have arrow head facing towards it

    4. undirected graph - can go in any direction unlike directed graphs. it doesn't have any specific direction.

    5. Traversing graph - depth first and breadth first traversal.
        a. DFT - exploring in single direction until we can't go in that direction i.e. until we reach last node in that direction
        b. BFT - exploring all the immediate neighbours first and expanding while doing it

    6. Depth first uses stack, Breadth first uses queue.

    7. cyclic and acyclic graph:
        a. cyclic - we end up into reaching the starting point during traversal and the loop will end up being infinite
        b. acyclic - we won't be able to traverse back to the source, and the loop will be finite.


'''

def depth_first_print(graph, source):
    stack = [source]
    while ( len(stack) > 0 ):
       current = stack.pop()
       print(current, end="->")
       stack.extend(graph[current])
    print(end="\n")

# depth_first_print using recursion
def depth_first_print_rec(graph, source):
    print(source, end="->")
    for neighbor in graph[source]:
        depth_first_print_rec(graph, neighbor)

def breadth_first_print(graph, source):
    queue = [source]
    while (len(queue) > 0):
        current = queue.pop(0) # poping out first element to mimic queueing behaviour
        print(current, end="->") 
        queue.extend(graph[current])

graph = {
    "a":['b', 'c'],
    "b":['d'],
    "c":['e'],
    "d":['f'],
    "e":[],
    "f":[],
}

depth_first_print(graph, "a")
depth_first_print_rec(graph, "a")
print()
breadth_first_print(graph, "a")

