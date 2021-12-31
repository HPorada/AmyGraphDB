import json


def subgraph_from_interactions_extendedV2(database, q1=None, q2=None, q3=None, filename="result", directory=None):
    q1 = q1.replace(".", "").replace(",", "").replace(";", "").replace(" ", "_")
    q2 = q2.replace(".", "").replace(",", "").replace(";", "").replace(" ", "_")
    q3 = q3.replace(".", "").replace(",", "").replace(";", "").replace(" ", "_")

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
                        let que1 = (
                            for v, e, p in 1..1 outbound i._id graph "ExtendedV2" 
                                filter v._id == @q1 
                                return {"interactions": i}
                        )        
                        let que2 = (
                            for v, e, p in 1..1 outbound i._id graph "ExtendedV2" 
                                filter v._id == @q2 
                                return {"interactions": i}
                        )        
                        let que3 = (
                            for v, e, p in 1..1 outbound i._id graph "ExtendedV2" 
                                filter v._id == @q3 
                                return {"interactions": i}
                        )
    
                        let final = intersection(que1, que2, que3)
    
                        for item in final 
                            return {"interactions": item.interactions}
                        )
    
                let ints_paths = (
                    for i in ints
                        for v, e, p in 1..1 outbound i.interactions._id graph "ExtendedV2"
                            return {"paths": p}
                    )
    
                let seqs = (
                    for i in ints
                        for v, e, p in 1..1 inbound i.interactions._id graph "ExtendedV2"
                            return {"paths": p, "sequences": v}
                )
    
                let amys = (
                    for item in seqs
                        for v, e, p in 1..1 inbound item.sequences._id graph "ExtendedV2"
                            return distinct {"paths": p, "amyloids": v}
                )  
    
                let orgs = (
                    for item in amys
                        for v, e, p in 1..1 inbound item.amyloids._id graph "ExtendedV2"
                            return distinct {"paths": p, "organisms": v}
                )
    
                let props = (
                    for item in orgs
                        for v, e, p in 1..1 inbound item.organisms._id graph "ExtendedV2"
                            return distinct {"paths": p, "properties": v}
                )
    
                for item in union(
                    for item in ints_paths return item.paths,
                    for item in seqs return item.paths,
                    for item in amys return item.paths,
                    for item in orgs return item.paths,
                    for item in props return item.paths
                )
                    return item""",
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
                        let que1 = (
                            for v, e, p in 1..1 outbound i._id graph "ExtendedV2" 
                                filter v._id == @q1 
                                return {"interactions": i}
                        )        
                        let que2 = (
                            for v, e, p in 1..1 outbound i._id graph "ExtendedV2" 
                                filter v._id == @q2 
                                return {"interactions": i}
                        )        
        
                        let final = intersection(que1, que2)
        
                        for item in final 
                            return {"interactions": item.interactions}
                        )
        
                let ints_paths = (
                    for i in ints
                        for v, e, p in 1..1 outbound i.interactions._id graph "ExtendedV2"
                            return {"paths": p}
                    )
        
                let seqs = (
                    for i in ints
                        for v, e, p in 1..1 inbound i.interactions._id graph "ExtendedV2"
                            return {"paths": p, "sequences": v}
                )
        
                let amys = (
                    for item in seqs
                        for v, e, p in 1..1 inbound item.sequences._id graph "ExtendedV2"
                            return distinct {"paths": p, "amyloids": v}
                )  
        
                let orgs = (
                    for item in amys
                        for v, e, p in 1..1 inbound item.amyloids._id graph "ExtendedV2"
                            return distinct {"paths": p, "organisms": v}
                )
        
                let props = (
                    for item in orgs
                        for v, e, p in 1..1 inbound item.organisms._id graph "ExtendedV2"
                            return distinct {"paths": p, "properties": v}
                )
        
                for item in union(
                    for item in ints_paths return item.paths,
                    for item in seqs return item.paths,
                    for item in amys return item.paths,
                    for item in orgs return item.paths,
                    for item in props return item.paths
                )
                    return item""",
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
                        let que2 = (
                            for v, e, p in 1..1 outbound i._id graph "ExtendedV2" 
                                filter v._id == @q2 
                                return {"interactions": i}
                        )        
                        let que3 = (
                            for v, e, p in 1..1 outbound i._id graph "ExtendedV2" 
                                filter v._id == @q3 
                                return {"interactions": i}
                        )
        
                        let final = intersection(que2, que3)
        
                        for item in final 
                            return {"interactions": item.interactions}
                        )
        
                let ints_paths = (
                    for i in ints
                        for v, e, p in 1..1 outbound i.interactions._id graph "ExtendedV2"
                            return {"paths": p}
                    )
        
                let seqs = (
                    for i in ints
                        for v, e, p in 1..1 inbound i.interactions._id graph "ExtendedV2"
                            return {"paths": p, "sequences": v}
                )
        
                let amys = (
                    for item in seqs
                        for v, e, p in 1..1 inbound item.sequences._id graph "ExtendedV2"
                            return distinct {"paths": p, "amyloids": v}
                )  
        
                let orgs = (
                    for item in amys
                        for v, e, p in 1..1 inbound item.amyloids._id graph "ExtendedV2"
                            return distinct {"paths": p, "organisms": v}
                )
        
                let props = (
                    for item in orgs
                        for v, e, p in 1..1 inbound item.organisms._id graph "ExtendedV2"
                            return distinct {"paths": p, "properties": v}
                )
        
                for item in union(
                    for item in ints_paths return item.paths,
                    for item in seqs return item.paths,
                    for item in amys return item.paths,
                    for item in orgs return item.paths,
                    for item in props return item.paths
                )
                    return item""",
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
                        let que1 = (
                            for v, e, p in 1..1 outbound i._id graph "ExtendedV2" 
                                filter v._id == @q1 
                                return {"interactions": i}
                        )        
                        let que3 = (
                            for v, e, p in 1..1 outbound i._id graph "ExtendedV2" 
                                filter v._id == @q3 
                                return {"interactions": i}
                        )
        
                        let final = intersection(que1, que3)
        
                        for item in final 
                            return {"interactions": item.interactions}
                        )
        
                let ints_paths = (
                    for i in ints
                        for v, e, p in 1..1 outbound i.interactions._id graph "ExtendedV2"
                            return {"paths": p}
                    )
        
                let seqs = (
                    for i in ints
                        for v, e, p in 1..1 inbound i.interactions._id graph "ExtendedV2"
                            return {"paths": p, "sequences": v}
                )
        
                let amys = (
                    for item in seqs
                        for v, e, p in 1..1 inbound item.sequences._id graph "ExtendedV2"
                            return distinct {"paths": p, "amyloids": v}
                )  
        
                let orgs = (
                    for item in amys
                        for v, e, p in 1..1 inbound item.amyloids._id graph "ExtendedV2"
                            return distinct {"paths": p, "organisms": v}
                )
        
                let props = (
                    for item in orgs
                        for v, e, p in 1..1 inbound item.organisms._id graph "ExtendedV2"
                            return distinct {"paths": p, "properties": v}
                )
        
                for item in union(
                    for item in ints_paths return item.paths,
                    for item in seqs return item.paths,
                    for item in amys return item.paths,
                    for item in orgs return item.paths,
                    for item in props return item.paths
                )
                    return item""",
            bind_vars={'q1': q1, 'q3': q3}
        )

    elif (
            q1.lower() == "faster_aggregation" or q1.lower() == "slower_aggregation" or q1.lower() == "no_aggregation" or q1.lower() == "no_effect" or q1.lower() == "no_information"):

        q1 = "question1/" + q1

        cursor = database.aql.execute(
            """
            let ints = (
        
                for i in interactionsE
                    
                    let q1 = (
                        for v, e, p in 1..1 outbound i._id graph "ExtendedV2"
                            filter v._id == @q1
                            return {"interactions": i}
                    )
                
                for item in q1 
                    return {"interactions": item.interactions}
            )
             
            let ints_paths = (
                    for i in ints
                        for v, e, p in 1..1 outbound i.interactions._id graph "ExtendedV2"
                            return {"paths": p}
            )
            
            let seqs = (
                for i in ints
                    for v, e, p in 1..1 inbound i.interactions._id graph "ExtendedV2"
                        return {"paths": p, "sequences": v}
            )
                    
            let amys = (
                for item in seqs
                    for v, e, p in 1..1 inbound item.sequences._id graph "ExtendedV2"
                        return distinct {"paths": p, "amyloids": v}
            )  
            
            let orgs = (
                for item in amys
                    for v, e, p in 1..1 inbound item.amyloids._id graph "ExtendedV2"
                        return distinct {"paths": p, "organisms": v}
            )
            
            let props = (
                for item in orgs
                    for v, e, p in 1..1 inbound item.organisms._id graph "ExtendedV2"
                        return distinct {"paths": p, "properties": v}
            )
                
            for item in union(
                for item in ints_paths return item.paths,
                for item in seqs return item.paths,
                for item in amys return item.paths,
                for item in orgs return item.paths,
                for item in props return item.paths
            )
                return item
            """,
            bind_vars={'q1': q1}
        )

    elif (
            q2.lower() == "yes_direct_evidence" or q2.lower() == "yes_implied_by_kinetics" or q2.lower() == "formation_of_fibrils_by_the_interactee_is_inhibited" or q2.lower() == "no" or q2.lower() == "no_information"):

        q2 = "question2/" + q2

        cursor = database.aql.execute(
            """
            let ints = (
        
                for i in interactionsE
        
                    let q2 = (
                        for v, e, p in 1..1 outbound i._id graph "ExtendedV2"
                            filter v._id == @q2
                            return {"interactions": i}
                    )
        
                for item in q2 
                    return {"interactions": item.interactions}
            )
        
            let ints_paths = (
                    for i in ints
                        for v, e, p in 1..1 outbound i.interactions._id graph "ExtendedV2"
                            return {"paths": p}
            )
        
            let seqs = (
                for i in ints
                    for v, e, p in 1..1 inbound i.interactions._id graph "ExtendedV2"
                        return {"paths": p, "sequences": v}
            )
        
            let amys = (
                for item in seqs
                    for v, e, p in 1..1 inbound item.sequences._id graph "ExtendedV2"
                        return distinct {"paths": p, "amyloids": v}
            )  
        
            let orgs = (
                for item in amys
                    for v, e, p in 1..1 inbound item.amyloids._id graph "ExtendedV2"
                        return distinct {"paths": p, "organisms": v}
            )
        
            let props = (
                for item in orgs
                    for v, e, p in 1..1 inbound item.organisms._id graph "ExtendedV2"
                        return distinct {"paths": p, "properties": v}
            )
        
            for item in union(
                for item in ints_paths return item.paths,
                for item in seqs return item.paths,
                for item in amys return item.paths,
                for item in orgs return item.paths,
                for item in props return item.paths
            )
                return item
            """,
            bind_vars={'q2': q2}
        )

    elif (
            q3.lower() == "yes" or q3.lower() == "no" or q3.lower() == "no_information"):

        q3 = "question3/" + q3

        cursor = database.aql.execute(
            """
            let ints = (
        
                for i in interactionsE
        
                    let q3 = (
                        for v, e, p in 1..1 outbound i._id graph "ExtendedV2"
                            filter v._id == @q3
                            return {"interactions": i}
                    )
        
                for item in q3
                    return {"interactions": item.interactions}
            )
        
            let ints_paths = (
                    for i in ints
                        for v, e, p in 1..1 outbound i.interactions._id graph "ExtendedV2"
                            return {"paths": p}
            )
        
            let seqs = (
                for i in ints
                    for v, e, p in 1..1 inbound i.interactions._id graph "ExtendedV2"
                        return {"paths": p, "sequences": v}
            )
        
            let amys = (
                for item in seqs
                    for v, e, p in 1..1 inbound item.sequences._id graph "ExtendedV2"
                        return distinct {"paths": p, "amyloids": v}
            )  
        
            let orgs = (
                for item in amys
                    for v, e, p in 1..1 inbound item.amyloids._id graph "ExtendedV2"
                        return distinct {"paths": p, "organisms": v}
            )
        
            let props = (
                for item in orgs
                    for v, e, p in 1..1 inbound item.organisms._id graph "ExtendedV2"
                        return distinct {"paths": p, "properties": v}
            )
        
            for item in union(
                for item in ints_paths return item.paths,
                for item in seqs return item.paths,
                for item in amys return item.paths,
                for item in orgs return item.paths,
                for item in props return item.paths
            )
                return item
            """,
            bind_vars={'q3': q3}
        )

    else:
        cursor = database.aql.execute(
            """let ints = (
                    for i in interactionsE
                            return {"interactions": i}
                        )        
        
                let ints_paths = (
                    for i in ints
                        for v, e, p in 1..1 outbound i.interactions._id graph "ExtendedV2"
                            return {"paths": p}
                    )
        
                let seqs = (
                    for i in ints
                        for v, e, p in 1..1 inbound i.interactions._id graph "ExtendedV2"
                            return {"paths": p, "sequences": v}
                )
        
                let amys = (
                    for item in seqs
                        for v, e, p in 1..1 inbound item.sequences._id graph "ExtendedV2"
                            return distinct {"paths": p, "amyloids": v}
                )  
        
                let orgs = (
                    for item in amys
                        for v, e, p in 1..1 inbound item.amyloids._id graph "ExtendedV2"
                            return distinct {"paths": p, "organisms": v}
                )
        
                let props = (
                    for item in orgs
                        for v, e, p in 1..1 inbound item.organisms._id graph "ExtendedV2"
                            return distinct {"paths": p, "properties": v}
                )
        
                for item in union(
                    for item in ints_paths return item.paths,
                    for item in seqs return item.paths,
                    for item in amys return item.paths,
                    for item in orgs return item.paths,
                    for item in props return item.paths
                )
                    return item"""
        )

    inter = [i for i in cursor]

    if directory is not None:
        with open(f"{directory}/{filename}.json", "w") as outfile:
            json.dump(inter, outfile)
    else:
        with open(f"./management/json_data/{filename}.json", "w") as outfile:
            json.dump(inter, outfile)


