import json


def filter_questions_extended(database, q1, q2, q3, filename="result", directory=None):
    """This method executes a simple query filtering the database of EXTENDED structure based on answers to 3 questions:
    1. Is the interactor affecting interactee's aggregating speed?
    (Faster aggregation/Slower aggregation/No aggregation/No effect/No information)
    2. Do fibrils of the interactee elongate by attaching to monomers/oligomers/fibrils of the interactor?
    (Yes, direct evidence/Yes, implied by kinetics/No/Formation of fibrils by the interactee is inhibited/No information)
    3. Is interaction resulting in heterogeneous fibrils consisting of interactor and interactee molecules?
    (Yes/No/No information)

    :param database: (StandardDatabase) Database in which query is to be executed.
    :param q1: (str) Answer to the first question defining the interaction. Optional.
    :param q2: (str) Answer to the second question defining the interaction. Optional.
    :param q3: (str) Answer to the third question defining the interaction. Optional.
    :param filename: (str) Name of the file where query result is to be saved. Optional.
    :param directory: (str) Path to the directory where file with query result is to be saved. Optional.
    """
    if (
            q1 == "Faster aggregation" or q1 == "Slower aggregation" or q1 == "No aggregation" or q1 == "No effect" or q1 == "No information") and (
            q2 == "Yes, direct evidence." or q2 == "Yes; implied by kinetics." or q2 == "Formation of fibrils by the interactee is inhibited" or q2 == "No" or q2 == "No information") and (
            q3 == "Yes" or q3 == "No" or q3 == "No information"):

        cursor = database.aql.execute(
            """for item in interactionsE
                for v, e, p in 1..1 any item._id graph "Extended"
                    filter item.question_1 == @q1
                    filter item.question_2 == @q2
                    filter item.question_3 == @q3
                    return p""",
            bind_vars={'q1': q1, 'q2': q2, 'q3': q3}
        )

    elif (
            q1 == "Faster aggregation" or q1 == "Slower aggregation" or q1 == "No aggregation" or q1 == "No effect" or q1 == "No information") and (
            q2 == "Yes, direct evidence." or q2 == "Yes; implied by kinetics." or q2 == "Formation of fibrils by the interactee is inhibited" or q2 == "No" or q2 == "No information"):

        cursor = database.aql.execute(
            """for item in interactionsE
                for v, e, p in 1..1 any item._id graph "Extended"
                    filter item.question_1 == @q1
                    filter item.question_2 == @q2
                    return p""",
            bind_vars={'q1': q1, 'q2': q2}
        )

    elif (
            q2 == "Yes, direct evidence." or q2 == "Yes; implied by kinetics." or q2 == "Formation of fibrils by the interactee is inhibited" or q2 == "No" or q2 == "No information") and (
            q3 == "Yes" or q3 == "No" or q3 == "No information"):

        cursor = database.aql.execute(
            """for item in interactionsE
                for v, e, p in 1..1 any item._id graph "Extended"
                    filter item.question_2 == @q2
                    filter item.question_3 == @q3
                    return p""",
            bind_vars={'q2': q2, 'q3': q3}
        )

    elif (
            q1 == "Faster aggregation" or q1 == "Slower aggregation" or q1 == "No aggregation" or q1 == "No effect" or q1 == "No information") and (
            q3 == "Yes" or q3 == "No" or q3 == "No information"):

        cursor = database.aql.execute(
            """for item in interactionsE
                for v, e, p in 1..1 any item._id graph "Extended"
                    filter item.question_1 == @q1
                    filter item.question_3 == @q3
                    return p""",
            bind_vars={'q1': q1, 'q3': q3}
        )

    elif (
            q1 == "Faster aggregation" or q1 == "Slower aggregation" or q1 == "No aggregation" or q1 == "No effect" or q1 == "No information"):

        cursor = database.aql.execute(
            """for item in interactionsE
                for v, e, p in 1..1 any item._id graph "Extended"
                    filter item.question_1 == @q1
                    return p""",
            bind_vars={'q1': q1}
        )

    elif (
            q2 == "Yes, direct evidence." or q2 == "Yes; implied by kinetics." or q2 == "Formation of fibrils by the interactee is inhibited" or q2 == "No" or q2 == "No information"):

        cursor = database.aql.execute(
            """for item in interactionsE
                for v, e, p in 1..1 any item._id graph "Extended"
                    filter item.question_2 == @q2
                    return p""",
            bind_vars={'q2': q2}
        )

    elif (
            q3 == "Yes" or q3 == "No" or q3 == "No information"):

        cursor = database.aql.execute(
            """for item in interactionsE
                for v, e, p in 1..1 any item._id graph "Extended"
                    filter item.question_3 == @q3
                    return p""",
            bind_vars={'q3': q3}
        )

    else:
        cursor = database.aql.execute(
            """for item in interactionsE
                for v, e, p in 1..1 any item._id graph "Extended"
                    return p"""
        )

    inter = [doc for doc in cursor]

    if directory is not None:
        with open(f"{directory}/{filename}.json", "w") as outfile:
            json.dump(inter, outfile)
    else:
        with open(f"./management/json_data/{filename}.json", "w") as outfile:
            json.dump(inter, outfile)


def contains_fragment_extended(database, fragment, filename="result", directory=None):
    """This method executes a query filtering the database of EXTENDED structure in search of sequences containing chosen fragment.

    :param database: (StandardDatabase) Database in which query is to be executed.
    :param fragment: (str) Sequence fragment which is to be looked for.
    :param filename: (str) Name of the file where query result is to be saved. Optional.
    :param directory: (str) Path to the directory where file with query result is to be saved. Optional.
    """
    cursor = database.aql.execute(
        """for item in amyloidsE
            for v, e, p in 1..1 outbound item._id graph "Extended"
                filter contains(v.sequence, @fragment)
                return p""",
        bind_vars={'fragment': fragment}
    )

    inter = [doc for doc in cursor]

    if directory is not None:
        with open(f"{directory}/{filename}.json", "w") as outfile:
            json.dump(inter, outfile)
    else:
        with open(f"./management/json_data/{filename}.json", "w") as outfile:
            json.dump(inter, outfile)


def search_phrase_extended(database, keyword, filename="result", directory=None):
    """This method executes a query searching the database of EXTENDED structure for mentions of chosen keyword.

    :param database: (StandardDatabase) Database in which query is to be executed.
    :param keyword: (str) Keyword which is to be searched for.
    :param filename: (str) Name of the file where query result is to be saved. Optional.
    :param directory: (str) Path to the directory where file with query result is to be saved. Optional.
    """
    cursor = database.aql.execute(
        """
        for i in extendedView 
            search phrase(i.general_remarks, @keyword, 'text_en') 
            return i""",
        bind_vars={'keyword': keyword}
    )

    inter = [doc for doc in cursor]

    if directory is not None:
        with open(f"{directory}/{filename}.json", "w") as outfile:
            json.dump(inter, outfile)
    else:
        with open(f"./management/json_data/{filename}.json", "w") as outfile:
            json.dump(inter, outfile)

# def search_connected_extended(database, collection, start, filename="result"):
#     ()
#