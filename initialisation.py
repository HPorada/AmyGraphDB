import json
import os
import sys

from arango import ArangoClient
from pathlib import Path
from initialisation_functions import simple_json, extended_json, extendedV2_json, additional_functions

sys.path.append("../")
sys.path.append("../initialisation_functions")


def database_start(database, username, password, structure):
    """This method automatically creates JSON files from Excel files with data, connects to the chosen database
    (if database with chosen name does not exist, it is created), imports data and creates a graph and a view,
    based on chosen database structure.

    :param database: (str) Name of the database to be connected or created.
    :param username: (str) Username of ArangoDB user.
    :param password: (str) Password of ArangoDB user.
    :param structure: (str) Chosen database structure ("simple", "extended" or "extendedv2").
    :return: (StandardDatabase) Database on which all actions were performed.
    """
    create_json_files(structure, "../initialisation_functions/data/questionnaire_example.xlsx",
                      "../initialisation_functions/data/experiments_example.xlsx",
                      f"../initialisation_functions/{structure}")
    db_new = connect_to_database(database, username, password)

    if structure.lower() == "simple":
        directory = "../initialisation_functions/simple"
    elif structure.lower() == "extended":
        directory = "../initialisation_functions/extended"
    elif structure.lower() == "extendedv2" or structure.lower() == "extended v2":
        directory = "../initialisation_functions/extendedV2"
    else:
        directory = None
        print("Available database structures: simple, extended, extendedV2.")

    if directory is not None:
        import_collections(db_new, directory)
        create_graph(db_new, structure)
        create_view(db_new, structure)

    return db_new


def create_json_files(structure, input_questionnaire, input_experiments, output_dir):
    """This method automatically creates JSON files from two input Excel files: first with data from questionnaire,
    second with data from electronic laboratory log, based on chosen database structure and saves them in chosen directory.

    :param structure: (str) Chosen database structure ("simple", "extended" or "extendedv2").
    :param input_questionnaire: (str) Path to the Excel file with questionnaire data.
    :param input_experiments: (str) Path to the Excel file with electronic laboratory log data.
    :param output_dir: (str) Path to the directory where JSON files are to be saved.
    """
    if structure.lower() == "simple":
        simple_json.questionnaire_simple(input_questionnaire, output_dir)
        simple_json.experiments_simple(input_experiments, output_dir)

    elif structure.lower() == "extended":
        extended_json.questionnaire_extended(input_questionnaire, output_dir)
        extended_json.experiments_extended(input_experiments, output_dir)

    elif structure.lower() == "extendedv2":
        extendedV2_json.questionnaire_extendedV2(input_questionnaire, output_dir)
        extendedV2_json.experiments_extendedV2(input_experiments, output_dir)

    else:
        raise ValueError(
            "Could not recognise database structure. Available database structures: simple, extended, extendedV2.")


def connect_to_database(database, username, password):
    """This method connects to the chosen database (if database with chosen name does not exist, it is created).

    :param database: (str) Name of the database to be connected or created.
    :param username: (str) Username of ArangoDB user.
    :param password: (str) Password of ArangoDB user.
    :return: (StandardDatabase) Database to which function connected.
    """
    client = ArangoClient(hosts='http://localhost:8529')

    db_sys = client.db('_system', username=username, password=password)

    if not db_sys.has_database(database):
        db_sys.create_database(database)

    db_new = client.db(database, username=username, password=password)

    return db_new


def import_collections(database, directory, delete_previous=True):
    """This method automatically imports data from JSON files from chosen directory to the chosen database.

    :param database: (StandardDatabase) Database to which JSON files are to be imported.
    :param directory: (str) Path to the directory with JSON files.
    :param delete_previous: (boolean) Default: True - all collections existing in the database before method's execution are deleted.
    """
    files = os.listdir(directory)

    if delete_previous:
        cols = database.collections()

        if len(cols) != 0:
            for col in cols:
                if not col['system']:
                    database.delete_collection(col['name'])

    for file in files:

        with open(directory + "/" + file) as input:
            json_data = json.loads(input.read())

        if '_from' in json_data[0]:

            a = database.create_collection(Path(file).stem, edge=True)

        else:
            a = database.create_collection(Path(file).stem)

        with open(directory + '/' + file, 'r') as json_file:
            data = json.load(json_file)
            a.import_bulk(data)


