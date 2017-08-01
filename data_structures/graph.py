"""
Implementing a graph data structure through Python
"""


#                                 Homework VII
#
#  Problem: Graph
#
#  Prompt: Create a Vertex class/constructor and Graph class/constructor.
#          Name it Graph.
#
#  The Vertex will have the following properties:
#
#               value: integer value (initially None)
#               edges: hash that contains edges to other vertices
#
#  The Graph will have the following properties:
#
#            vertices: A hash/dictionary/object to store vertices
#      total_vertices: The total number of vertices in your Graph
#         total_edges: The total number of edges in your Graph
#
#  The Graph will also have the following methods:
#
#          add_vertex: Method that accepts an id (int/str), and creates an
#                      object with a "value" of id, and a property called
#                      "edges" which will store the edges of the vertex. If a
#                      vertex with the id already exists, then do not create a
#                      new vertex.
#
#          get_vertex: Method that takes an id, and outputs the vertex with the
#                      matching id, if it exists.
#
#            add_edge: Method that accepts two different id's as its input, and
#                      creates an edge between both vertices.
#                      (This edge may look like [id1,id2])
#
#         remove_edge: Method that accepts two different id's as its input, and
#                      removes the edge between the two vertices if it exists.
#
#       remove_vertex: Method that takes an id as its input, and removes the
#                      vertex with the matching id.
#
#      find_neighbors: Method that accepts an id as its input, and returns
#                      all of the edges of that vertex.
#
#  Input:  N/A
#  Output: A Graph instance
#
#  What are the time and auxilliary space complexities of the various methods?



class Vertex(object):

    def __init__(self):
        self.edges = []
        self.id  = id



class Graph(object):

    def __init__(self, total_vertices, total_edges):
        self.vertices = {}
        self.total_verticies = total_vertices
        self.total_edges = total_edges