def subgraph_from_sequence_extendedV2(database, sequence=None, name=None, filename="result", directory=None):
    if sequence is not None and name is not None:
        cursor = database.aql.execute(
            """let seqs = (
                for s in sequencesE
                    filter s.sequence == @seq
                    filter s._key = @name
                    return {"sequences": s}
            )

            let ints = (
                for item in seqs
                    for v, e, p in 1..1 outbound item.sequences._id graph "ExtendedV2"
                        return {"paths": p, "interactions": v}
            )

            let ques = (
                for item in ints
                    for v, e, p in 1..1 outbound item.interactions._id graph "ExtendedV2"
                        return {"paths": p, "questions": v}
            )

            let seqs2 = (
                for item in ints
                    for v, e, p in 1..1 inbound item.interactions._id graph "ExtendedV2"
                        return {"paths": p, "sequences": v}
            )

            let amys = (
                for item in seqs2
                    for v, e, p in 1..1 inbound item.sequences._id graph "ExtendedV2"
                        return distinct{"paths": p, "amyloids": v}
            )

            let orgs = (
                for item in amys
                    for v, e, p in 1..1 inbound item.amyloids._id graph "ExtendedV2"
                        return distinct {"paths": p, "organisms": v}
            )

            let props = (
                for item in orgs
                    for v, e, p in 1..1 inbound item.organisms._id graph "ExtendedV2"
                        return distinct {"paths": p, "properties": v}
            )

            for item in union(
                for item in ints return item.paths,
                for item in ques return item.paths,
                for item in amys return item.paths,
                for item in orgs return item.paths,
                for item in props return item.paths,
                for item in seqs2 return item.paths
            )
                return item""",
            bind_vars={'seq': sequence, 'name': name}
        )

    elif sequence is not None:
        cursor = database.aql.execute(
            """let seqs = (
                for s in sequencesE
                    filter s.sequence == @seq
                    return {"sequences": s}
            )
            
            let ints = (
                for item in seqs
                    for v, e, p in 1..1 outbound item.sequences._id graph "ExtendedV2"
                        return {"paths": p, "interactions": v}
            )
            
            let ques = (
                for item in ints
                    for v, e, p in 1..1 outbound item.interactions._id graph "ExtendedV2"
                        return {"paths": p, "questions": v}
            )
            
            let seqs2 = (
                for item in ints
                    for v, e, p in 1..1 inbound item.interactions._id graph "ExtendedV2"
                        return {"paths": p, "sequences": v}
            )
            
            let amys = (
                for item in seqs2
                    for v, e, p in 1..1 inbound item.sequences._id graph "ExtendedV2"
                        return distinct{"paths": p, "amyloids": v}
            )
            
            let orgs = (
                for item in amys
                    for v, e, p in 1..1 inbound item.amyloids._id graph "ExtendedV2"
                        return distinct {"paths": p, "organisms": v}
            )
            
            let props = (
                for item in orgs
                    for v, e, p in 1..1 inbound item.organisms._id graph "ExtendedV2"
                        return distinct {"paths": p, "properties": v}
            )
            
            for item in union(
                for item in ints return item.paths,
                for item in ques return item.paths,
                for item in amys return item.paths,
                for item in orgs return item.paths,
                for item in props return item.paths,
                for item in seqs2 return item.paths
            )
                return item""",
            bind_vars={'seq': sequence}
        )

    elif name is not None:
        cursor = database.aql.execute(
            """let seqs = (
                for s in sequencesE
                    filter s._key == @name
                    return {"sequences": s}
            )

            let ints = (
                for item in seqs
                    for v, e, p in 1..1 outbound item.sequences._id graph "ExtendedV2"
                        return {"paths": p, "interactions": v}
            )

            let ques = (
                for item in ints
                    for v, e, p in 1..1 outbound item.interactions._id graph "ExtendedV2"
                        return {"paths": p, "questions": v}
            )

            let seqs2 = (
                for item in ints
                    for v, e, p in 1..1 inbound item.interactions._id graph "ExtendedV2"
                        return {"paths": p, "sequences": v}
            )

            let amys = (
                for item in seqs2
                    for v, e, p in 1..1 inbound item.sequences._id graph "ExtendedV2"
                        return distinct{"paths": p, "amyloids": v}
            )

            let orgs = (
                for item in amys
                    for v, e, p in 1..1 inbound item.amyloids._id graph "ExtendedV2"
                        return distinct {"paths": p, "organisms": v}
            )

            let props = (
                for item in orgs
                    for v, e, p in 1..1 inbound item.organisms._id graph "ExtendedV2"
                        return distinct {"paths": p, "properties": v}
            )

            for item in union(
                for item in ints return item.paths,
                for item in ques return item.paths,
                for item in amys return item.paths,
                for item in orgs return item.paths,
                for item in props return item.paths,
                for item in seqs2 return item.paths
            )
                return item""",
            bind_vars={'name': name}
        )

    else:
        cursor = database.aql.execute(
            """let seqs = (
                for s in sequencesE
                    return {"sequences": s}
            )

            let ints = (
                for item in seqs
                    for v, e, p in 1..1 outbound item.sequences._id graph "ExtendedV2"
                        return {"paths": p, "interactions": v}
            )

            let ques = (
                for item in ints
                    for v, e, p in 1..1 outbound item.interactions._id graph "ExtendedV2"
                        return {"paths": p, "questions": v}
            )

            let seqs2 = (
                for item in ints
                    for v, e, p in 1..1 inbound item.interactions._id graph "ExtendedV2"
                        return {"paths": p, "sequences": v}
            )

            let amys = (
                for item in seqs2
                    for v, e, p in 1..1 inbound item.sequences._id graph "ExtendedV2"
                        return distinct{"paths": p, "amyloids": v}
            )

            let orgs = (
                for item in amys
                    for v, e, p in 1..1 inbound item.amyloids._id graph "ExtendedV2"
                        return distinct {"paths": p, "organisms": v}
            )

            let props = (
                for item in orgs
                    for v, e, p in 1..1 inbound item.organisms._id graph "ExtendedV2"
                        return distinct {"paths": p, "properties": v}
            )

            for item in union(
                for item in ints return item.paths,
                for item in ques return item.paths,
                for item in amys return item.paths,
                for item in orgs return item.paths,
                for item in props return item.paths,
                for item in seqs2 return item.paths
            )
                return item"""
        )

    inter = [i for i in cursor]

    if directory is not None:
        with open(f"{directory}/{filename}.json", "w") as outfile:
            json.dump(inter, outfile)
    else:
        with open(f"./management/json_data/{filename}.json", "w") as outfile:
            json.dump(inter, outfile)