def create_graph(database, structure):
    """This method creates a graph in chosen database based on chosen database structure.

    :param database: (StandardDatabase) Database in which graph is to be created.
    :param structure: (str) Chosen database structure ("simple", "extended" or "extendedv2").
    :return: (Graph) Created graph.
    """
    if structure.lower() == "simple":
        if database.has_graph("Simple"):
            graph = database.graph("Simple")
        else:
            graph = database.create_graph("Simple")

            if graph.has_edge_definition('amyseq'):
                amyseq = graph.edge_collection('amyseq')
            else:
                amyseq = graph.create_edge_definition(
                    edge_collection='amyseq',
                    from_vertex_collections=['amyloids'],
                    to_vertex_collections=['sequences']
                )

            if graph.has_edge_definition('interactions'):
                interactions = graph.edge_collection('interactions')
            else:
                interactions = graph.create_edge_definition(
                    edge_collection='interactions',
                    from_vertex_collections=['sequences'],
                    to_vertex_collections=['sequences']
                )

            if graph.has_edge_definition('orgamy'):
                orgamy = graph.edge_collection('orgamy')
            else:
                orgamy = graph.create_edge_definition(
                    edge_collection='orgamy',
                    from_vertex_collections=['organisms'],
                    to_vertex_collections=['amyloids']
                )

    elif structure.lower() == "extended":
        if database.has_graph("Extended"):
            graph = database.graph("Extended")
        else:
            graph = database.create_graph("Extended")

            if graph.has_edge_definition('amyseqE'):
                amyseqE = graph.edge_collection('amyseqE')
            else:
                amyseqE = graph.create_edge_definition(
                    edge_collection='amyseqE',
                    from_vertex_collections=['amyloidsE'],
                    to_vertex_collections=['sequencesE']
                )

            if graph.has_edge_definition('seqintE'):
                seqintE = graph.edge_collection('seqintEs')
            else:
                seqintE = graph.create_edge_definition(
                    edge_collection='seqintE',
                    from_vertex_collections=['sequencesE'],
                    to_vertex_collections=['interactionsE']
                )

            if graph.has_edge_definition('orgamyE'):
                orgamyE = graph.edge_collection('orgamyE')
            else:
                orgamyE = graph.create_edge_definition(
                    edge_collection='orgamyE',
                    from_vertex_collections=['organismsE'],
                    to_vertex_collections=['amyloidsE']
                )

    elif structure.lower() == "extendedv2":
        if database.has_graph("ExtendedV2"):
            graph = database.graph("ExtendedV2")
        else:
            graph = database.create_graph("ExtendedV2")

            if graph.has_edge_definition('amyseqE'):
                amyseqE = graph.edge_collection('amyseqE')
            else:
                amyseqE = graph.create_edge_definition(
                    edge_collection='amyseqE',
                    from_vertex_collections=['amyloidsE'],
                    to_vertex_collections=['sequencesE']
                )

            if graph.has_edge_definition('intque1'):
                intque1 = graph.edge_collection('intque1')
            else:
                intque1 = graph.create_edge_definition(
                    edge_collection='intque1',
                    from_vertex_collections=['interactionsE'],
                    to_vertex_collections=['question1']
                )

            if graph.has_edge_definition('intque2'):
                intque2 = graph.edge_collection('intque2')
            else:
                intque2 = graph.create_edge_definition(
                    edge_collection='intque2',
                    from_vertex_collections=['interactionsE'],
                    to_vertex_collections=['question2']
                )

            if graph.has_edge_definition('intque3'):
                intque3 = graph.edge_collection('intque3')
            else:
                intque3 = graph.create_edge_definition(
                    edge_collection='intque3',
                    from_vertex_collections=['interactionsE'],
                    to_vertex_collections=['question3']
                )

            if graph.has_edge_definition('seqintE'):
                seqintE = graph.edge_collection('seqintEs')
            else:
                seqintE = graph.create_edge_definition(
                    edge_collection='seqintE',
                    from_vertex_collections=['sequencesE'],
                    to_vertex_collections=['interactionsE']
                )

            if graph.has_edge_definition('orgamyE'):
                orgamyE = graph.edge_collection('orgamyE')
            else:
                orgamyE = graph.create_edge_definition(
                    edge_collection='orgamyE',
                    from_vertex_collections=['organismsE'],
                    to_vertex_collections=['amyloidsE']
                )

            if graph.has_edge_definition('phorgE'):
                phorgE = graph.edge_collection('phorgE')
            else:
                phorgE = graph.create_edge_definition(
                    edge_collection='phorgE',
                    from_vertex_collections=['phsE'],
                    to_vertex_collections=['organismsE']
                )

            if graph.has_edge_definition('temorgE'):
                temorgE = graph.edge_collection('temorgE')
            else:
                temorgE = graph.create_edge_definition(
                    edge_collection='temorgE',
                    from_vertex_collections=['temperaturesE'],
                    to_vertex_collections=['organismsE']
                )
    else:
        graph = None
        raise ValueError(
            "Could not recognise database structure. Available database structures: simple, extended, extendedV2.")

    return graph


