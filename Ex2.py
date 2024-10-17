# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 11:37:02 2024

@author: L13
"""

import networkx as nx
import matplotlib.pyplot as plt
import random
import time

# Function to generate a random graph
def generate_random_graph(num_vertices):
    G = nx.gnp_random_graph(num_vertices, 0.5)
    return G

# Welsh-Powell Algorithm for graph coloring
def welsh_powell_algorithm(G):
    nodes_sorted_by_degree = sorted(G.degree, key=lambda x: x[1], reverse=True)
    colors = {}
    available_colors = set(range(len(G.nodes)))

    for node, _ in nodes_sorted_by_degree:
        used_colors = {colors[neighbor] for neighbor in G.neighbors(node) if neighbor in colors}
        for color in available_colors:
            if color not in used_colors:
                colors[node] = color
                break

    chromatic_number = max(colors.values()) + 1
    return colors, chromatic_number

# Function to assign random colors and draw the graph
def draw_colored_graph(G, colors):
    random_colors = {node: f"#{random.randint(0, 0xFFFFFF):06x}" for node in G.nodes()}
    
    node_colors = [random_colors[node] for node in G.nodes()]
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color=node_colors, node_size=700, font_color='white')
    plt.show()
        

def main():
    start_time = time.time()
    num_vertices = int(input("Enter the number of vertices (summits) for the graph: "))
    
    G = generate_random_graph(num_vertices)
    
    colors, chromatic_number = welsh_powell_algorithm(G)
    
    print(f"Chromatic Number of the graph: {chromatic_number}")
    
    draw_colored_graph(G, colors)
    
    end_time = time.time()  # Enregistre le temps de fin
    total_execution_time = end_time - start_time  # Calcule le temps total d'exécution
    print(f"Total execution time: {total_execution_time:.6f} seconds")

if __name__ == "__main__":
    main()

