from initialisation import database
from management import visualisation_functions as vf, simple_queries as sq, extended_queries as eq, extendedV2_queries as e2q


new_db = database.connect_to_database('new_extendedV2', 'root', 'Amyloids')
#database.create_view(new_db, 'simple')
#simple_queries.filter_questions_simple(new_db, q1="Slower aggregation", q3="Yes", filename="result")
#extended_queries.filter_questions_extended(new_db, q1="Slower aggregation", q3="Yes", filename="result")

#sq.contains_fragment_simple(new_db, "DAEFRHDSG", "result")
#eq.contains_fragment_extended(new_db, "DAEFRHDSG", "result")
#e2q.contains_fragment_extendedV2(new_db, "DAEFRHDSG", "result")

#new_db = database.database_start('new_extendedV2', 'root', 'Amyloids', 'extendedv2')

e2q.search_phrase_extendedV2(new_db, 'pH', 'result')
#
vf.graphviz_graph('result')
vf.networkx_graph('result')

