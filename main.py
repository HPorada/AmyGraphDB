import initialisation as i
import queries as q
import visualisation as v

database = i.connect_to_database('new_simple', 'root', 'Amyloids')

q.subgraph_from_interactions('simple', database, q1='Slower aggregation', q2='Yes; implied by kinetics.', q3='No information', filename='result')
# q.subgraph_from_amyloid('extendedv2', db, 'Sup35', filename='result')

# q.full_graph('extendedv2', db, filename='result')

#q.subgraph_from_interactions('extendedV2', db, q1="Slower aggregation", q3="Yes", filename="result")

# sequence="MEFVAKLFKFFKDLLGKFLGNN"

#q.subgraph_from_sequence('extended', database, sequence="MEFVAKLFKFFKDLLGKFLGNN", filename='result')

# q.subgraph_from_amyloid("extendedV2", db, amyloid="Sup35", filename="result")

# q.subgraph_from_organism("extendedV2", db, organism="Coleophoma_crateriformis",  filename="result")

# v.graphviz_graph('result')

# query = """for i in interactionsE
# filter i.question_1 == "Slower aggregation"
# filter i.question_3 == "Yes"
# return i"""
# q.custom_query(database, query, "result")
#q.full_graph("extendedv2", database, filename="result")
#q.filter_questions("extendedV2", database, q1="Slower aggregation", q3="Yes",
#                   filename="result")
# q.contains_fragment("extendedV2", database, "DAEFRHDSG", filename="result")
# q.search_phrase("extendedV2", database, "pH", filename="result")
# q.subgraph_from_interactions("extendedV2", database, q1="Slower aggregation",q3="Yes", filename="result")
# q.subgraph_from_sequence("extendedV2", database, sequence="MEFVAKLFKFFKDLLGKFLGNN", filename="result")
#q.subgraph_from_amyloid("extendedV2", database, amyloid="Sup35",filename="result")
# q.subgraph_from_organism("extendedV2", database, organism="Frankia_sp_KB5", filename="result")
v.networkx_pyvis_graph('result')
