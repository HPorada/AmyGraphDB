from initialisation import database, simple_json, extended_json, extendedV2_json
from management.queries import simple_queries, extended_queries, extendedV2_queries
from management import visualisation_functions as vf

#simple_JSON.questionnaire_simple()
#simple_JSON.experiments_simple()

new_db = database.create_database('new_simple', 'root', 'Amyloids')
#database.import_collections(new_db, './initialisation/simple')
#graph = database.create_graph(new_db)
database.create_view(new_db, "simple")

#simple_queries.filter_questions_simple(new_db, "Faster aggregation", "Yes; implied by kinetics.", "No information", "result")

vf.graphviz_graph('result', sequences=True)
vf.networkx_graph('result', True)

# extended_JSON.questionnaire_extended()
# extended_JSON.experiments_extended()

# new_db = database.create_database('new_extended', 'root', 'Amyloids')
# database.import_collections(new_db, './initialisation/extended')
# graph = database.create_extended_graph(new_db)
#
# extended_queries.filter_extended(new_db, "Faster aggregation", "Yes; implied by kinetics.", "No information", "result")
#
# vf.graphviz_graph('result', sequences=True)
# vf.networkx_graph('result', True)

# extendedV2_json.questionnaire_extendedV2()
# extendedV2_json.experiments_extendedV2()
#
# new_db = database.create_database('new_extendedV2', 'root', 'Amyloids')
# database.import_collections(new_db, './initialisation/extendedV2')
# graph = database.create_graph(new_db)
#
# extendedV2_queries.filter_extendedV2(new_db, "Faster aggregation", "Yes; implied by kinetics.", "No information", "result")
#
# vf.graphviz_graph('result', sequences=True)
# vf.networkx_graph('result', True)

# import json
# import socket
#
# from management.queries import simple_queries as sim
#
# import visualisation_functions as vf
# from arango import ArangoClient
#
# client = ArangoClient(hosts='http://localhost:8529')
#
# sys_db = client.db('_system', username='root', password='Amyloids')
#
# # Simple & Extended
# db_Sep = client.db('AmyloidsSep', username='root', password='Amyloids')
#
# # ExtendedE
# db_Nov = client.db('AmyloidsNov', username='root', password='Amyloids')
#
# s = socket.socket()
# s.settimeout(100)
#
#
# sim.filter_simple(db_Sep, "Faster aggregation4", "Yes; implied by kinetics.", "No information", "Simple", "result")
# # ext2.filter_extended_v2(db_Nov, "Faster aggregation", "Yes; implied by kinetics.", "No information", "result")
# # sim.contains_simple(db_Sep, 'DAEFRHDSGY', "result")
# # ext.contains_extended(db_Sep, 'DAEFRHDSGY', "result")
# # ext2.contains_extended_v2(db_Nov, 'DAEFRHDSGY', "result")
#
# def check_questions_simple(database, q1, q2, q3):
#     aql = database.aql
#
#     cursor = database.aql.execute(
#         'FOR int IN interactions FILTER int.question_1 == @q1 FILTER int.question_2 == @q2 FILTER int.question_3 == @q3 RETURN int ',
#         bind_vars={'q1': q1, 'q2': q2, 'q3': q3}
#     )
#
#     # interactionsE
#
#     inter = [doc for doc in cursor]
#
#     for x in inter:
#         print(x)
#
#
# def search_for_fragment(database, fragment):
#     aql = database.aql
#
#     cursor = database.aql.execute(
#         'for i in sequences filter contains(i.sequence, @fragment) return i',
#         bind_vars={'fragment': fragment}
#     )
#
#     # simpleView / sequencesE / extendedView
#
#     inter = [doc for doc in cursor]
#
#     for x in inter:
#         print(x)
#
#
# def search_for_key_word(database, key_word):
#     aql = database.aql
#
#     cursor = database.aql.execute(
#         'for i in simpleView search phrase(i.general_remarks, @key, \'text_en\') return i',
#         bind_vars={'key': key_word}
#     )
#
#     # extendedView
#
#     inter = [doc for doc in cursor]
#
#     for x in inter:
#         print(x)
#
#
# def search_for_all_connected(database, starting_amyloid):
#     aql = database.aql
#
#     cursor = database.aql.execute(
#         'for v, e, p in 1..2 outbound @start amyseq return p',
#         bind_vars={'start': starting_amyloid}
#     )
#
#     inter = [i for i in cursor]
#
#     for x in inter:
#         print(x)
#
#     with open("management/json_data/test.json", "w") as outfile:
#         json.dump(inter, outfile)
#
#
# def search_for_most_common(database, limit, type):  # type interactor lub interactee
#     aql = database.aql
#
#     cursor = database.aql.execute(
#         "for int in intseqE filter int.type == @type collect sequence = int._from with count into total sort total desc limit @limit return{ \'sequence\': sequence, \'uses\': total}",
#         bind_vars={'type': type, 'limit': limit}
#     )
#
#     inter = [doc for doc in cursor]
#
#     for x in inter:
#         print(x)
#
#     inter = [i for i in cursor]
#
#     for x in inter:
#         print(x)
#
#     with open("management/json_data/test.json", "w") as outfile:
#         json.dump(inter, outfile)
#
#
# # sq.subgraph_from_interactions(db_Nov, q1="Slower aggregation", q2="Yes, direct evidence.", q3="No information", filename="result")
# # simple.check_questions_simple(db_Sep, "Faster aggregation", "Yes; implied by kinetics.", "No information", "result")
# # sq.subgraph_from_sequence(db_Nov, "VFHGKGIQHTGSGNFSVGNDLSIS", "result")
# # sq.subgraph_from_amyloid(db_Nov, "IAPP", "result")
# # sq.subgraph_from_organism(db_Nov, "Frankia_sp._KB5", "organism")
#
# #vf.graphviz_graph('result', int_questions=True, sequences=True)
# vf.networkx_graph('result', int_questions=True)
