import sys
from queries_functions import simple_subgraph_queries, extended_queries, extendedV2_subgraph_queries, \
    extended_subgraph_queries, extendedV2_queries, simple_queries

sys.path.append("../")
sys.path.append("../queries_functions")

from config.definitions import ROOT_DIR
from queries_functions import save_function as save


def custom_query(database, query, filename="result", directory=None):
    """This method allows to execute a custom query in chosen database and save it with chosen name in chosen directory.

    :param database: (StandardDatabase) Database in which query is to be executed.
    :param query: (str) AQL query that is to be executed.
    :param filename: (str) Name of the file where query result is to be saved. Optional.
    :param directory: (str) Path to the directory where file with query result is to be saved. Optional.
    """
    cursor = database.aql.execute(query)

    inter = [doc for doc in cursor]

    save.save_query_result(ROOT_DIR, directory, filename, inter)


def full_graph(structure, database, filename="result", directory=None):
    """This method executes a query showing whole graph of the database of chosen structure.

    :param structure: (str) Structure of the chosen database ("simple", "extended" or "extendedv2").
    :param database: (StandardDatabase) Database in which query is to be executed.
    :param filename: (str) Name of the file where query result is to be saved. Optional.
    :param directory: (str) Path to the directory where file with query result is to be saved. Optional.
    """

    if structure.lower() == "simple":
        simple_subgraph_queries.full_graph_simple(database, filename, directory)
    elif structure.lower() == "extended":
        extended_subgraph_queries.full_graph_extended(database, filename, directory)
    elif structure.lower() == "extendedv2":
        extendedV2_subgraph_queries.full_graph_extendedV2(database, filename, directory)
    else:
        raise ValueError(
            "Could not recognise database structure. Available database structures: simple, extended, extendedV2.")


def filter_questions(structure, database, q1=None, q2=None, q3=None, filename="result", directory=None):
    """This method executes a simple query filtering the database of chosen structure based on answers to 3 questions:
    \n
    1. Is the interactor affecting interactee's aggregating speed?
    (Faster aggregation/Slower aggregation/No aggregation/No effect/No information)
    \n
    2. Do fibrils of the interactee elongate by attaching to monomers/oligomers/fibrils of the interactor?
    (Yes, direct evidence/Yes, implied by kinetics/No/Formation of fibrils by the interactee is inhibited/No information)
    \n
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
        raise ValueError(
            "Could not recognise database structure. Available database structures: simple, extended, extendedV2.")


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
        raise ValueError(
            "Could not recognise database structure. Available database structures: simple, extended, extendedV2.")


def search_phrase(structure, database, keyword, filename="result", directory=None):
    """This method executes a query searching the database of chosen structure for mentions of chosen keyword.

    :param structure: (str) Structure of the chosen database ("simple", "extended" or "extendedv2").
    :param database: (StandardDatabase) Database in which query is to be executed.
    :param keyword: (str) Keyword which is to be searched for.
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
        raise ValueError(
            "Could not recognise database structure. Available database structures: simple, extended, extendedV2.")


def subgraph_from_interactions(structure, database, q1=None, q2=None, q3=None, filename="result", directory=None):
    """This method executes a subgraph query filtering the database of chosen structure based on answers to 3 questions:
    \n
    1. Is the interactor affecting interactee's aggregating speed?
    (Faster aggregation/Slower aggregation/No aggregation/No effect/No information)
    \n
    2. Do fibrils of the interactee elongate by attaching to monomers/oligomers/fibrils of the interactor?
    (Yes, direct evidence/Yes, implied by kinetics/No/Formation of fibrils by the interactee is inhibited/No information)
    \n
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
        simple_subgraph_queries.subgraph_from_interactions_simple(database, q1, q2, q3, filename, directory)
    elif structure.lower() == "extended":
        extended_subgraph_queries.subgraph_from_interactions_extended(database, q1, q2, q3, filename, directory)
    elif structure.lower() == "extendedv2":
        extendedV2_subgraph_queries.subgraph_from_interactions_extendedV2(database, q1, q2, q3, filename, directory)
    else:
        raise ValueError(
            "Could not recognise database structure. Available database structures: simple, extended, extendedV2.")


def subgraph_from_sequence(structure, database, sequence=None, name=None, filename="result", directory=None):
    """This method executes a subgraph query filtering the database of chosen structure based on sequence or name of a sequence.

    :param structure: (str) Structure of the chosen database ("simple", "extended" or "extendedv2").
    :param database: (StandardDatabase) Database in which query is to be executed.
    :param sequence: (str) Sequence which is to be searched for. Optional.
    :param name: (str) Name of a sequence which is to be searched for. Optional.
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
        raise ValueError(
            "Could not recognise database structure. Available database structures: simple, extended, extendedV2.")


def subgraph_from_amyloid(structure, database, amyloid, filename="result", directory=None):
    """This method executes a subgraph query filtering the database of chosen structure based on name of an amyloid.

    :param structure: (str) Structure of the chosen database ("simple", "extended" or "extendedv2").
    :param database: (StandardDatabase) Database in which query is to be executed.
    :param amyloid: (str) Name of an amyloid which s to be searched for.
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
        raise ValueError(
            "Could not recognise database structure. Available database structures: simple, extended, extendedV2.")


def subgraph_from_organism(structure, database, organism, filename="result", directory=None):
    """This method executes a subgraph query filtering the database of chosen structure based on name of an organism.

    :param structure: (str) Structure of the chosen database ("simple", "extended" or "extendedv2").
    :param database: (StandardDatabase) Database in which query is to be executed.
    :param organism: (str) Name of an organism which is to be searched for.
    :param filename: (str) Name of the file where query result is to be saved. Optional.
    :param directory: (str) Path to the directory where file with query result is to be saved. Optional.
    """
    if structure.lower() == "simple":
        simple_subgraph_queries.subgraph_from_organism_simple(database, organism, filename, directory)
    elif structure.lower() == "extended":
        extended_subgraph_queries.subgraph_from_organism_extended(database, organism, filename, directory)
    elif structure.lower() == "extendedv2":
        extendedV2_subgraph_queries.subgraph_from_organism_extendedV2(database, organism, filename, directory)
    else:
        raise ValueError(
            "Could not recognise database structure. Available database structures: simple, extended, extendedV2.")
