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
#extended_queries.search_phrase_extended(new_db, 'pH', "result")

vf.networkx_graph('result')


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
