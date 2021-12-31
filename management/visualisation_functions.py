import json
import networkx as nx
import matplotlib.pyplot as plt
from graphviz import Digraph
import re
from pyvis.network import Network
import plotly.graph_objects as go


def graphviz_graph(filename, input_dir='./management/json_data', output_dir='./management/graphviz', int_questions=False, sequences=False, engine='dot', direction='LR'):
    """

    :param filename:
    :param input_dir:
    :param output_dir:
    :param int_questions:
    :param sequences:
    :param engine:
    :param direction:
    """
    with open(f"{input_dir}/{filename}.json", "r") as file:
        arango_graph = json.load(file)

    graph_name = filename

    g = Digraph(graph_name, filename=f"{output_dir}/{graph_name}.dot", format='jpeg', engine=engine,
                graph_attr={'rankdir': direction})
    # g.attr(scale='2', label='Searching with starting node', fontsize='18')
    g.attr('node', shape='rectangle', style='filled', fillcolor='#bfbfbf', fixedsize='false', width='0.5')

    for item in arango_graph:
        if 'vertices' in item:
            for vertex in item['vertices']:

                if re.search("^sequencesE", vertex['_id']) is not None:
                    if sequences:
                        g.node(vertex['_id'], label=vertex['sequence'] if 'sequence' in vertex else "seq:" + vertex['_key'])
                    else:
                        g.node(vertex['_id'], label=vertex['name'] if 'name' in vertex else "seq:" + vertex['_key'])

                elif re.search("^interactionsE", vertex['_id']) is not None:

                    if 'question_1' in vertex:
                        shape = question1_shape_graphviz(vertex['question_1'])
                    else:
                        shape = 'box'

                    if 'question_2' in vertex:
                        color = question2_color(vertex['question_2'])
                    else:
                        color = '#bfbfbf'

                    if 'question_3' in vertex:
                        frame = question3_border_graphviz(vertex['question_3'])
                    else:
                        frame = '#000000'

                    g.attr('node', shape=shape, style='filled', fillcolor=color, color=frame, penwidth='5')
                    g.node(vertex['_id'], label="int:" + vertex['_key'])
                    g.attr('node', shape='rectangle', fillcolor='#bfbfbf', fixedsize='false', width='0.5',
                           fontcolor='black', color='#000000', penwidth='1')

                elif re.search("^amyloidsE", vertex['_id']) is not None:
                    g.attr('node', shape='ellipse', fillcolor='aqua')
                    g.node(vertex['_id'], label=vertex['name'])
                    g.attr('node', shape='rectangle', fillcolor='#bfbfbf', fixedsize='false', width='0.5')

                elif re.search("^question", vertex['_id']) is not None:
                    if int_questions:
                        g.node(vertex['_id'], label=vertex['_key'])

                else:
                    g.node(vertex['_id'], label=vertex['name'] if 'name' in vertex else vertex['_key'])
            for edge in item['edges']:
                if not int_questions:
                    if not re.search("^question", edge["_to"]) is not None:
                        g.edge(edge['_from'], edge['_to'])
                else:
                    g.edge(edge['_from'], edge['_to'])

        else:
            if '_from' in item:
                g.edge(item['_from'], item['_to'])
            else:
                if re.search("^sequencesE", item['_id']) is not None:
                    if sequences:
                        g.node(item['_id'], label=item['sequence'] if 'sequence' in item else "seq:" + item['_key'])
                    else:
                        g.node(item['_id'], label=item['name'] if 'name' in item else "seq:" + item['_key'])

                elif re.search("^interactionsE", item['_id']) is not None:

                    if 'question_1' in item:
                        shape = question1_shape_graphviz(item['question_1'])
                    else:
                        shape = 'box'

                    if 'question_2' in item:
                        color = question2_color(item['question_2'])
                    else:
                        color = '#bfbfbf'

                    if 'question_3' in item:
                        frame = question3_border_graphviz(item['question_3'])
                    else:
                        frame = '#000000'

                    g.attr('node', shape=shape, style='filled', fillcolor=color, color=frame, penwidth='5')
                    g.node(item['_id'], label="int:" + item['_key'])
                    g.attr('node', shape='rectangle', fillcolor='#bfbfbf', fixedsize='false', width='0.5',
                           fontcolor='black', color='#000000', penwidth='1')
                else:
                    g.node(item['_id'], label=item['_key'])

    # Render to file into some directory
    # g.render(directory='/tmp/', filename=graph_name)

    # Or just show rendered file using system default program
    g.view()


