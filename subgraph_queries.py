import json


def subgraph_from_interactions(database, q1=None, q2=None, q3=None, filename="result"):
    aql = database.aql

    if q1 == (
            "Faster aggregation" or "Slower aggregation" or "No aggregation" or "No effect" or "No information") and q2 == (
            "Yes, direct evidence." or "Yes; implied by kinetics." or "Formation of fibrils by the interactee is inhibited" or "No" or "No information") and q3 == (
            "Yes" or "No" or "No information"):

        q1 = "question1/" + q1.replace(".", "").replace(",", "").replace(";", "").replace(" ", "_")
        q2 = "question2/" + q2.replace(".", "").replace(",", "").replace(";", "").replace(" ", "_")
        q3 = "question3/" + q3.replace(".", "").replace(",", "").replace(";", "").replace(" ", "_")

        cursor = database.aql.execute(
            """let ints = (
                    for i in interactionsE
                        let que1 = (
                            for v, e, p in 1..1 outbound i._id graph "ExtendedAndEdges" 
                                filter v._id == @q1 
                                return {"interactions": i}
                        )        
                        let que2 = (
                            for v, e, p in 1..1 outbound i._id graph "ExtendedAndEdges" 
                                filter v._id == @q2 
                                return {"interactions": i}
                        )        
                        let que3 = (
                            for v, e, p in 1..1 outbound i._id graph "ExtendedAndEdges" 
                                filter v._id == @q3 
                                return {"interactions": i}
                        )

                        let final = intersection(que1, que2, que3)

                        for item in final 
                            return {"interactions": item.interactions}
                        )

                let ints_paths = (
                    for i in ints
                        for v, e, p in 1..1 outbound i.interactions._id graph "ExtendedAndEdges"
                            return {"paths": p}
                    )

                let seqs = (
                    for i in ints
                        for v, e, p in 1..1 inbound i.interactions._id graph "ExtendedAndEdges"
                            return {"paths": p, "sequences": v}
                )

                let amys = (
                    for item in seqs
                        for v, e, p in 1..1 inbound item.sequences._id graph "ExtendedAndEdges"
                            return distinct {"paths": p, "amyloids": v}
                )  

                let orgs = (
                    for item in amys
                        for v, e, p in 1..1 inbound item.amyloids._id graph "ExtendedAndEdges"
                            return distinct {"paths": p, "organisms": v}
                )

                let props = (
                    for item in orgs
                        for v, e, p in 1..1 inbound item.organisms._id graph "ExtendedAndEdges"
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

    elif q1 == (
            "Faster aggregation" or "Slower aggregation" or "No aggregation" or "No effect" or "No information") and q2 == (
            "Yes, direct evidence." or "Yes; implied by kinetics." or "Formation of fibrils by the interactee is inhibited" or "No" or "No information"):

        q1 = "question1/" + q1.replace(".", "").replace(",", "").replace(";", "").replace(" ", "_")
        q2 = "question2/" + q2.replace(".", "").replace(",", "").replace(";", "").replace(" ", "_")

        cursor = database.aql.execute(
            """let ints = (
                    for i in interactionsE
                        let que1 = (
                            for v, e, p in 1..1 outbound i._id graph "ExtendedAndEdges" 
                                filter v._id == @q1 
                                return {"interactions": i}
                        )        
                        let que2 = (
                            for v, e, p in 1..1 outbound i._id graph "ExtendedAndEdges" 
                                filter v._id == @q2 
                                return {"interactions": i}
                        )        

                        let final = intersection(que1, que2)

                        for item in final 
                            return {"interactions": item.interactions}
                        )

                let ints_paths = (
                    for i in ints
                        for v, e, p in 1..1 outbound i.interactions._id graph "ExtendedAndEdges"
                            return {"paths": p}
                    )

                let seqs = (
                    for i in ints
                        for v, e, p in 1..1 inbound i.interactions._id graph "ExtendedAndEdges"
                            return {"paths": p, "sequences": v}
                )

                let amys = (
                    for item in seqs
                        for v, e, p in 1..1 inbound item.sequences._id graph "ExtendedAndEdges"
                            return distinct {"paths": p, "amyloids": v}
                )  

                let orgs = (
                    for item in amys
                        for v, e, p in 1..1 inbound item.amyloids._id graph "ExtendedAndEdges"
                            return distinct {"paths": p, "organisms": v}
                )

                let props = (
                    for item in orgs
                        for v, e, p in 1..1 inbound item.organisms._id graph "ExtendedAndEdges"
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

    elif q2 == (
            "Yes, direct evidence." or "Yes; implied by kinetics." or "Formation of fibrils by the interactee is inhibited" or "No" or "No information") and q3 == (
            "Yes" or "No" or "No information"):

        q2 = "question2/" + q2.replace(".", "").replace(",", "").replace(";", "").replace(" ", "_")
        q3 = "question3/" + q3.replace(".", "").replace(",", "").replace(";", "").replace(" ", "_")

        cursor = database.aql.execute(
            """let ints = (
                    for i in interactionsE       
                        let que2 = (
                            for v, e, p in 1..1 outbound i._id graph "ExtendedAndEdges" 
                                filter v._id == @q2 
                                return {"interactions": i}
                        )        
                        let que3 = (
                            for v, e, p in 1..1 outbound i._id graph "ExtendedAndEdges" 
                                filter v._id == @q3 
                                return {"interactions": i}
                        )

                        let final = intersection(que2, que3)

                        for item in final 
                            return {"interactions": item.interactions}
                        )

                let ints_paths = (
                    for i in ints
                        for v, e, p in 1..1 outbound i.interactions._id graph "ExtendedAndEdges"
                            return {"paths": p}
                    )

                let seqs = (
                    for i in ints
                        for v, e, p in 1..1 inbound i.interactions._id graph "ExtendedAndEdges"
                            return {"paths": p, "sequences": v}
                )

                let amys = (
                    for item in seqs
                        for v, e, p in 1..1 inbound item.sequences._id graph "ExtendedAndEdges"
                            return distinct {"paths": p, "amyloids": v}
                )  

                let orgs = (
                    for item in amys
                        for v, e, p in 1..1 inbound item.amyloids._id graph "ExtendedAndEdges"
                            return distinct {"paths": p, "organisms": v}
                )

                let props = (
                    for item in orgs
                        for v, e, p in 1..1 inbound item.organisms._id graph "ExtendedAndEdges"
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

    elif q1 == (
            "Faster aggregation" or "Slower aggregation" or "No aggregation" or "No effect" or "No information") and q3 == (
            "Yes" or "No" or "No information"):

        q1 = "question1/" + q1.replace(".", "").replace(",", "").replace(";", "").replace(" ", "_")
        q3 = "question3/" + q3.replace(".", "").replace(",", "").replace(";", "").replace(" ", "_")

        cursor = database.aql.execute(
            """let ints = (
                    for i in interactionsE
                        let que1 = (
                            for v, e, p in 1..1 outbound i._id graph "ExtendedAndEdges" 
                                filter v._id == @q1 
                                return {"interactions": i}
                        )        
                        let que3 = (
                            for v, e, p in 1..1 outbound i._id graph "ExtendedAndEdges" 
                                filter v._id == @q3 
                                return {"interactions": i}
                        )

                        let final = intersection(que1, que3)

                        for item in final 
                            return {"interactions": item.interactions}
                        )

                let ints_paths = (
                    for i in ints
                        for v, e, p in 1..1 outbound i.interactions._id graph "ExtendedAndEdges"
                            return {"paths": p}
                    )

                let seqs = (
                    for i in ints
                        for v, e, p in 1..1 inbound i.interactions._id graph "ExtendedAndEdges"
                            return {"paths": p, "sequences": v}
                )

                let amys = (
                    for item in seqs
                        for v, e, p in 1..1 inbound item.sequences._id graph "ExtendedAndEdges"
                            return distinct {"paths": p, "amyloids": v}
                )  

                let orgs = (
                    for item in amys
                        for v, e, p in 1..1 inbound item.amyloids._id graph "ExtendedAndEdges"
                            return distinct {"paths": p, "organisms": v}
                )

                let props = (
                    for item in orgs
                        for v, e, p in 1..1 inbound item.organisms._id graph "ExtendedAndEdges"
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

    elif q1 == (
            "Faster aggregation" or "Slower aggregation" or "No aggregation" or "No effect" or "No information"):

        q1 = "question1/" + q1.replace(".", "").replace(",", "").replace(";", "").replace(" ", "_")

        cursor = database.aql.execute(
            """
            let ints = (

                for i in interactionsE
                    
                    let q1 = (
                        for v, e, p in 1..1 outbound i._id graph "ExtendedAndEdges"
                            filter v._id == @q1
                            return {"interactions": i}
                    )
                
                for item in q1 
                    return {"interactions": item.interactions}
            )
             
            let ints_paths = (
                    for i in ints
                        for v, e, p in 1..1 outbound i.interactions._id graph "ExtendedAndEdges"
                            return {"paths": p}
            )
            
            let seqs = (
                for i in ints
                    for v, e, p in 1..1 inbound i.interactions._id graph "ExtendedAndEdges"
                        return {"paths": p, "sequences": v}
            )
                    
            let amys = (
                for item in seqs
                    for v, e, p in 1..1 inbound item.sequences._id graph "ExtendedAndEdges"
                        return distinct {"paths": p, "amyloids": v}
            )  
            
            let orgs = (
                for item in amys
                    for v, e, p in 1..1 inbound item.amyloids._id graph "ExtendedAndEdges"
                        return distinct {"paths": p, "organisms": v}
            )
            
            let props = (
                for item in orgs
                    for v, e, p in 1..1 inbound item.organisms._id graph "ExtendedAndEdges"
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

    elif q2 == (
            "Yes, direct evidence." or "Yes; implied by kinetics." or "Formation of fibrils by the interactee is inhibited" or "No" or "No information"):

        q2 = "question2/" + q2.replace(".", "").replace(",", "").replace(";", "").replace(" ", "_")

        cursor = database.aql.execute(
            """
            let ints = (

                for i in interactionsE

                    let q2 = (
                        for v, e, p in 1..1 outbound i._id graph "ExtendedAndEdges"
                            filter v._id == @q2
                            return {"interactions": i}
                    )

                for item in q2 
                    return {"interactions": item.interactions}
            )

            let ints_paths = (
                    for i in ints
                        for v, e, p in 1..1 outbound i.interactions._id graph "ExtendedAndEdges"
                            return {"paths": p}
            )

            let seqs = (
                for i in ints
                    for v, e, p in 1..1 inbound i.interactions._id graph "ExtendedAndEdges"
                        return {"paths": p, "sequences": v}
            )

            let amys = (
                for item in seqs
                    for v, e, p in 1..1 inbound item.sequences._id graph "ExtendedAndEdges"
                        return distinct {"paths": p, "amyloids": v}
            )  

            let orgs = (
                for item in amys
                    for v, e, p in 1..1 inbound item.amyloids._id graph "ExtendedAndEdges"
                        return distinct {"paths": p, "organisms": v}
            )

            let props = (
                for item in orgs
                    for v, e, p in 1..1 inbound item.organisms._id graph "ExtendedAndEdges"
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

    elif q3 == (
            "Yes" or "No" or "No information"):

        q3 = "question3/" + q3.replace(".", "").replace(",", "").replace(";", "").replace(" ", "_")

        cursor = database.aql.execute(
            """
            let ints = (

                for i in interactionsE

                    let q3 = (
                        for v, e, p in 1..1 outbound i._id graph "ExtendedAndEdges"
                            filter v._id == @q3
                            return {"interactions": i}
                    )

                for item in q3
                    return {"interactions": item.interactions}
            )

            let ints_paths = (
                    for i in ints
                        for v, e, p in 1..1 outbound i.interactions._id graph "ExtendedAndEdges"
                            return {"paths": p}
            )

            let seqs = (
                for i in ints
                    for v, e, p in 1..1 inbound i.interactions._id graph "ExtendedAndEdges"
                        return {"paths": p, "sequences": v}
            )

            let amys = (
                for item in seqs
                    for v, e, p in 1..1 inbound item.sequences._id graph "ExtendedAndEdges"
                        return distinct {"paths": p, "amyloids": v}
            )  

            let orgs = (
                for item in amys
                    for v, e, p in 1..1 inbound item.amyloids._id graph "ExtendedAndEdges"
                        return distinct {"paths": p, "organisms": v}
            )

            let props = (
                for item in orgs
                    for v, e, p in 1..1 inbound item.organisms._id graph "ExtendedAndEdges"
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
                        for v, e, p in 1..1 outbound i._id graph "ExtendedAndEdges"
                            return {"interactions": i}
                        )        

                let ints_paths = (
                    for i in ints
                        for v, e, p in 1..1 outbound i.interactions._id graph "ExtendedAndEdges"
                            return {"paths": p}
                    )

                let seqs = (
                    for i in ints
                        for v, e, p in 1..1 inbound i.interactions._id graph "ExtendedAndEdges"
                            return {"paths": p, "sequences": v}
                )

                let amys = (
                    for item in seqs
                        for v, e, p in 1..1 inbound item.sequences._id graph "ExtendedAndEdges"
                            return distinct {"paths": p, "amyloids": v}
                )  

                let orgs = (
                    for item in amys
                        for v, e, p in 1..1 inbound item.amyloids._id graph "ExtendedAndEdges"
                            return distinct {"paths": p, "organisms": v}
                )

                let props = (
                    for item in orgs
                        for v, e, p in 1..1 inbound item.organisms._id graph "ExtendedAndEdges"
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

    with open(f"json_data/{filename}.json", "w") as outfile:
        json.dump(inter, outfile)


def subgraph_from_sequence(database, sequence, filename="result"):
    aql = database.aql

    cursor = database.aql.execute(
        """let seqs = (
            for s in sequencesE
                filter s.sequence == @seq
                return {"sequences": s}
        )
        
        let ints = (
            for item in seqs
                for v, e, p in 1..1 outbound item.sequences._id graph "ExtendedAndEdges"
                    return {"paths": p, "interactions": v}
        )
        
        let ques = (
            for item in ints
                for v, e, p in 1..1 outbound item.interactions._id graph "ExtendedAndEdges"
                    return {"paths": p, "questions": v}
        )
        
        let seqs2 = (
            for item in ints
                for v, e, p in 1..1 inbound item.interactions._id graph "ExtendedAndEdges"
                    return {"paths": p, "sequences": v}
        )
        
        let amys = (
            for item in seqs2
                for v, e, p in 1..1 inbound item.sequences._id graph "ExtendedAndEdges"
                    return distinct{"paths": p, "amyloids": v}
        )
        
        let orgs = (
            for item in amys
                for v, e, p in 1..1 inbound item.amyloids._id graph "ExtendedAndEdges"
                    return distinct {"paths": p, "organisms": v}
        )
        
        let props = (
            for item in orgs
                for v, e, p in 1..1 inbound item.organisms._id graph "ExtendedAndEdges"
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

    inter = [i for i in cursor]

    with open(f"json_data/{filename}.json", "w") as outfile:
        json.dump(inter, outfile)


def subgraph_from_amyloid(database, amyloid, filename="result"):
    aql = database.aql

    cursor = database.aql.execute(
        """let amys = (
            for a in amyloidsE
                filter a.name == @amy
                return {"amyloids": a}
        )
        
        let seqs = (
            for item in amys
                for v, e, p in 1..1 outbound item.amyloids._id graph "ExtendedAndEdges"
                    return distinct{"paths": p, "sequences": v}
        )
        
        let ints = (
            for item in seqs
                for v, e, p in 1..1 outbound item.sequences._id graph "ExtendedAndEdges"
                    return distinct{"paths": p, "interactions": v}
        )
        
        let ques = (
            for item in ints
                for v, e, p in 1..1 outbound item.interactions._id graph "ExtendedAndEdges"
                    return distinct{"paths": p, "questions": v}
        )
        
        let seqs2 = (
            for item in ints
                for v, e, p in 1..1 inbound item.interactions._id graph "ExtendedAndEdges"
                    return distinct{"paths": p, "sequences": v}
        )
        
        let amys2 = (
            for item in seqs2
                for v, e, p in 1..1 inbound item.sequences._id graph "ExtendedAndEdges"
                    return distinct{"paths": p, "amyloids": v}
        )
        
        let orgs = (
            for item in amys2
                for v, e, p in 1..1 inbound item.amyloids._id graph "ExtendedAndEdges"
                    return distinct {"paths": p, "organisms": v}
        )
        
        let props = (
            for item in orgs
                for v, e, p in 1..1 inbound item.organisms._id graph "ExtendedAndEdges"
                    return distinct {"paths": p, "properties": v}
        )
        
        /*let orgs2 = (
            for item in amys2
                for v, e, p in 1..1 inbound item.amyloids._id graph "ExtendedAndEdges"
                    return distinct {"paths": p, "organisms": v}
        )
        
        let props2 = (
            for item in orgs2
                for v, e, p in 1..1 inbound item.organisms._id graph "ExtendedAndEdges"
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

    with open(f"json_data/{filename}.json", "w") as outfile:
        json.dump(inter, outfile)


def subgraph_from_organism(database, organism, filename="result"):
    aql = database.aql

    cursor = database.aql.execute(
        """let orgs = (
            for o in organismsE
                filter o._id == @org
                return {"organisms": o}
        )
        
        let amys = (
            for item in orgs
                for v, e, p in 1..1 outbound item.organisms._id graph "ExtendedAndEdges"
                    return distinct {"paths": p, "amyloids": v}
        )
        
        let seqs = (
            for item in amys
                for v, e, p in 1..1 outbound item.amyloids._id graph "ExtendedAndEdges"
                    return distinct{"paths": p, "sequences": v}
        )
        
        let ints = (
            for item in seqs
                for v, e, p in 1..1 outbound item.sequences._id graph "ExtendedAndEdges"
                    return distinct{"paths": p, "interactions": v}
        )
        
        let ques = (
            for item in ints
                for v, e, p in 1..1 outbound item.interactions._id graph "ExtendedAndEdges"
                    return distinct{"paths": p, "questions": v}
        )
        
        let seqs2 = (
            for item in ints
                for v, e, p in 1..1 inbound item.interactions._id graph "ExtendedAndEdges"
                    return distinct{"paths": p, "sequences": v}
        )
        
        let amys2 = (
            for item in seqs2
                for v, e, p in 1..1 inbound item.sequences._id graph "ExtendedAndEdges"
                    return distinct{"paths": p, "amyloids": v}
        )
        
        let orgs2 = (
            for item in amys2
                for v, e, p in 1..1 inbound item.amyloids._id graph "ExtendedAndEdges"
                    return distinct {"paths": p, "organisms": v}
        )
        
        /*let props = (
            for item in orgs
                for v, e, p in 1..1 inbound item.organisms._id graph "ExtendedAndEdges"
                    return distinct {"paths": p, "properties": v}
        )*/
        
        let props2 = (
            for item in orgs2
                for v, e, p in 1..1 inbound item.organisms._id graph "ExtendedAndEdges"
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

    with open(f"json_data/{filename}.json", "w") as outfile:
        json.dump(inter, outfile)
