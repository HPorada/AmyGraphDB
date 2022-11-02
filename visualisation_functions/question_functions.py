def question1_shape_graphviz(answer):
    """This method determines shape of the node in graph_graphviz function based on an answer to the first question. \n
    (Is the interactor affecting interactee's aggregating speed?)

    :param answer: (str) Answer to the first question.
    :return: (str) Node shape.
    """
    switch = {
        "Faster aggregation": "triangle",
        "Slower aggregation": "invtriangle",
        "No aggregation": "square",
        "No effect": "diamond",
        "No information": "box"
    }
    return switch.get(answer, "box")


def question1_shape_networkx(answer):
    """This method determines shape of the node in graph_networkx function based on an answer to the first question. \n
    (Is the interactor affecting interactee's aggregating speed?)

    :param answer: (str) Answer to the first question.
    :return: (str) Node shape.
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
    """This method determines colour of the node based on an answer to the second question. \n
    (Do fibrils of the interactee elongate by attaching to monomers/oligomers/fibrils of the interactor?)

    :param answer: (str) Answer to the second question.
    :return: (str) Node colour.
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
    """This method determines colour of the node's border in graph_graphviz function based on an answer to the third question. \n
    (Is interaction resulting in heterogeneous fibrils consisting of interactor and interactee molecules?)

    :param answer: (str) Answer to the third question.
    :return: (str) Node's border colour.
    """
    switch = {
        "Yes": "#55ff3c",
        "No": "#ff6c28",
        "No information": "#000000"
    }
    return switch.get(answer, "#000000")


def question3_answer_networkx(answer):
    """This method determines an indication added to label in graph_networkx function based on an answer to the third question. \n
    (Is interaction resulting in heterogeneous fibrils consisting of interactor and interactee molecules?)

    :param answer: (str) Answer to the third question.
    :return: (str) Indication of the answer.
    """
    switch = {
        "Yes": "(Y)",
        "No": "(N)",
        "No information": "(NI)"
    }
    return switch.get(answer, "(NI)")
