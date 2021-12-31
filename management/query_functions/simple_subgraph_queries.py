import json


def subgraph_from_interactions(database, q1=None, q2=None, q3=None, filename="result"):
    if (
            q1 == "Faster aggregation" or q1 == "Slower aggregation" or q1 == "No aggregation" or q1 == "No effect" or q1 == "No information") and (
            q2 == "Yes, direct evidence." or q2 == "Yes; implied by kinetics." or q2 == "Formation of fibrils by the interactee is inhibited" or q2 == "No" or q2 == "No information") and (
            q3 == "Yes" or q3 == "No" or q3 == "No information"):

        cursor = database.aql.execute(
            """
            let seqs = (
                for s in sequences
                    for v, e, p in 1..1 any s._id graph "Simple"
                        filter e.question_1 == @q1
                        filter e.question_2 == @q2
                        filter e.question_3 == @q3
                        return {'paths': p, 'sequences': v}
            )
            
            let amys = (
                for item in seqs
                    for v, e, p in 1..1 inbound item.sequences._id graph "Simple"
                        filter v._id like "amyloids%"
                        return {'paths': p, 'amyloids': v}
            )
            
            for item in union(
                for item in seqs return item.paths,
                for item in amys return item.paths
            )
                return item""",
            bind_vars={'q1': q1, 'q2': q2, 'q3': q3}
        )

    elif (
            q1 == "Faster aggregation" or q1 == "Slower aggregation" or q1 == "No aggregation" or q1 == "No effect" or q1 == "No information") and (
            q2 == "Yes, direct evidence." or q2 == "Yes; implied by kinetics." or q2 == "Formation of fibrils by the interactee is inhibited" or q2 == "No" or q2 == "No information"):

        cursor = database.aql.execute(
            """let seqs = (
                for s in sequences
                    for v, e, p in 1..1 any s._id graph "Simple"
                        filter e.question_1 == @q1
                        filter e.question_2 == @q2
                        return {'paths': p, 'sequences': v}
            )
            
            let amys = (
                for item in seqs
                    for v, e, p in 1..1 inbound item.sequences._id graph "Simple"
                        filter v._id like "amyloids%"
                        return {'paths': p, 'amyloids': v}
            )
            
            for item in union(
                for item in seqs return item.paths,
                for item in amys return item.paths
            )
                return item""",
            bind_vars={'q1': q1, 'q2': q2}
        )

    elif (
            q2 == "Yes, direct evidence." or q2 == "Yes; implied by kinetics." or q2 == "Formation of fibrils by the interactee is inhibited" or q2 == "No" or q2 == "No information") and (
            q3 == "Yes" or q3 == "No" or q3 == "No information"):

        cursor = database.aql.execute(
            """let seqs = (
                for s in sequences
                    for v, e, p in 1..1 any s._id graph "Simple"
                        filter e.question_2 == @q2
                        filter e.question_3 == @q3
                        return {'paths': p, 'sequences': v}
            )
            
            let amys = (
                for item in seqs
                    for v, e, p in 1..1 inbound item.sequences._id graph "Simple"
                        filter v._id like "amyloids%"
                        return {'paths': p, 'amyloids': v}
            )
            
            for item in union(
                for item in seqs return item.paths,
                for item in amys return item.paths
            )
                return item""",
            bind_vars={'q2': q2, 'q3': q3}
        )

    elif (
            q1 == "Faster aggregation" or q1 == "Slower aggregation" or q1 == "No aggregation" or q1 == "No effect" or q1 == "No information") and (
            q3 == "Yes" or q3 == "No" or q3 == "No information"):

        cursor = database.aql.execute(
            """let seqs = (
                for s in sequences
                    for v, e, p in 1..1 any s._id graph "Simple"
                        filter e.question_1 == @q1
                        filter e.question_3 == @q3
                        return {'paths': p, 'sequences': v}
            )
            
            let amys = (
                for item in seqs
                    for v, e, p in 1..1 inbound item.sequences._id graph "Simple"
                        filter v._id like "amyloids%"
                        return {'paths': p, 'amyloids': v}
            )
            
            for item in union(
                for item in seqs return item.paths,
                for item in amys return item.paths
            )
                return item""",
            bind_vars={'q1': q1, 'q3': q3}
        )

    elif (
            q1 == "Faster aggregation" or q1 == "Slower aggregation" or q1 == "No aggregation" or q1 == "No effect" or q1 == "No information"):

        cursor = database.aql.execute(
            """
            let seqs = (
                for s in sequences
                    for v, e, p in 1..1 any s._id graph "Simple"
                        filter e.question_1 == @q1
                        return {'paths': p, 'sequences': v}
            )
            
            let amys = (
                for item in seqs
                    for v, e, p in 1..1 inbound item.sequences._id graph "Simple"
                        filter v._id like "amyloids%"
                        return {'paths': p, 'amyloids': v}
            )
            
            for item in union(
                for item in seqs return item.paths,
                for item in amys return item.paths
            )
                return item""",
            bind_vars={'q1': q1}
        )

    elif (
            q2 == "Yes, direct evidence." or q2 == "Yes; implied by kinetics." or q2 == "Formation of fibrils by the interactee is inhibited" or q2 == "No" or q2 == "No information"):

        cursor = database.aql.execute(
            """
            let seqs = (
                for s in sequences
                    for v, e, p in 1..1 any s._id graph "Simple"
                        filter e.question_2 == @q2
                        return {'paths': p, 'sequences': v}
            )
            
            let amys = (
                for item in seqs
                    for v, e, p in 1..1 inbound item.sequences._id graph "Simple"
                        filter v._id like "amyloids%"
                        return {'paths': p, 'amyloids': v}
            )
            
            for item in union(
                for item in seqs return item.paths,
                for item in amys return item.paths
            )
                return item""",
            bind_vars={'q2': q2}
        )

    elif (
            q3 == "Yes" or q3 == "No" or q3 == "No information"):

        cursor = database.aql.execute(
            """
            let seqs = (
                for s in sequences
                    for v, e, p in 1..1 any s._id graph "Simple"
                        filter e.question_3 == @q3
                        return {'paths': p, 'sequences': v}
            )
            
            let amys = (
                for item in seqs
                    for v, e, p in 1..1 inbound item.sequences._id graph "Simple"
                        filter v._id like "amyloids%"
                        return {'paths': p, 'amyloids': v}
            )
            
            for item in union(
                for item in seqs return item.paths,
                for item in amys return item.paths
            )
                return item""",
            bind_vars={'q3': q3}
        )

    else:
        cursor = database.aql.execute(
            """let seqs = (
                for s in sequences
                    for v, e, p in 1..1 any s._id graph "Simple"
                        return {'paths': p, 'sequences': v}
            )
            
            let amys = (
                for item in seqs
                    for v, e, p in 1..1 inbound item.sequences._id graph "Simple"
                        filter v._id like "amyloids%"
                        return {'paths': p, 'amyloids': v}
            )
            
            for item in union(
                for item in seqs return item.paths,
                for item in amys return item.paths
            )
                return item"""
        )

    inter = [doc for doc in cursor]

    with open(f"./management/json_data/{filename}.json", "w") as outfile:
        json.dump(inter, outfile)


