from config.definitions import ROOT_DIR
from queries_functions import save_function as save


def filter_questions_extendedV2(database, q1=None, q2=None, q3=None, filename="result", directory=None):
    """This method executes a simple query filtering the database of EXTENDED v2 structure based on answers to 3 questions:
    \n
    1. Is the interactor affecting interactee's aggregating speed?
    (Faster aggregation/Slower aggregation/No aggregation/No effect/No information)
    \n
    2. Do fibrils of the interactee elongate by attaching to monomers/oligomers/fibrils of the interactor?
    (Yes, direct evidence/Yes, implied by kinetics/No/Formation of fibrils by the interactee is inhibited/No information)
    \n
    3. Is interaction resulting in heterogeneous fibrils consisting of interactor and interactee molecules?
    (Yes/No/No information)

    :param database: (StandardDatabase) Database in which query is to be executed.
    :param q1: (str) Answer to the first question defining the interaction. Optional.
    :param q2: (str) Answer to the second question defining the interaction. Optional.
    :param q3: (str) Answer to the third question defining the interaction. Optional.
    :param filename: (str) Name of the file where query result is to be saved. Optional.
    :param directory: (str) Path to the directory where file with query result is to be saved. Optional.
    """

    cursor = None

    if q1 is not None:
        q1 = q1.replace(".", "").replace(",", "").replace(";", "").replace(" ", "_")
    if q2 is not None:
        q2 = q2.replace(".", "").replace(",", "").replace(";", "").replace(" ", "_")
    if q3 is not None:
        q3 = q3.replace(".", "").replace(",", "").replace(";", "").replace(" ", "_")

    if q1 is not None and q2 is not None and q3 is not None:
        if (
                q1.lower() == "faster_aggregation" or q1.lower() == "slower_aggregation" or q1.lower() == "no_aggregation" or q1.lower() == "no_effect" or q1.lower() == "no_information") and (
                q2.lower() == "yes_direct_evidence" or q2.lower() == "yes_implied_by_kinetics" or q2.lower() == "formation_of_fibrils_by_the_interactee_is_inhibited" or q2.lower() == "no" or q2.lower() == "no_information") and (
                q3.lower() == "yes" or q3.lower() == "no" or q3.lower() == "no_information"):
            q1 = "question1/" + q1
            q2 = "question2/" + q2
            q3 = "question3/" + q3

            cursor = database.aql.execute(
                """let ints = (
                    for i in interactionsE
                        let q1 = (
                            for v, e, p in 1..1 outbound i._id graph "ExtendedV2"
                                filter v._id == @q1
                                return {"interactions": i}
                        )
                        let q2 = (
                            for v, e, p in 1..1 outbound i._id graph "ExtendedV2"
                                filter v._id == @q2
                                return {"interactions": i}
                        )
                        let q3 = (  
                            for v, e, p in 1..1 outbound i._id graph "ExtendedV2"
                                filter v._id == @q3
                                return {"interactions": i}
                        )
                    
                    let final = intersection(q1, q2, q3)
                    
                    for item in final 
                        return {"interactions": item.interactions}
                )
                        
                for i in ints
                    for v, e, p in 1..1 any i.interactions._id graph "ExtendedV2"
                        return p""",
                bind_vars={'q1': q1, 'q2': q2, 'q3': q3}
            )

    elif q1 is not None and q2 is not None:
        if (
                q1.lower() == "faster_aggregation" or q1.lower() == "slower_aggregation" or q1.lower() == "no_aggregation" or q1.lower() == "no_effect" or q1.lower() == "no_information") and (
                q2.lower() == "yes_direct_evidence" or q2.lower() == "yes_implied_by_kinetics" or q2.lower() == "formation_of_fibrils_by_the_interactee_is_inhibited" or q2.lower() == "no" or q2.lower() == "no_information"):
            q1 = "question1/" + q1
            q2 = "question2/" + q2

            cursor = database.aql.execute(
                """let ints = (
                    for i in interactionsE
                        let q1 = (
                            for v, e, p in 1..1 outbound i._id graph "ExtendedV2"
                                filter v._id == @q1
                                return {"interactions": i}
                        )
                        let q2 = (
                            for v, e, p in 1..1 outbound i._id graph "ExtendedV2"
                                filter v._id == @q2
                                return {"interactions": i}
                        )
                    
                    let final = intersection(q1, q2)
                    
                    for item in final 
                        return {"interactions": item.interactions}
                )
                        
                for i in ints
                    for v, e, p in 1..1 any i.interactions._id graph "ExtendedV2"
                        return p""",
                bind_vars={'q1': q1, 'q2': q2}
            )

    elif q2 is not None and q3 is not None:
        if (
                q2.lower() == "yes_direct_evidence" or q2.lower() == "yes_implied_by_kinetics" or q2.lower() == "formation_of_fibrils_by_the_interactee_is_inhibited" or q2.lower() == "no" or q2.lower() == "no_information") and (
                q3.lower() == "yes" or q3.lower() == "no" or q3.lower() == "no_information"):
            q2 = "question2/" + q2
            q3 = "question3/" + q3

            cursor = database.aql.execute(
                """let ints = (
                    for i in interactionsE
                        let q2 = (
                            for v, e, p in 1..1 outbound i._id graph "ExtendedV2"
                                filter v._id == @q2
                                return {"interactions": i}
                        )
                        let q3 = (  
                            for v, e, p in 1..1 outbound i._id graph "ExtendedV2"
                                filter v._id == @q3
                                return {"interactions": i}
                        )
                    
                    let final = intersection(q2, q3)
                    
                    for item in final 
                        return {"interactions": item.interactions}
                )
                        
                for i in ints
                    for v, e, p in 1..1 any i.interactions._id graph "ExtendedV2"
                        return p""",
                bind_vars={'q2': q2, 'q3': q3}
            )

    elif q1 is not None and q3 is not None:
        if (
                q1.lower() == "faster_aggregation" or q1.lower() == "slower_aggregation" or q1.lower() == "no_aggregation" or q1.lower() == "no_effect" or q1.lower() == "no_information") and (
                q3.lower() == "yes" or q3.lower() == "no" or q3.lower() == "no_information"):
            q1 = "question1/" + q1
            q3 = "question3/" + q3

            cursor = database.aql.execute(
                """let ints = (
                    for i in interactionsE
                        let q1 = (
                            for v, e, p in 1..1 outbound i._id graph "ExtendedV2"
                                filter v._id == @q1
                                return {"interactions": i}
                        )
                        let q3 = (  
                            for v, e, p in 1..1 outbound i._id graph "ExtendedV2"
                                filter v._id == @q3
                                return {"interactions": i}
                        )
                    
                    let final = intersection(q1, q3)
                    
                    for item in final 
                        return {"interactions": item.interactions}
                )
                        
                for i in ints
                    for v, e, p in 1..1 any i.interactions._id graph "ExtendedV2"
                        return p""",
                bind_vars={'q1': q1, 'q3': q3}
            )

    elif q1 is not None:
        if (
                q1.lower() == "faster_aggregation" or q1.lower() == "slower_aggregation" or q1.lower() == "no_aggregation" or q1.lower() == "no_effect" or q1.lower() == "no_information"):
            q1 = "question1/" + q1

            cursor = database.aql.execute(
                """let ints = (
                    for i in interactionsE
                        let q1 = (
                            for v, e, p in 1..1 outbound i._id graph "ExtendedV2"
                                filter v._id == @q1
                                return {"interactions": i}
                        )
                                        
                    for item in q1 
                        return {"interactions": item.interactions}
                )
                        
                for i in ints
                    for v, e, p in 1..1 any i.interactions._id graph "ExtendedV2"
                        return p""",
                bind_vars={'q1': q1}
            )

    elif q2 is not None:
        if (
                q2.lower() == "yes_direct_evidence" or q2.lower() == "yes_implied_by_kinetics" or q2.lower() == "formation_of_fibrils_by_the_interactee_is_inhibited" or q2.lower() == "no" or q2.lower() == "no_information"):
            q2 = "question2/" + q2

            cursor = database.aql.execute(
                """let ints = (
                    for i in interactionsE
                        let q2 = (
                            for v, e, p in 1..1 outbound i._id graph "ExtendedV2"
                                filter v._id == @q2
                                return {"interactions": i}
                        )
                                        
                    for item in q2 
                        return {"interactions": item.interactions}
                )
                        
                for i in ints
                    for v, e, p in 1..1 any i.interactions._id graph "ExtendedV2"
                        return p""",
                bind_vars={'q2': q2}
            )

    elif q3 is not None:
        if (
                q3.lower() == "yes" or q3.lower() == "no" or q3.lower() == "no_information"):
            q3 = "question3/" + q3

            cursor = database.aql.execute(
                """let ints = (
                    for i in interactionsE
                        let q3 = (
                            for v, e, p in 1..1 outbound i._id graph "ExtendedV2"
                                filter v._id == @q3
                                return {"interactions": i}
                        )
                                        
                    for item in q3 
                        return {"interactions": item.interactions}
                )
                        
                for i in ints
                    for v, e, p in 1..1 any i.interactions._id graph "ExtendedV2"
                        return p""",
                bind_vars={'q3': q3}
            )

    else:
        cursor = database.aql.execute(
            """let ints = (
                for i in interactionsE
                    let q = (
                        for v, e, p in 1..1 outbound i._id graph "ExtendedV2"
                            return {"interactions": i}
                    )
                                    
                for item in q 
                    return {"interactions": item.interactions}
            )
                    
            for i in ints
                for v, e, p in 1..1 any i.interactions._id graph "ExtendedV2"
                    return p"""
        )

    if cursor is not None:
        inter = [doc for doc in cursor]

        save.save_query_result(ROOT_DIR, directory, filename, inter)


