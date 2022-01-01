import json
from management import simple_subgraph_queries, extended_queries, extendedV2_subgraph_queries, \
    extended_subgraph_queries, extendedV2_queries, simple_queries


def custom_query(database, query, filename="result", directory=None):
    """This method allows to execute a custom query in chosen database and save it with chosen name in chosen directory.

    :param database: (StandardDatabase) Database in which query is to be executed.
    :param query: (str) AQL query that is to be executed.
    :param filename: (str) Name of the file where query result is to be saved. Optional.
    :param directory: (str) Path to the directory where file with query result is to be saved. Optional.
    """
    cursor = database.aql.execute(query)

    inter = [doc for doc in cursor]

    if directory is not None:
        with open(f"{directory}/{filename}.json", "w") as outfile:
            json.dump(inter, outfile)
    else:
        with open(f"./management/json_data/{filename}.json", "w") as outfile:
            json.dump(inter, outfile)


def filter_questions(structure, database, q1=None, q2=None, q3=None, filename="result", directory=None):
    """This method executes a query filtering the database of chosen structure based on answers to 3 questions:
    1. Is the interactor affecting interactee's aggregating speed?
    (Faster aggregation/Slower aggregation/No aggregation/No effect/No information)
    2. Do fibrils of the interactee elongate by attaching to monomers/oligomers/fibrils of the interactor?
    (Yes, direct evidence/Yes, implied by kinetics/No/Formation of fibrils by the interactee is inhibited/No information)
    3. Is interaction resulting in heterogeneous fibrils consisting of interactor and interactee molecules?
    (Yes/No/No information)

    :param structure: (str) Structure of the chosen database ("simple", "extended" or "extendedv2").
    :param database: (StandardDatabase) Database in which query is to be executed.
    :param q1: (str) Answer to the first question defining the interaction. Optional.
    :param q2: (str) Answer to the second question defining the interaction. Optional.
    :param q3: (str) Answer to the third question defining the interaction. Optional.
    :param filename: (str) Name of the file where query result is to be saved. Optional.
    :param directory: (str) Path to the directory where file with query result is to be saved. Optional.
    """
    if structure.lower() == "simple":
        simple_queries.filter_questions_simple(database, q1, q2, q3, filename, directory)
    elif structure.lower() == "extended":
        extended_queries.filter_questions_extended(database, q1, q2, q3, filename, directory)
    elif structure.lower() == "extendedv2":
        extendedV2_queries.filter_questions_extendedV2(database, q1, q2, q3, filename, directory)
    else:
        print("Available database structures: simple, extended, extendedV2.")


def contains_fragment(structure, database, fragment, filename="result", directory=None):
    """This method executes a query filtering the database of chosen structure in search of sequences containing chosen fragment.

    :param structure: (str) Structure of the chosen database ("simple", "extended" or "extendedv2").
    :param database: (StandardDatabase) Database in which query is to be executed.
    :param fragment: (str) Sequence fragment which is to be looked for.
    :param filename: (str) Name of the file where query result is to be saved. Optional.
    :param directory: (str) Path to the directory where file with query result is to be saved. Optional.
    """
    if structure.lower() == "simple":
        simple_queries.contains_fragment_simple(database, fragment, filename, directory)
    elif structure.lower() == "extended":
        extended_queries.contains_fragment_extended(database, fragment, filename, directory)
    elif structure.lower() == "extendedv2":
        extendedV2_queries.contains_fragment_extendedV2(database, fragment, filename, directory)
    else:
        print("Available database structures: simple, extended, extendedV2.")


def search_phrase(structure, database, keyword, filename="result", directory=None):
    """

    :param structure: (str) Structure of the chosen database ("simple", "extended" or "extendedv2").
    :param database: (StandardDatabase) Database in which query is to be executed.
    :param keyword:
    :param filename: (str) Name of the file where query result is to be saved. Optional.
    :param directory: (str) Path to the directory where file with query result is to be saved. Optional.
    """
    if structure.lower() == "simple":
        simple_queries.search_phrase_simple(database, keyword, filename, directory)
    elif structure.lower() == "extended":
        extended_queries.search_phrase_extended(database, keyword, filename, directory)
    elif structure.lower() == "extendedv2":
        extendedV2_queries.search_phrase_extendedV2(database, keyword, filename, directory)
    else:
        print("Available database structures: simple, extended, extendedV2.")


