from initialisation import database, simple_json, extended_json, extendedV2_json
from management.queries import simple_queries, extended_queries, extendedV2_queries
from management import visualisation_functions as vf

#simple_JSON.questionnaire_simple()
#simple_JSON.experiments_simple()

new_db = database.create_database('new_extended', 'root', 'Amyloids')
#database.import_collections(new_db, './initialisation/simple')
#graph = database.create_graph(new_db)
#database.create_view(new_db, "extendedV2")

#simple_queries.search_phrase_simple(new_db, 'pH', "result")
extended_queries.search_phrase_extended(new_db, 'pH', "result")

vf.networkx_graph('result')

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
