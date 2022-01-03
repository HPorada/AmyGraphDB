#new_db = database.connect_to_database('new_extendedV2', 'root', 'Amyloids')
#database.create_view(new_db, 'simple')
#simple_queries.filter_questions_simple(new_db, q1="Slower aggregation", q3="Yes", filename="result")
#extended_queries.filter_questions_extended(new_db, q1="Slower aggregation", q3="Yes", filename="result")

#sq.contains_fragment_simple(new_db, "DAEFRHDSG", "result")
#eq.contains_fragment_extended(new_db, "DAEFRHDSG", "result")
#e2q.contains_fragment_extendedV2(new_db, "DAEFRHDSG", "result")

#new_db = database.database_start('new_extendedV2', 'root', 'Amyloids', 'extendedv2')
#
# e2q.search_phrase_extendedV2(new_db, 'pH', 'result')
# #
# vf.graphviz_graph('result')
# vf.networkx_graph('result')

#database.create_json_files("extendedV2", "./initialisation_functions/data/questionnaire.xlsx", "./initialisation_functions/data/experiments.xlsx", "./initialisation_functions/extendedV2")

def example_function(int):
    """ Function takes int and returns int

    :param int: Integer
    :return: Integer
    """
    return int