def create_view(database, structure):
    """This method creates a view in chosen database based on chosen database structure.

    :param database: (StandardDatabase) Database in which view is to be created.
    :param structure: (str) Chosen database structure ("simple", "extended" or "extendedv2").
    """
    if structure.lower() == "simple":
        database.create_view(
            name='simpleView',
            view_type='arangosearch',
            properties={
                "links": {
                    "sequences": {
                        "analyzers": [
                            "identity",
                            "text_en"
                        ],
                        "fields": {},
                        "includeAllFields": True,
                        "storeValues": "none",
                        "trackListPositions": False
                    },
                    "amyseq": {
                        "analyzers": [
                            "identity",
                            "text_en"
                        ],
                        "fields": {},
                        "includeAllFields": True,
                        "storeValues": "none",
                        "trackListPositions": False
                    },
                    "interactions": {
                        "analyzers": [
                            "identity",
                            "text_en"
                        ],
                        "fields": {},
                        "includeAllFields": True,
                        "storeValues": "none",
                        "trackListPositions": False
                    },
                    "amyloids": {
                        "analyzers": [
                            "identity",
                            "text_en"
                        ],
                        "fields": {},
                        "includeAllFields": True,
                        "storeValues": "none",
                        "trackListPositions": False
                    },
                    "organisms": {
                        "analyzers": [
                            "identity",
                            "text_en"
                        ],
                        "fields": {},
                        "includeAllFields": True,
                        "storeValues": "none",
                        "trackListPositions": False
                    },
                    "orgamy": {
                        "analyzers": [
                            "identity",
                            "text_en"
                        ],
                        "fields": {},
                        "includeAllFields": True,
                        "storeValues": "none",
                        "trackListPositions": False
                    }
                }
            }
        )

    elif structure.lower() == "extended":
        database.create_view(
            name='extendedView',
            view_type='arangosearch',
            properties={
                "links": {
                    "sequencesE": {
                        "analyzers": [
                            "identity",
                            "text_en"
                        ],
                        "fields": {},
                        "includeAllFields": True,
                        "storeValues": "none",
                        "trackListPositions": False
                    },
                    "amyseqE": {
                        "analyzers": [
                            "identity",
                            "text_en"
                        ],
                        "fields": {},
                        "includeAllFields": True,
                        "storeValues": "none",
                        "trackListPositions": False
                    },
                    "interactionsE": {
                        "analyzers": [
                            "identity",
                            "text_en"
                        ],
                        "fields": {},
                        "includeAllFields": True,
                        "storeValues": "none",
                        "trackListPositions": False
                    },
                    "amyloidsE": {
                        "analyzers": [
                            "identity",
                            "text_en"
                        ],
                        "fields": {},
                        "includeAllFields": True,
                        "storeValues": "none",
                        "trackListPositions": False
                    },
                    "organismsE": {
                        "analyzers": [
                            "identity",
                            "text_en"
                        ],
                        "fields": {},
                        "includeAllFields": True,
                        "storeValues": "none",
                        "trackListPositions": False
                    },
                    "orgamyE": {
                        "analyzers": [
                            "identity",
                            "text_en"
                        ],
                        "fields": {},
                        "includeAllFields": True,
                        "storeValues": "none",
                        "trackListPositions": False
                    },
                    "seqintE": {
                        "analyzers": [
                            "identity",
                            "text_en"
                        ],
                        "fields": {},
                        "includeAllFields": True,
                        "storeValues": "none",
                        "trackListPositions": False

                    }
                }
            }
        )

    elif structure.lower() == "extendedv2":
        database.create_view(
            name='extendedV2View',
            view_type='arangosearch',
            properties={
                "links": {
                    "sequencesE": {
                        "analyzers": [
                            "identity",
                            "text_en"
                        ],
                        "fields": {},
                        "includeAllFields": True,
                        "storeValues": "none",
                        "trackListPositions": False
                    },
                    "amyseqE": {
                        "analyzers": [
                            "identity",
                            "text_en"
                        ],
                        "fields": {},
                        "includeAllFields": True,
                        "storeValues": "none",
                        "trackListPositions": False
                    },
                    "interactionsE": {
                        "analyzers": [
                            "identity",
                            "text_en"
                        ],
                        "fields": {},
                        "includeAllFields": True,
                        "storeValues": "none",
                        "trackListPositions": False
                    },
                    "amyloidsE": {
                        "analyzers": [
                            "identity",
                            "text_en"
                        ],
                        "fields": {},
                        "includeAllFields": True,
                        "storeValues": "none",
                        "trackListPositions": False
                    },
                    "organismsE": {
                        "analyzers": [
                            "identity",
                            "text_en"
                        ],
                        "fields": {},
                        "includeAllFields": True,
                        "storeValues": "none",
                        "trackListPositions": False
                    },
                    "orgamyE": {
                        "analyzers": [
                            "identity",
                            "text_en"
                        ],
                        "fields": {},
                        "includeAllFields": True,
                        "storeValues": "none",
                        "trackListPositions": False
                    },
                    "seqintE": {
                        "analyzers": [
                            "identity",
                            "text_en"
                        ],
                        "fields": {},
                        "includeAllFields": True,
                        "storeValues": "none",
                        "trackListPositions": False
                    },
                    "intque1": {
                        "analyzers": [
                            "identity",
                            "text_en"
                        ],
                        "fields": {},
                        "includeAllFields": True,
                        "storeValues": "none",
                        "trackListPositions": False
                    },
                    "intque2": {
                        "analyzers": [
                            "identity",
                            "text_en"
                        ],
                        "fields": {},
                        "includeAllFields": True,
                        "storeValues": "none",
                        "trackListPositions": False
                    },
                    "intque3": {
                        "analyzers": [
                            "identity",
                            "text_en"
                        ],
                        "fields": {},
                        "includeAllFields": True,
                        "storeValues": "none",
                        "trackListPositions": False

                    },
                    "question1": {
                        "analyzers": [
                            "identity",
                            "text_en"
                        ],
                        "fields": {},
                        "includeAllFields": True,
                        "storeValues": "none",
                        "trackListPositions": False
                    },
                    "question2": {
                        "analyzers": [
                            "identity",
                            "text_en"
                        ],
                        "fields": {},
                        "includeAllFields": True,
                        "storeValues": "none",
                        "trackListPositions": False
                    },
                    "question3": {
                        "analyzers": [
                            "identity",
                            "text_en"
                        ],
                        "fields": {},
                        "includeAllFields": True,
                        "storeValues": "none",
                        "trackListPositions": False
                    },
                    "phsE": {
                        "analyzers": [
                            "identity",
                            "text_en"
                        ],
                        "fields": {},
                        "includeAllFields": True,
                        "storeValues": "none",
                        "trackListPositions": False
                    },
                    "phorgE": {
                        "analyzers": [
                            "identity",
                            "text_en"
                        ],
                        "fields": {},
                        "includeAllFields": True,
                        "storeValues": "none",
                        "trackListPositions": False
                    },
                    "temperaturesE": {
                        "analyzers": [
                            "identity",
                            "text_en"
                        ],
                        "fields": {},
                        "includeAllFields": True,
                        "storeValues": "none",
                        "trackListPositions": False
                    },
                    "temorgE": {
                        "analyzers": [
                            "identity",
                            "text_en"
                        ],
                        "fields": {},
                        "includeAllFields": True,
                        "storeValues": "none",
                        "trackListPositions": False
                    }
                }
            }
        )
    else:
        raise ValueError(
            "Could not recognise database structure. Available database structures: simple, extended, extendedV2.")


def delete_database(database, username, password):
    """This method deletes the chosen database if it exists.

    :param database: (str) Name of the database to be deleted.
    :param username: (str) Username of ArangoDB user.
    :param password: (str) Password of ArangoDB user.
    """

    client = ArangoClient()
    sys_db = client.db("_system", username=username, password=password)

    if sys_db.has_database(database):
        sys_db.delete_database(database)
