class graph():
    def __init__(self):
        self.adj_list = {}

    def print_graph(self):
        for vertex in self.adj_list:
            print(vertex, ":" , self.adj_list[vertex])

    def add_vertex(self, vertex):
        if vertex not in self.adj_list.keys():
            self.adj_list[vertex] = []
            return True
        return False

    def add_edge(self, v1, v2):
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            self.adj_list[v1].append(v2)
            self.adj_list[v2].append(v1)
            return True
        return False
    

    def remove_edge(self, v1, v2):
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            try:    
                self.adj_list[v1].remove(v2)
                self.adj_list[v2].remove(v1)
            except ValueError:  # HANDLING THE EDGE CASES
                pass
            return True
        return False
    

    def remove_vertex(self, vertex):
        if vertex in self.adj_list:
            for other_vertex in self.adj_list[vertex]:
                self.adj_list[other_vertex].remove(vertex)
            del self.adj_list[vertex]
            return True
        return False    

    

My_graph = graph()

My_graph.add_vertex("A")
My_graph.add_vertex("B")
My_graph.add_vertex("C")
My_graph.add_vertex("D")

My_graph.add_edge("A","B")
My_graph.add_edge("A","C")
My_graph.add_edge("A","D")
My_graph.add_edge("B","C")
My_graph.add_edge("B","D")

My_graph.remove_vertex("D")

My_graph.print_graph()