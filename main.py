from initialisation import database
from management import visualisation_functions as vf, extended_queries

new_db = database.connect_to_database('new_extended', 'root', 'Amyloids')
#simple_queries.filter_questions_simple(new_db, q1="Slower aggregation", q3="Yes", filename="result")
extended_queries.filter_questions_extended(new_db, q1="Slower aggregation", q3="Yes", filename="result")

# #simple_JSON.questionnaire_simple()
# #simple_JSON.experiments_simple()
#
#
# #sheet = add.open_questionnaire("./initialisation/data/questionnaire.xlsx")
#
# new_db = database.connect_to_database('new_extendedV2', 'root', 'Amyloids')
# #database.create_json_files("simple")
# #database.import_collections(new_db, './initialisation/simple')
# #graph = database.create_graph(new_db, "simple")
# # #database.create_view(new_db, "extendedV2")
# #
# # #simple_queries.search_phrase_simple(new_db, 'pH', "result")
# # #extended_queries.search_phrase_extended(new_db, 'pH', "result")
# #
# query = """for i in interactionsE
#     filter i.question_1 == "Slower aggregation"
#     filter i.question_3 == "Yes"
#     return i"""
#
# simple_queries.custom_query(new_db, query, filename='result_test')

vf.graphviz_graph('result')
vf.networkx_graph('result')

#db = database.database_start("new_test", "root", "Amyloids", "simple")

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
