import json
import networkx as nx
import matplotlib.pyplot as plt
from graphviz import Digraph


def graphviz_graph(filename):
    with open(f".\json_data\{filename}", "r") as file:
        arango_graph = json.load(file)

    graph_name = filename

    g = Digraph(graph_name, filename=f".\graphs\{graph_name}", format='jpeg', engine='neato')
    g.attr(scale='2', label='Searching with starting node', fontsize='18')
    g.attr('node', shape='circle', fixedsize='false', width='0.5')

    for item in arango_graph:
        for vertex in item['vertices']:
            g.node(vertex['_id'], label=vertex['_key'])
        for edge in item['edges']:
            g.edge(edge['_from'], edge['_to'])

    # Render to file into some directory
    # g.render(directory='/tmp/', filename=graph_name)

    # Or just show rendered file using system default program
    g.view()


def networkx_graph(filename):
    with open(f".\json_data\{filename}") as file:
        json_data = json.loads(file.read())

    G = nx.DiGraph()

    for i in range(len(json_data)):
        G.add_nodes_from(
            (elem['_id'])
            for elem in json_data[i]['vertices']
        )

        G.add_edges_from(
            (elem['_from'], elem['_to'])
            for elem in json_data[i]['edges']
        )

    nx.draw(
        G,
        with_labels=True
    )

    nx.write_graphml_lxml(G, f"{filename}.gml")

    plt.show()
