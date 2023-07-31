'''
Assignment 3  - Programming and Tools for AI (CT5132)

Student Names: Yamini Shailesh Girkar, Jash Prakash Rana
Student IDs: 22230186, 22222806
'''

import sys
import networkx as nx 
from itertools import combinations

# Using sys.argv to read the name of the text document
inf = open(str(sys.argv[1]),'r')

# Converting text file to dictionary
dicts = eval(inf.read())
inf.close()

# Graph Initialization
g = nx.Graph()

# Saving edges using dictionary values
edges = []
for i in dicts.values():
    edges.append(i)

# Function to create combinations from a sequence to spconnect neighbors of the edges 
def combinations(sequence, length, NULL=object()):
    if length <= 0:
        combos = [NULL]
    else:
        combos = []
        for i, item in enumerate(sequence, 1):
            rem_items = sequence[i:]
            rem_combos = combinations(rem_items, length-1)
            combos.extend(item if combo is NULL else [item, combo]
                            for combo in rem_combos)
    return combos

# Maintaining a list using the above function to make a set of 2 neighbors.
comb = []
for i in edges: 
  comb.append(combinations(i, 2))

# List to tuple conversion
def convert(list):
    return tuple(list)

# Making a list of edges for all the possible nodes
list_of_edges = []
for i in comb: 
  for j in i: 
   list_of_edges.append(convert(j))

# Adding edges to the NetworkX object
g.add_edges_from(list_of_edges)


try:
    # Trying to find the shortest path between two nodes in a file.
    print(nx.shortest_path(g,'Dracula','Pumpkin'))

except nx.NetworkXNoPath:
    # If there is no path, it will print out the following message
    print("The message is not reachable to Pumkin")