def contains_fragment_extendedV2(database, fragment, filename="result", directory=None):
    """This method executes a query filtering the database of EXTENDED v2 structure in search of sequences containing chosen fragment.

    :param database: (StandardDatabase) Database in which query is to be executed.
    :param fragment: (str) Sequence fragment which is to be looked for.
    :param filename: (str) Name of the file where query result is to be saved. Optional.
    :param directory: (str) Path to the directory where file with query result is to be saved. Optional.
    """
    cursor = database.aql.execute(
        """for item in amyloidsE
            for v, e, p in 1..1 outbound item._id graph "ExtendedV2"
                filter contains(v.sequence, @fragment)
                return p""",
        bind_vars={'fragment': fragment}
    )

    inter = [doc for doc in cursor]

    save.save_query_result(ROOT_DIR, directory, filename, inter)


def search_phrase_extendedV2(database, keyword, filename="result", directory=None):
    """This method executes a query searching the database of EXTENDED v2 structure for mentions of chosen keyword.

    :param database: (StandardDatabase) Database in which query is to be executed.
    :param keyword: (str) Keyword which is to be searched for.
    :param filename: (str) Name of the file where query result is to be saved. Optional.
    :param directory: (str) Path to the directory where file with query result is to be saved. Optional.
    """
    cursor = database.aql.execute(
        """
        for i in extendedV2View 
            search phrase(i.general_remarks, @keyword, 'text_en') 
            return i""",
        bind_vars={'keyword': keyword}
    )

    inter = [doc for doc in cursor]

    save.save_query_result(ROOT_DIR, directory, filename, inter)
