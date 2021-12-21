import json
import networkx as nx
import matplotlib.pyplot as plt
from graphviz import Digraph
import re
from pyvis.network import Network
import plotly.graph_objects as go


def graphviz_graph(filename):
    with open(f".\json_data\{filename}", "r") as file:
        arango_graph = json.load(file)

    graph_name = filename

    g = Digraph(graph_name, filename=f".\graphs\{graph_name}", format='jpeg', engine='dot')
    g.attr(scale='2', label='Searching with starting node', fontsize='18')
    g.attr('node', shape='rectangle', style='filled', fillcolor='', fixedsize='false', width='0.5')

    for item in arango_graph:
        for vertex in item['vertices']:

            if re.search("^sequencesE", vertex['_id']) is not None:
                # g.attr('node', shape='triangle')
                g.node(vertex['_id'], label=vertex['name'] if 'name' in vertex else "seq:" + vertex['_key'])

            elif re.search("^interactionsE", vertex['_id']) is not None:

                shape = question1_shape(vertex['question_1'])
                color = question2_color(vertex['question_2'])

                g.attr('node', shape=shape, style='filled', fillcolor=color)
                g.node(vertex['_id'], label="int:" + vertex['_key'])
                g.attr('node', shape='rectangle', fillcolor='', fixedsize='false', width='0.5')

            elif re.search("^amyloidsE", vertex['_id']) is not None:
                g.attr('node', shape='ellipse')
                g.node(vertex['_id'], label=vertex['name'])
                g.attr('node', shape='rectangle', fillcolor='', fixedsize='false', width='0.5')

            else:
                g.node(vertex['_id'], label=vertex['name'] if 'name' in vertex else vertex['_key'])
        for edge in item['edges']:
            g.edge(edge['_from'], edge['_to'])

    # Render to file into some directory
    # g.render(directory='/tmp/', filename=graph_name)

    # Or just show rendered file using system default program
    g.view()


def question1_shape(answer):
    switch = {
        "Faster aggregation": "triangle",
        "Slower aggregation": "invtriangle",
        "No aggregation": "octagon",
        "No effect": "diamond",
        "No information": "box"
    }
    return switch.get(answer, "box")


def question2_color(answer):
    switch = {
        "Yes, direct evidence.": "darkgreen",
        "Yes; implied by kinetics.": "forestgreen",
        "Formation of fibrils by the interactee is inhibited": "red1",
        "No": "yellow2",
        "No information": ""
    }
    return switch.get(answer, "")


def networkx_graph(filename):
    with open(f'.\json_data\{filename}') as file:
        json_data = json.loads(file.read())

    G = nx.DiGraph()

    # for i in range(len(json_data)):
    #     G.add_nodes_from(
    #         (elem['_key'])
    #         for elem in json_data[i]['vertices']
    #     )
    #
    #     G.add_edges_from(
    #         (elem['_from'], elem['_to'])
    #         for elem in json_data[i]['edges']
    #     )

    for i in range(len(json_data)):
        for j in json_data[i]['vertices']:
            if re.search("^questions", j['_id']) is not None:
                G.add_node(j['_id'], label=j['_key'], group=1)
            elif re.search("^interactions", j['_id']) is not None:
                G.add_node(j['_id'], label='int' + j['_key'], group=2)
            elif re.search("^sequences", j['_id']) is not None:
                G.add_node(j['_id'], sequence=j['sequence'], label=j['name'] if 'name' in j else "seq:" + j['_key'],
                           group=3)
            elif re.search("^amyloids", j['_id']) is not None:
                G.add_node(j['_id'], label=j['name'], group=4)
            elif re.search("^organisms", j['_id']) is not None:
                G.add_node(j['_id'], lifestyle=j['lifestyle'], temperature=j['temperature'], pH=j['pH'],
                           label=j['_key'], group=5)
            elif re.search("^temperatures", j['_id']) is not None:
                G.add_node(j['_id'], range=j['range'], label=j['_key'], group=6)
            elif re.search("^phs", j['_id']) is not None:
                G.add_node(j['_id'], range=j['range'], label=j['_key'], group=7)
            else:
                G.add_node(j['_id'], label=j['_key'], group=8)
        for k in json_data[i]['edges']:
            G.add_edge(k['_from'], k['_to'])

    # nx.draw(
    #     G,
    #     with_labels=True
    # )

    # Pyvis
    nt = Network('1000px', '1000px')
    # nt.enable_physics(True)
    nt.show_buttons(filter_=['physics'])
    nt.from_nx(G)
    nt.show('nx.html')

    nx.write_graphml_lxml(G, f"{filename}.gml")
    # nx.write_gml(G, f"{filename}.graphml")
    # nx.write_gexf(G, f"{filename}.gexf")

    plt.show()