def subgraph_from_amyloid_extendedV2(database, amyloid, filename="result", directory=None):
    cursor = database.aql.execute(
        """let amys = (
            for a in amyloidsE
                filter a.name == @amy
                return {"amyloids": a}
        )
        
        let seqs = (
            for item in amys
                for v, e, p in 1..1 outbound item.amyloids._id graph "ExtendedV2"
                    return distinct{"paths": p, "sequences": v}
        )
        
        let ints = (
            for item in seqs
                for v, e, p in 1..1 outbound item.sequences._id graph "ExtendedV2"
                    return distinct{"paths": p, "interactions": v}
        )
        
        let ques = (
            for item in ints
                for v, e, p in 1..1 outbound item.interactions._id graph "ExtendedV2"
                    return distinct{"paths": p, "questions": v}
        )
        
        let seqs2 = (
            for item in ints
                for v, e, p in 1..1 inbound item.interactions._id graph "ExtendedV2"
                    return distinct{"paths": p, "sequences": v}
        )
        
        let amys2 = (
            for item in seqs2
                for v, e, p in 1..1 inbound item.sequences._id graph "ExtendedV2"
                    return distinct{"paths": p, "amyloids": v}
        )
        
        let orgs = (
            for item in amys2
                for v, e, p in 1..1 inbound item.amyloids._id graph "ExtendedV2"
                    return distinct {"paths": p, "organisms": v}
        )
        
        let props = (
            for item in orgs
                for v, e, p in 1..1 inbound item.organisms._id graph "ExtendedV2"
                    return distinct {"paths": p, "properties": v}
        )
        
        /*let orgs2 = (
            for item in amys2
                for v, e, p in 1..1 inbound item.amyloids._id graph "ExtendedV2"
                    return distinct {"paths": p, "organisms": v}
        )
        
        let props2 = (
            for item in orgs2
                for v, e, p in 1..1 inbound item.organisms._id graph "ExtendedV2"
                    return distinct {"paths": p, "properties": v}
        )*/
        
        for item in union(
            for item in ints return item.paths,
            for item in ques return item.paths,
            for item in orgs return item.paths,
            for item in props return item.paths,
            for item in seqs2 return item.paths,
            for item in amys2 return item.paths
        )
            return item""",
        bind_vars={'amy': amyloid}
    )

    inter = [i for i in cursor]

    if directory is not None:
        with open(f"{directory}/{filename}.json", "w") as outfile:
            json.dump(inter, outfile)
    else:
        with open(f"./management/json_data/{filename}.json", "w") as outfile:
            json.dump(inter, outfile)


