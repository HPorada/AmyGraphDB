import json
import socket

import simple_queries as sim
import extended_queries as ext
import extended_v2_queries as ext2

import subgraph_queries as sq
import visualisation_functions as vf
from arango import ArangoClient
import networkx as nx
import matplotlib.pyplot as plt

client = ArangoClient(hosts='http://localhost:8529')

sys_db = client.db('_system', username='root', password='Amyloids')

# Simple & Extended
db_Sep = client.db('AmyloidsSep', username='root', password='Amyloids')

# ExtendedE
db_Nov = client.db('AmyloidsNov', username='root', password='Amyloids')

s = socket.socket()
s.settimeout(100)

#ext2.filter_extended_v2(db_Nov, "Faster aggregation", "Yes; implied by kinetics.", "No information", "result")
#sim.contains_simple(db_Sep, 'DAEFRHDSGY', "result")
#ext.contains_extended(db_Sep, 'DAEFRHDSGY', "result")
ext2.contains_extended_v2(db_Nov, 'DAEFRHDSGY', "result")

def check_questions_simple(database, q1, q2, q3):
    aql = database.aql

    cursor = database.aql.execute(
        'FOR int IN interactions FILTER int.question_1 == @q1 FILTER int.question_2 == @q2 FILTER int.question_3 == @q3 RETURN int ',
        bind_vars={'q1': q1, 'q2': q2, 'q3': q3}
    )

    # interactionsE

    inter = [doc for doc in cursor]

    for x in inter:
        print(x)


def search_for_fragment(database, fragment):
    aql = database.aql

    cursor = database.aql.execute(
        'for i in sequences filter contains(i.sequence, @fragment) return i',
        bind_vars={'fragment': fragment}
    )

    # simpleView / sequencesE / extendedView

    inter = [doc for doc in cursor]

    for x in inter:
        print(x)


def search_for_key_word(database, key_word):
    aql = database.aql

    cursor = database.aql.execute(
        'for i in simpleView search phrase(i.general_remarks, @key, \'text_en\') return i',
        bind_vars={'key': key_word}
    )

    # extendedView

    inter = [doc for doc in cursor]

    for x in inter:
        print(x)


def search_for_all_connected(database, starting_amyloid):
    aql = database.aql

    cursor = database.aql.execute(
        'for v, e, p in 1..2 outbound @start amyseq return p',
        bind_vars={'start': starting_amyloid}
    )

    inter = [i for i in cursor]

    for x in inter:
        print(x)

    with open("json_data/test.json", "w") as outfile:
        json.dump(inter, outfile)


def search_for_most_common(database, limit, type):  # type interactor lub interactee
    aql = database.aql

    cursor = database.aql.execute(
        "for int in intseqE filter int.type == @type collect sequence = int._from with count into total sort total desc limit @limit return{ \'sequence\': sequence, \'uses\': total}",
        bind_vars={'type': type, 'limit': limit}
    )

    inter = [doc for doc in cursor]

    for x in inter:
        print(x)


def search_by_questions(database):
    aql = database.aql

    cursor = database.aql.execute(
        "for vertex in union("
        "(for v in interactionsE return v._id),"
        "(for v in sequencesE return v._id),"
        "(for v in intseqE return v._id),"
        "(for v in amyloids return v._id),"
        "(for v in amyseqE return v._id),"
        "(for v in organismsE return v._id),"
        "(for v in orgamyE return v._id))"
        "for v, e, p in 1..2 any vertex graph 'Extended'"
        "filter v.question_3 == 'No information'"
        "filter v.question_2 == 'Yes; implied by kinetics.'return p"
    )

    inter = [i for i in cursor]

    for x in inter:
        print(x)

    with open("json_data/test.json", "w") as outfile:
        json.dump(inter, outfile)


# f.check_questions_simple(db_Sep, "Faster aggregation", "Yes; implied by kinetics.", "No information")

# search_for_fragment(db_Sep, 'DAEFRHDSGY')
# search_for_key_word(db_Sep, 'pH')
# search_for_all_connected(db_Sep, 'amyloids/IAPP')
# search_for_most_common(db_Sep, 10, 'interactor')

# search_by_questions(db_Sep)

# sq.subgraph_from_interactions(db_Nov, "Slower aggregation", "No information", "No information", "check2")
# simple.check_questions_simple(db_Sep, "Faster aggregation", "Yes; implied by kinetics.", "No information", "result")
# sq.subgraph_from_sequence(db_Nov, "MGIIAGIIKVIKSLIEQFTGK", "sequence2")
# sq.subgraph_from_amyloid(db_Nov, "δ-toxin", "amyloid4")
# sq.subgraph_from_organism(db_Nov, "Frankia_sp._KB5", "organism")

# vf.graphviz_graph('sequence2.json')
# vf.networkx_graph('organism.json')



# with open("./json_data/test.json") as file:
#     json_data = json.loads(file.read())
#
# for i in json_data:
#
# G = nx.Graph(json_data)
#
# nx.draw(
#     G,
#     with_labels=True
# )
#
# plt.show()
# nx.write_gml(G, "from_dict.gml")
#
# #print(item)
