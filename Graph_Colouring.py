import networkx as nx
import matplotlib.pyplot as plt
import random
import numpy as np

def create_2d_lattice(m, n):
    
    #Create a 2D lattice of size m x n.
    G = nx.grid_2d_graph(m, n, periodic=False)
    # Convert to a regular graph from a grid graph for easier manipulation
    G = nx.convert_node_labels_to_integers(G)
    return G

def assign_initial_colors(G, num_colors):
   
    #Randomly assign initial colors to each node in the graph.
    for node in G.nodes():
        G.nodes[node]['color'] = random.randint(1, num_colors)

def resolve_conflicts(G, num_colors):
    
    #Attempt to resolve color conflicts in the graph, returns the number of iterations taken to resolve all conflicts.
    
    iterations = 0
    while True:
        conflict_nodes = []
        for node in G.nodes():
            neighbor_colors = [G.nodes[neighbor]['color'] for neighbor in G.neighbors(node)]
            if neighbor_colors.count(G.nodes[node]['color']) > 0:
                conflict_nodes.append(node)
        
        if not conflict_nodes:
            break
        
        for node in conflict_nodes:
            neighbor_colors = [G.nodes[neighbor]['color'] for neighbor in G.neighbors(node)]
            available_colors = [color for color in range(1, num_colors + 1) if color not in neighbor_colors]
            if available_colors:
                G.nodes[node]['color'] = random.choice(available_colors)
        
        iterations += 1
    return iterations

def visualize_graph(G):
    
    #Visualize the graph with nodes colored according to their assigned color.
    colors = [G.nodes[node]['color'] for node in G.nodes()]
    pos = {node: (node % m, -node // m) for node in G.nodes()}  # Position nodes in a grid
    nx.draw(G, pos, node_color=colors, with_labels=False, node_size=40, cmap=plt.cm.jet)
    plt.show()

# Parameters
m, n = 5, 5  # Dimensions of the lattice
num_colors = 4  # Number of colors

# Create a 2D lattice graph
G = create_2d_lattice(m, n)

# Assign initial colors
assign_initial_colors(G, num_colors)

# Resolve conflicts and print the number of iterations
iterations = resolve_conflicts(G, num_colors)
print(f"Resolved conflicts in {iterations} iterations.")

# Visualize the final colored graph
visualize_graph(G)