def subgraph_from_organism_extendedV2(database, organism, filename="result", directory=None):
    cursor = database.aql.execute(
        """let orgs = (
            for o in organismsE
                filter o._key == @org
                return {"organisms": o}
        )
        
        let amys = (
            for item in orgs
                for v, e, p in 1..1 outbound item.organisms._id graph "ExtendedV2"
                    return distinct {"paths": p, "amyloids": v}
        )
        
        let seqs = (
            for item in amys
                for v, e, p in 1..1 outbound item.amyloids._id graph "ExtendedV2"
                    return distinct{"paths": p, "sequences": v}
        )
        
        let ints = (
            for item in seqs
                for v, e, p in 1..1 outbound item.sequences._id graph "ExtendedV2"
                    return distinct{"paths": p, "interactions": v}
        )
        
        let ques = (
            for item in ints
                for v, e, p in 1..1 outbound item.interactions._id graph "ExtendedV2"
                    return distinct{"paths": p, "questions": v}
        )
        
        let seqs2 = (
            for item in ints
                for v, e, p in 1..1 inbound item.interactions._id graph "ExtendedV2"
                    return distinct{"paths": p, "sequences": v}
        )
        
        let amys2 = (
            for item in seqs2
                for v, e, p in 1..1 inbound item.sequences._id graph "ExtendedV2"
                    return distinct{"paths": p, "amyloids": v}
        )
        
        let orgs2 = (
            for item in amys2
                for v, e, p in 1..1 inbound item.amyloids._id graph "ExtendedV2"
                    return distinct {"paths": p, "organisms": v}
        )
        
        /*let props = (
            for item in orgs
                for v, e, p in 1..1 inbound item.organisms._id graph "ExtendedV2"
                    return distinct {"paths": p, "properties": v}
        )*/
        
        let props2 = (
            for item in orgs2
                for v, e, p in 1..1 inbound item.organisms._id graph "ExtendedV2"
                    return distinct {"paths": p, "properties": v}
        )
        
        for item in union(
            for item in ints return item.paths,
            for item in ques return item.paths,
           /* for item in seqs return item.paths,
            for item in amys return item.paths,
            for item in props return item.paths,*/
            for item in seqs2 return item.paths,
            for item in amys2 return item.paths,
            for item in orgs2 return item.paths,
            for item in props2 return item.paths
        )
            return item""",
        bind_vars={'org': organism}
    )

    inter = [i for i in cursor]

    if directory is not None:
        with open(f"{directory}/{filename}.json", "w") as outfile:
            json.dump(inter, outfile)
    else:
        with open(f"./management/json_data/{filename}.json", "w") as outfile:
            json.dump(inter, outfile)
