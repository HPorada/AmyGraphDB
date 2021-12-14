import json
import socket

from graphviz import Digraph

from arango import ArangoClient

client = ArangoClient(hosts='http://localhost:8529')

sys_db = client.db('_system', username='root', password='Amyloids')

# Simple & Extended
db_Sep = client.db('AmyloidsSep', username='root', password='Amyloids')

# ExtendedE
db_Nov = client.db('AmyloidsNov', username='root', password='Amyloids')

s = socket.socket()
s.settimeout(100)

# print(db.graph('ExtendedWithEdges'))
# graph = db.graph('ExtendedWithEdges')


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

    with open("./test.json", "w") as outfile:
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

    with open("./test.json", "w") as outfile:
        json.dump(inter, outfile)


# check_questions_simple(db_Sep, "Faster aggregation", "Yes; implied by kinetics.", "No information")
# search_for_fragment(db_Sep, 'DAEFRHDSGY')
# search_for_key_word(db_Sep, 'pH')
# search_for_all_connected(db_Sep, 'amyloids/IAPP')
# search_for_most_common(db_Sep, 10, 'interactor')

search_by_questions(db_Sep)

with open("./test.json", "r") as file:
    arango_graph = json.load(file)

graph_name = 'example_graph'

g = Digraph(graph_name, filename=graph_name, format='jpeg', engine='neato')
g.attr(scale='2', label='Searching with starting node', fontsize='18')
g.attr('node', shape='circle', fixedsize='false', width='0.5')

for item in arango_graph:
    for vertex in item['vertices']:
        g.node(vertex['_id'], label=vertex['_key'])
    for edge in item['edges']:
        g.edge(edge['_from'], edge['_to'])

# Render to file into some directory
# g.render(directory='/tmp/', filename=graph_name)
# Or just show rendered file using system default program
g.view()
