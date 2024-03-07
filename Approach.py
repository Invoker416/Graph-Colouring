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

def assign_random_colors(G, num_colors):
    
    #Assign colors to each node completely at random.
    
    for node in G.nodes():
        G.nodes[node]['color'] = random.randint(1, num_colors)

def assign_clustered_colors(G, num_colors, clusters):
    
    #Assign colors to create clusters in the lattice, Clusters parameter defines how many nodes in a region get the same color.
    
    color = 1
    for i in range(0, G.number_of_nodes(), clusters):
        for j in range(i, min(i+clusters, G.number_of_nodes())):
            G.nodes[j]['color'] = color
        color = (color % num_colors) + 1

def resolve_conflicts(G, num_colors):
    
    #Resolve conflicts with a simple rule: if a conflict is detected, choose a new color. 
    #If no available color, skip to avoid IndexError. Returns the number of iterations to resolve conflicts.
    
    iterations = 0
    conflict_exists = True
    while conflict_exists:
        conflict_exists = False
        for node in G.nodes():
            neighbor_colors = [G.nodes[neighbor]['color'] for neighbor in G.neighbors(node)]
            if neighbor_colors.count(G.nodes[node]['color']) > 0:
                available_colors = [c for c in range(1, num_colors+1) if c not in neighbor_colors]
                if available_colors:
                    G.nodes[node]['color'] = random.choice(available_colors)
                    conflict_exists = True
                # If there are no available colors, this node's conflict remains unresolved for now
        iterations += 1
        if iterations > 1000:  # Add a stop condition to avoid infinite loops
            print("Stopped after 1000 iterations due to unresolved conflicts.")
            break
    return iterations


def visualize_graph(G, title):
    
    #Visualize the graph with nodes colored according to their assigned color.
    
    colors = [G.nodes[node]['color'] for node in G.nodes()]
    pos = {node: (node % m, -node // m) for node in G.nodes()}  # Grid position
    plt.figure(figsize=(8, 8))
    nx.draw(G, pos, node_color=colors, with_labels=True, node_size=40, cmap=plt.cm.jet)
    plt.title(title)
    plt.show()

m, n = 50, 50  # Lattice size
num_colors = 4  # Available colors
clusters = 5  # Nodes per cluster for clustered distribution

# Create the 2D lattice
G = create_2d_lattice(m, n)

# Experiment 1: Random Color Distribution
assign_random_colors(G, num_colors)
iterations_random = resolve_conflicts(G, num_colors)
visualize_graph(G, "Random Color Distribution")
print(f"Random Distribution: Resolved in {iterations_random} iterations.")

# Reset the graph for the next experiment
G = create_2d_lattice(m, n)

# Experiment 2: Clustered Color Distribution
assign_clustered_colors(G, num_colors, clusters)
iterations_clustered = resolve_conflicts(G, num_colors)
visualize_graph(G, "Clustered Color Distribution")
print(f"Clustered Distribution: Resolved in {iterations_clustered} iterations.")
