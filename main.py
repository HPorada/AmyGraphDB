from inspect import getmembers, isfunction
from initialisation import additional_functions,database,extended_json,extendedV2_json,simple_json
from management.queries import simple_queries, extended_queries, extendedV2_queries
from management import visualisation_functions as vf
import management.queries.simple_subgraph_queries as ssq
import initialisation.additional_functions as add

#simple_JSON.questionnaire_simple()
#simple_JSON.experiments_simple()


#sheet = add.open_questionnaire("./initialisation/data/questionnaire.xlsx")

new_db = database.connect_to_database('new_simple', 'root', 'Amyloids')
#database.create_json_files("simple")
#database.import_collections(new_db, './initialisation/simple')
graph = database.create_graph(new_db, "simple")
# #database.create_view(new_db, "extendedV2")
#
# #simple_queries.search_phrase_simple(new_db, 'pH', "result")
# #extended_queries.search_phrase_extended(new_db, 'pH', "result")
#
# query = """for i in amyloids
#     filter i._key == "IAPP"
#     return i"""

#simple_queries.custom_query(new_db, query, filename='result_test')
#
#vf.networkx_graph('result')

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
