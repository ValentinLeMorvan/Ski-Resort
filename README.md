Ski-Resort
==========

###Ski Resort - AG44 (Graph theory and applications) project

###Author

Valentin Le Morvan (valentinlemorvan@gmail.com)

###Objective

- Parsing a text file of data about a ski resort into a usable data structure representing it as a graph.

- Finding the shortest path in this graph

- Finding the reachable points from a given vertices, avoiding given edges.

###Implementation

The programm is writen in Python.

The graph is represented by 2 dictionnaries. One contain informations about the vertices, the other contain informations about the edges.

The shortest path is found using the Floyd-Warshall algorithm.

The reachable points are found using a depth-first search in the graph after removing the unwanted edges.
