import json
from query_functions import simple_queries, extended_queries, extendedV2_queries, simple_subgraph_queries, extended_subgraph_queries, extendedV2_subgraph_queries


def custom_query(database, query, filename="result", directory=None):
    cursor = database.aql.execute(query)

    inter = [doc for doc in cursor]

    if directory is not None:
        with open(f"{directory}/{filename}.json", "w") as outfile:
            json.dump(inter, outfile)
    else:
        with open(f"./management/json_data/{filename}.json", "w") as outfile:
            json.dump(inter, outfile)


def filter_questions(database, structure, q1=None, q2=None, q3=None, filename="result", directory=None):
    if structure.lower() == "simple":
        simple_queries.filter_questions_simple(database, q1, q2, q3, filename, directory)
    elif structure.lower() == "extended":
        extended_queries.filter_questions_extended(database, q1, q2, q3, filename, directory)
    elif structure.lower() == "extendedv2":
        extendedV2_queries.filter_questions_extendedV2(database, q1, q2, q3, filename, directory)
    else:
        print("Available database structures: simple, extended, extendedV2.")


def contains_fragment(database, structure, fragment, filename="result", directory=None):

    if structure.lower() == "simple":
        simple_queries.contains_fragment_simple(database, fragment, filename, directory)
    elif structure.lower() == "extended":
        extended_queries.contains_fragment_extended(database, fragment, filename, directory)
    elif structure.lower() == "extendedv2":
        extendedV2_queries.contains_fragment_extendedV2(database, fragment, filename, directory)
    else:
        print("Available database structures: simple, extended, extendedV2.")


def search_phrase(database, structure, keyword, filename="result", directory=None):

    if structure.lower() == "simple":
        simple_queries.search_phrase_simple(database, keyword, filename, directory)
    elif structure.lower() == "extended":
        extended_queries.search_phrase_extended(database, keyword, filename, directory)
    elif structure.lower() == "extendedv2":
        extendedV2_queries.search_phrase_extendedV2(database, keyword, filename, directory)
    else:
        print("Available database structures: simple, extended, extendedV2.")