def networkx_graph(filename, input_dir='./management/json_data', output_dir='./management/networkx', int_questions=False, sequences=True, general_remarks=True):
    """

    :param filename:
    :param input_dir:
    :param output_dir:
    :param int_questions:
    :param sequences:
    :param general_remarks:
    """
    with open(f'{input_dir}/{filename}.json') as file:
        json_data = json.loads(file.read())

    G = nx.DiGraph()

    for i in json_data:
        if 'vertices' in i:
            for j in i['vertices']:

                if re.search("^question", j['_id']) is not None:
                    if int_questions:
                        G.add_node(j['_id'], label=j['_key'], group=1),

                elif re.search("^interactions", j['_id']) is not None:

                    if 'question_1' in j:
                        shape = question1_shape_networkx(j['question_1'])
                    else:
                        shape = 'box'

                    if 'question_2' in j:
                        color = question2_color(j['question_2'])
                    else:
                        color = '#bfbfbf'

                    if 'question_3' in j:
                        answer = question3_answer_networkx(j['question_3'])
                    else:
                        answer = "(NI)"

                    if general_remarks:
                        G.add_node(j['_id'],
                                   title='<a href="javascript:alert(' + j['general_remarks'] + ')">' + j[
                                       'general_remarks'] + '</a>'
                                   if 'general_remarks' in j else 'No information',
                                   label='int:' + j['_key'] + answer, group=2,
                                   shape=shape, color=color),
                    else:
                        G.add_node(j['_id'], label='int:' + j['_key'] + answer, group=2,
                                   shape=shape, color=color),

                elif re.search("^sequences", j['_id']) is not None:
                    if sequences:
                        G.add_node(j['_id'],
                                   title='<a href="javascript:alert(' + j['sequence'] + ')">' + j['sequence'] + '</a>'
                                   if 'sequence' in j else 'No information',
                                   label=j['name'] if 'name' in j else "seq:" + j['_key'],
                                   group=3)
                    else:
                        G.add_node(j['_id'], label=j['name'] if 'name' in j else "seq:" + j['_key'],
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

            for k in i['edges']:
                if not int_questions:
                    if not re.search("^question", k["_to"]) is not None:
                        G.add_edge(k['_from'], k['_to'])
                else:
                    if 'general_remarks' in k:
                        G.add_edge(k['_from'], k['_to'],
                                   title='<a href="javascript:alert(' + k['general_remarks'] + ')">' + k[
                                       'general_remarks'] + '</a>')
                    elif 'type' in k:
                        G.add_edge(k['_from'], k['_to'], title=k['type'])
                    elif 'values' in k:
                        G.add_edge(k['_from'], k['_to'], title=k['values'])
                    else:
                        G.add_edge(k['_from'], k['_to'])

        else:
            if '_from' in i:
                G.add_edge(i['_from'], i['_to'])
            else:
                if re.search("^interactions", i['_id']) is not None:

                    if 'question_1' in i:
                        shape = question1_shape_networkx(i['question_1'])
                    else:
                        shape = 'box'

                    if 'question_2' in i:
                        color = question2_color(i['question_2'])
                    else:
                        color = '#bfbfbf'

                    if 'question_3' in i:
                        answer = question3_answer_networkx(i['question_3'])
                    else:
                        answer = "(NI)"

                    if general_remarks:
                        G.add_node(i['_id'],
                                   title='<a href="javascript:alert(' + i['general_remarks'] + ')">' + i[
                                       'general_remarks'] + '</a>'
                                   if 'general_remarks' in i else 'No information',
                                   label='int:' + i['_key'] + answer, group=2,
                                   shape=shape, color=color),
                    else:
                        G.add_node(i['_id'], label='int:' + i['_key'] + answer, group=2,
                                   shape=shape, color=color),

                elif re.search("^sequences", i['_id']) is not None:
                    if sequences:
                        G.add_node(i['_id'],
                                   title='<a href="javascript:alert(' + i['sequence'] + ')">' + i['sequence'] + '</a>'
                                   if 'sequence' in i else 'No information',
                                   label=i['name'] if 'name' in i else "seq:" + i['_key'],
                                   group=3)
                    else:
                        G.add_node(i['_id'], label=j['name'] if 'name' in i else "seq:" + i['_key'],
                                   group=3)
                else:
                    G.add_node(i['_id'], label=i['_key'])

    nx.draw(
        G,
        with_labels=True
    )

    # Pyvis
    nt = Network('1000px', '1000px')
    nt.show_buttons(filter_=['physics'])
    nt.from_nx(G)
    nt.show('nx.html')

    nx.write_graphml_lxml(G, f"{output_dir}/{filename}.gml")
    # nx.write_gml(G, f"{filename}.graphml")
    # nx.write_gexf(G, f"{filename}.gexf")

    plt.show()


def question1_shape_graphviz(answer):
    """

    :param answer:
    :return:
    """
    switch = {
        "Faster aggregation": "triangle",
        "Slower aggregation": "invtriangle",
        "No aggregation": "octagon",
        "No effect": "diamond",
        "No information": "box"
    }
    return switch.get(answer, "box")


def question1_shape_networkx(answer):
    """

    :param answer:
    :return:
    """
    switch = {
        "Faster aggregation": "triangle",
        "Slower aggregation": "triangleDown",
        "No aggregation": "square",
        "No effect": "diamond",
        "No information": "box"
    }
    return switch.get(answer, "box")


def question2_color(answer):
    """

    :param answer:
    :return:
    """
    switch = {
        "Yes, direct evidence.": "#1A870A",
        "Yes; implied by kinetics.": "#0bd11f",
        "Formation of fibrils by the interactee is inhibited": "#e30000",
        "No": "#ffe124",
        "No information": "#bfbfbf"
    }
    return switch.get(answer, "#bfbfbf")


def question3_border_graphviz(answer):
    """

    :param answer:
    :return:
    """
    switch = {
        "Yes": "#55ff3c",
        "No": "#ff6c28",
        "No information": "#000000"
    }
    return switch.get(answer, "#000000")


def question3_answer_networkx(answer):
    """

    :param answer:
    :return:
    """
    switch = {
        "Yes": "(Y)",
        "No": "(N)",
        "No information": "(NI)"
    }
    return switch.get(answer, "(NI)")