def subgraph_from_sequence(database, sequence=None, name=None, filename="result"):
    cursor = database.aql.execute(
        """let seqs = (
                for s in sequences
                    for v, e, p in 1..1 any s._id graph "Simple"
                        filter s.sequence == @seqZatem 
                        return {'paths': p, 'sequences': v}
            )
                        
            let amys = (
                for item in seqs
                    for v, e, p in 1..1 inbound item.sequences._id graph "Simple"
                        filter v._id like "amyloids%"
                        return {'paths': p, 'amyloids': v}
            )
            
            for item in union(
                for item in seqs return item.paths,
                for item in amys return item.paths
            )
                return item""",
        bind_vars={'seq': sequence}
    )

    inter = [doc for doc in cursor]

    with open(f"./management/json_data/{filename}.json", "w") as outfile:
        json.dump(inter, outfile)


def subgraph_from_amyloid(database, amyloid, filename="result"):
    cursor = database.aql.execute(
        """let amys = (
                for a in amyloids
                    filter a.name == @name
                    return {'amyloids': a}
             )
             
            let seqs = (
                for item in amys
                    for v, e, p in 1..1 outbound item.amyloids._id graph "Simple"
                        return {'paths': p, 'sequences': v}
             )
             
            let seqs2 = (
                for item in seqs
                    for v, e, p in 1..1 outbound item.sequences._id graph "Simple"
                        return {'paths': p, 'sequences': v}
            )
                        
            let amys2 = (
                for item in seqs2
                    for v, e, p in 1..1 inbound item.sequences._id graph "Simple"
                        filter v._id like "amyloids%"
                        return {'paths': p, 'amyloids': v}
            )
            
            let seqs_fin = union_distinct(seqs, seqs2)
            
            for item in union(
                for item in seqs_fin return item.paths,
                for item in amys2 return item.paths
            )
                return item""",
        bind_vars={'name': amyloid}
    )

    inter = [doc for doc in cursor]

    with open(f"./management/json_data/{filename}.json", "w") as outfile:
        json.dump(inter, outfile)


def subgraph_from_organism(database, organism, filename="result"):
    cursor = database.aql.execute(
        """let orgs = (
                for o in organisms
                    filter o._key == @org
                    return {'organisms': o}
            )
            
            let amys = (
                for item in orgs
                    for v, e, p in 1..1 outbound item.organisms._id graph "Simple"
                        return {'paths': p, 'amyloids': v}
            )
            
            let seqs = (
                for item in amys
                    for v, e, p in 1..1 outbound item.amyloids._id graph "Simple"
                        return {'paths': p, 'sequences': v}
            )
            
            let seqs2 = (
                for item in seqs
                    for v, e, p in 1..1 outbound item.sequences._id graph "Simple"
                        return {'paths': p, 'sequences': v}
            )
                        
            let amys2 = (
                for item in seqs2
                    for v, e, p in 1..1 inbound item.sequences._id graph "Simple"
                        filter v._id like "amyloids%"
                        return {'paths': p, 'amyloids': v}
            )
            
            let orgs2 = (
                for item in amys2
                    for v, e, p in 1..1 inbound item.amyloids._id graph "Simple"
                        return {'paths': p, 'organisms': v}
            )
            
            let amys_fin = union_distinct(amys, amys2)
            let seqs_fin = union_distinct(seqs, seqs2)
            
            
            for item in union(
                for item in seqs_fin return item.paths,
                for item in amys_fin return item.paths,
                for item in orgs2 return item.paths
            )
                return item""",
        bind_vars={'org': organism}
    )

    inter = [doc for doc in cursor]

    with open(f"./management/json_data/{filename}.json", "w") as outfile:
        json.dump(inter, outfile)