def subgraph_from_interactions(structure, database, q1=None, q2=None, q3=None, filename="result", directory=None):
    """

    :param structure: (str) Structure of the chosen database ("simple", "extended" or "extendedv2").
    :param database: (StandardDatabase) Database in which query is to be executed.
    :param q1:
    :param q2:
    :param q3:
    :param filename: (str) Name of the file where query result is to be saved. Optional.
    :param directory: (str) Path to the directory where file with query result is to be saved. Optional.
    """
    if structure.lower() == "simple":
        simple_subgraph_queries.subgraph_from_interactions_simple(database, q1, q2, q3, filename, directory)
    elif structure.lower() == "extended":
        extended_subgraph_queries.subgraph_from_interactions_extended(database, q1, q2, q3, filename, directory)
    elif structure.lower() == "extendedv2":
        extendedV2_subgraph_queries.subgraph_from_interactions_extendedV2(database, q1, q2, q3, filename, directory)
    else:
        print("Available database structures: simple, extended, extendedV2.")


def subgraph_from_sequence(structure, database, sequence=None, name=None, filename="result", directory=None):
    """

    :param structure: (str) Structure of the chosen database ("simple", "extended" or "extendedv2").
    :param database: (StandardDatabase) Database in which query is to be executed.
    :param sequence:
    :param name:
    :param filename: (str) Name of the file where query result is to be saved. Optional.
    :param directory: (str) Path to the directory where file with query result is to be saved. Optional.
    """
    if structure.lower() == "simple":
        simple_subgraph_queries.subgraph_from_sequence_simple(database, sequence, name, filename, directory)
    elif structure.lower() == "extended":
        extended_subgraph_queries.subgraph_from_sequence_extended(database, sequence, name, filename, directory)
    elif structure.lower() == "extendedv2":
        extendedV2_subgraph_queries.subgraph_from_sequence_extendedV2(database, sequence, name, filename, directory)
    else:
        print("Available database structures: simple, extended, extendedV2.")


def subgraph_from_amyloid(structure, database, amyloid, filename="result", directory=None):
    """

    :param structure: (str) Structure of the chosen database ("simple", "extended" or "extendedv2").
    :param database: (StandardDatabase) Database in which query is to be executed.
    :param amyloid:
    :param filename: (str) Name of the file where query result is to be saved. Optional.
    :param directory: (str) Path to the directory where file with query result is to be saved. Optional.
    """
    if structure.lower() == "simple":
        simple_subgraph_queries.subgraph_from_amyloid_simple(database, amyloid, filename, directory)
    elif structure.lower() == "extended":
        extended_subgraph_queries.subgraph_from_amyloid_extended(database, amyloid, filename, directory)
    elif structure.lower() == "extendedv2":
        extendedV2_subgraph_queries.subgraph_from_amyloid_extendedV2(database, amyloid, filename, directory)
    else:
        print("Available database structures: simple, extended, extendedV2.")
        
        
def subgraph_from_organism(structure, database, organism, filename="result", directory=None):
    """

    :param structure: (str) Structure of the chosen database ("simple", "extended" or "extendedv2").
    :param database: (StandardDatabase) Database in which query is to be executed.
    :param organism:
    :param filename: (str) Name of the file where query result is to be saved. Optional.
    :param directory: (str) Path to the directory where file with query result is to be saved. Optional.
    """
    if structure.lower() == "simple":
        simple_subgraph_queries.subgraph_from_organism_simple(database, organism, filename, directory)
    elif structure.lower() == "extended":
        extended_subgraph_queries.subgraph_from_amyloid_extended(database, organism, filename, directory)
    elif structure.lower() == "extendedv2":
        extendedV2_subgraph_queries.subgraph_from_amyloid_extendedV2(database, organism, filename, directory)
    else:
        print("Available database structures: simple, extended, extendedV2.")
