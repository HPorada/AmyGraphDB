from initialisation_functions import initialisation as i
from queries_functions import queries as q
from visualisation_functions import visualisation as v

db = i.connect_to_database('new_extendedV2', 'root', 'Amyloids')

#q.subgraph_from_interactions('simple', db, q1='Slower aggregation', q2='Yes; implied by kinetics.', q3='No information', filename='result')
#q.subgraph_from_amyloid('extendedv2', db, 'Sup35', filename='result')

# q.full_graph('extendedv2', db, filename='result')

#q.subgraph_from_interactions('extendedV2', db, q1="Slower aggregation", q3="Yes", filename="result")

#q.subgraph_from_sequence('extended', db, sequence="MEFVAKLFKFFKDLLGKFLGNN", filename='result')

q.subgraph_from_amyloid("extendedV2", db, amyloid="Sup35", filename="result")

#q.subgraph_from_organism("extendedV2", db, organism="Frankia_sp_KB5",  filename="result")

v.graphviz_graph('result')
v.networkx_graph('result')
