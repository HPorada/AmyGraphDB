import json
import os

from arango import ArangoClient
from pathlib import Path


def create_database(database, username, password):
    client = ArangoClient(hosts='http://localhost:8529')

    db_sys = client.db('_system', username=username, password=password)

    if not db_sys.has_database(database):
        db_sys.create_database(database)

    db_new = client.db(database, username=username, password=password)

    return db_new


def import_collections(database, directory):
    files = os.listdir(directory)

    # for col in database.collections():
    #     database.delete_collection(col)

    for file in files:

        if (Path(file).stem == 'amyseq' or Path(file).stem == 'orgamy' or Path(file).stem == 'interactions' or Path(
                file).stem == 'amyseqE' or Path(file).stem == 'orgamyE' or Path(file).stem == 'seqintE' or Path(
                file).stem == 'intque1' or Path(file).stem == 'intque2' or Path(file).stem == 'intque3' or Path(
                file).stem == 'phorgE' or Path(file).stem == 'temorgE'):

            a = database.create_collection(Path(file).stem, edge=True)

        else:
            a = database.create_collection(Path(file).stem)

        with open(directory + '/' + file, 'r') as json_file:
            data = json.load(json_file)
            a.import_bulk(data)


def create_simple_graph(database):
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

    return graph


def create_extended_graph(database):
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

    return graph


def create_extendedV2_graph(database):
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

    return graph
