import json


def filter_questions_extendedV2(database, q1, q2, q3, filename="result", directory=None):
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

    elif (
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

    elif (
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

    elif (
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

    elif (
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

    elif (
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

    elif (
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

    inter = [doc for doc in cursor]

    if directory is not None:
        with open(f"{directory}/{filename}.json", "w") as outfile:
            json.dump(inter, outfile)
    else:
        with open(f"./management/json_data/{filename}.json", "w") as outfile:
            json.dump(inter, outfile)


def contains_fragment_extendedV2(database, fragment, filename="result", directory=None):
    cursor = database.aql.execute(
        """for item in amyloidsE
            for v, e, p in 1..1 outbound item._id graph "ExtendedV2"
                filter contains(v.sequence, @fragment)
                return p""",
        bind_vars={'fragment': fragment}
    )

    inter = [doc for doc in cursor]

    if directory is not None:
        with open(f"{directory}/{filename}.json", "w") as outfile:
            json.dump(inter, outfile)
    else:
        with open(f"./management/json_data/{filename}.json", "w") as outfile:
            json.dump(inter, outfile)


def search_phrase_extendedV2(database, keyword, filename="result", directory=None):
    cursor = database.aql.execute(
        """
        for i in extendedV2View 
            search phrase(i.general_remarks, @keyword, 'text_en') 
            return i""",
        bind_vars={'keyword': keyword}
    )

    inter = [doc for doc in cursor]

    if directory is not None:
        with open(f"{directory}/{filename}.json", "w") as outfile:
            json.dump(inter, outfile)
    else:
        with open(f"./management/json_data/{filename}.json", "w") as outfile:
            json.dump(inter, outfile)

# def search_connected_extendedV2(database, collection, start, filename="result"):
#     ()
