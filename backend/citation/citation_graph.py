import networkx as nx

class CitationGraph:

    def build_graph(self, references):

        G = nx.DiGraph()

        for ref in references:

            G.add_node(ref)

        return G