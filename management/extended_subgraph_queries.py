import json


def subgraph_from_interactions_extended(database, q1=None, q2=None, q3=None, filename="result", directory=None):
    """This method executes a subgraph query filtering the database of EXTENDED structure based on answers to 3 questions:
    1. Is the interactor affecting interactee's aggregating speed?
    (Faster aggregation/Slower aggregation/No aggregation/No effect/No information)
    2. Do fibrils of the interactee elongate by attaching to monomers/oligomers/fibrils of the interactor?
    (Yes, direct evidence/Yes, implied by kinetics/No/Formation of fibrils by the interactee is inhibited/No information)
    3. Is interaction resulting in heterogeneous fibrils consisting of interactor and interactee molecules?
    (Yes/No/No information)

    :param database: (StandardDatabase) Database in which query is to be executed.:
    :param q1: (str) Answer to the first question defining the interaction. Optional.
    :param q2: (str) Answer to the second question defining the interaction. Optional.
    :param q3: (str) Answer to the third question defining the interaction. Optional.
    :param filename: (str) Name of the file where query result is to be saved. Optional.
    :param directory: (str) Path to the directory where file with query result is to be saved. Optional.
    """
    if (
            q1 == "Faster aggregation" or q1 == "Slower aggregation" or q1 == "No aggregation" or q1 == "No effect" or q1 == "No information") and (
            q2 == "Yes, direct evidence." or q2 == "Yes; implied by kinetics." or q2 == "Formation of fibrils by the interactee is inhibited" or q2 == "No" or q2 == "No information") and (
            q3 == "Yes" or q3 == "No" or q3 == "No information"):

        cursor = database.aql.execute(
            """let ints = (
                for i in interactionsE
                    filter i.question_1 == @q1
                    filter i.question_2 == @q2
                    filter i.question_3 == @q3
                    return {'interactions': i}
                    )
                
            let seqs = (
                for i in ints
                    for v, e, p in 1..1 inbound i.interactions._id graph "Extended"
                        return {"paths": p, "sequences": v}
            )
                
            let amys = (
                for item in seqs
                    for v, e, p in 1..1 inbound item.sequences._id graph "Extended"
                        return distinct {"paths": p, "amyloids": v}
            )  
                
            let orgs = (
                for item in amys
                    for v, e, p in 1..1 inbound item.amyloids._id graph "Extended"
                        return distinct {"paths": p, "organisms": v}
            )
                
            for item in union(
                for item in seqs return item.paths,
                for item in amys return item.paths,
                for item in orgs return item.paths
            )
                return item""",
            bind_vars={'q1': q1, 'q2': q2, 'q3': q3}
        )

    elif (
            q1 == "Faster aggregation" or q1 == "Slower aggregation" or q1 == "No aggregation" or q1 == "No effect" or q1 == "No information") and (
            q2 == "Yes, direct evidence." or q2 == "Yes; implied by kinetics." or q2 == "Formation of fibrils by the interactee is inhibited" or q2 == "No" or q2 == "No information"):

        cursor = database.aql.execute(
            """let ints = (
                for i in interactionsE
                    filter i.question_1 == @q1
                    filter i.question_2 == @q2
                    return {'interactions': i}
                    )
                
            let seqs = (
                for i in ints
                    for v, e, p in 1..1 inbound i.interactions._id graph "Extended"
                        return {"paths": p, "sequences": v}
            )
                
            let amys = (
                for item in seqs
                    for v, e, p in 1..1 inbound item.sequences._id graph "Extended"
                        return distinct {"paths": p, "amyloids": v}
            )  
                
            let orgs = (
                for item in amys
                    for v, e, p in 1..1 inbound item.amyloids._id graph "Extended"
                        return distinct {"paths": p, "organisms": v}
            )
                
            for item in union(
                for item in seqs return item.paths,
                for item in amys return item.paths,
                for item in orgs return item.paths
            )
                return item""",
            bind_vars={'q1': q1, 'q2': q2}
        )

    elif (
            q2 == "Yes, direct evidence." or q2 == "Yes; implied by kinetics." or q2 == "Formation of fibrils by the interactee is inhibited" or q2 == "No" or q2 == "No information") and (
            q3 == "Yes" or q3 == "No" or q3 == "No information"):

        cursor = database.aql.execute(
            """let ints = (
                for i in interactionsE
                    filter i.question_2 == @q2
                    filter i.question_3 == @q3
                    return {'interactions': i}
                    )
                
            let seqs = (
                for i in ints
                    for v, e, p in 1..1 inbound i.interactions._id graph "Extended"
                        return {"paths": p, "sequences": v}
            )
                
            let amys = (
                for item in seqs
                    for v, e, p in 1..1 inbound item.sequences._id graph "Extended"
                        return distinct {"paths": p, "amyloids": v}
            )  
                
            let orgs = (
                for item in amys
                    for v, e, p in 1..1 inbound item.amyloids._id graph "Extended"
                        return distinct {"paths": p, "organisms": v}
            )
                
            for item in union(
                for item in seqs return item.paths,
                for item in amys return item.paths,
                for item in orgs return item.paths
            )
                return item""",
            bind_vars={'q2': q2, 'q3': q3}
        )

    elif (
            q1 == "Faster aggregation" or q1 == "Slower aggregation" or q1 == "No aggregation" or q1 == "No effect" or q1 == "No information") and (
            q3 == "Yes" or q3 == "No" or q3 == "No information"):

        cursor = database.aql.execute(
            """let ints = (
                for i in interactionsE
                    filter i.question_1 == @q1
                    filter i.question_3 == @q3
                    return {'interactions': i}
                    )
                
            let seqs = (
                for i in ints
                    for v, e, p in 1..1 inbound i.interactions._id graph "Extended"
                        return {"paths": p, "sequences": v}
            )
                
            let amys = (
                for item in seqs
                    for v, e, p in 1..1 inbound item.sequences._id graph "Extended"
                        return distinct {"paths": p, "amyloids": v}
            )  
                
            let orgs = (
                for item in amys
                    for v, e, p in 1..1 inbound item.amyloids._id graph "Extended"
                        return distinct {"paths": p, "organisms": v}
            )
                
            for item in union(
                for item in seqs return item.paths,
                for item in amys return item.paths,
                for item in orgs return item.paths
            )
                return item""",
            bind_vars={'q1': q1, 'q3': q3}
        )

    elif (
            q1 == "Faster aggregation" or q1 == "Slower aggregation" or q1 == "No aggregation" or q1 == "No effect" or q1 == "No information"):

        cursor = database.aql.execute(
            """
            let ints = (
                for i in interactionsE
                    filter i.question_1 == @q1
                    return {'interactions': i}
                    )
                
            let seqs = (
                for i in ints
                    for v, e, p in 1..1 inbound i.interactions._id graph "Extended"
                        return {"paths": p, "sequences": v}
            )
                
            let amys = (
                for item in seqs
                    for v, e, p in 1..1 inbound item.sequences._id graph "Extended"
                        return distinct {"paths": p, "amyloids": v}
            )  
                
            let orgs = (
                for item in amys
                    for v, e, p in 1..1 inbound item.amyloids._id graph "Extended"
                        return distinct {"paths": p, "organisms": v}
            )
                
            for item in union(
                for item in seqs return item.paths,
                for item in amys return item.paths,
                for item in orgs return item.paths
            )
                return item""",
            bind_vars={'q1': q1}
        )

    elif (
            q2 == "Yes, direct evidence." or q2 == "Yes; implied by kinetics." or q2 == "Formation of fibrils by the interactee is inhibited" or q2 == "No" or q2 == "No information"):

        cursor = database.aql.execute(
            """
            let ints = (
                for i in interactionsE
                    filter i.question_2 == @q2
                    return {'interactions': i}
                    )
                
            let seqs = (
                for i in ints
                    for v, e, p in 1..1 inbound i.interactions._id graph "Extended"
                        return {"paths": p, "sequences": v}
            )
                
            let amys = (
                for item in seqs
                    for v, e, p in 1..1 inbound item.sequences._id graph "Extended"
                        return distinct {"paths": p, "amyloids": v}
            )  
                
            let orgs = (
                for item in amys
                    for v, e, p in 1..1 inbound item.amyloids._id graph "Extended"
                        return distinct {"paths": p, "organisms": v}
            )
                
            for item in union(
                for item in seqs return item.paths,
                for item in amys return item.paths,
                for item in orgs return item.paths
            )
                return item""",
            bind_vars={'q2': q2}
        )

    elif (
            q3 == "Yes" or q3 == "No" or q3 == "No information"):

        cursor = database.aql.execute(
            """
            let ints = (
                for i in interactionsE
                    filter i.question_3 == @q3
                    return {'interactions': i}
                    )
                
            let seqs = (
                for i in ints
                    for v, e, p in 1..1 inbound i.interactions._id graph "Extended"
                        return {"paths": p, "sequences": v}
            )
                
            let amys = (
                for item in seqs
                    for v, e, p in 1..1 inbound item.sequences._id graph "Extended"
                        return distinct {"paths": p, "amyloids": v}
            )  
                
            let orgs = (
                for item in amys
                    for v, e, p in 1..1 inbound item.amyloids._id graph "Extended"
                        return distinct {"paths": p, "organisms": v}
            )
                
            for item in union(
                for item in seqs return item.paths,
                for item in amys return item.paths,
                for item in orgs return item.paths
            )
                return item""",
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
                        for v, e, p in 1..1 outbound i.interactions._id graph "Extended"
                            return {"paths": p}
                    )

                let seqs = (
                    for i in ints
                        for v, e, p in 1..1 inbound i.interactions._id graph "Extended"
                            return {"paths": p, "sequences": v}
                )

                let amys = (
                    for item in seqs
                        for v, e, p in 1..1 inbound item.sequences._id graph "Extended"
                            return distinct {"paths": p, "amyloids": v}
                )  

                let orgs = (
                    for item in amys
                        for v, e, p in 1..1 inbound item.amyloids._id graph "Extended"
                            return distinct {"paths": p, "organisms": v}
                )

                for item in union(
                    for item in ints_paths return item.paths,
                    for item in seqs return item.paths,
                    for item in amys return item.paths,
                    for item in orgs return item.paths
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


def subgraph_from_sequence_extended(database, sequence=None, name=None, filename="result", directory=None):
    """This method executes a subgraph query filtering the database of EXTENDED structure based on sequence or name of a sequence.

    :param database: (StandardDatabase) Database in which query is to be executed.
    :param sequence: (str) Sequence which is to be searched for. Optional.
    :param name: (str) Name of a sequence which is to be searched for. Optional.
    :param filename: (str) Name of the file where query result is to be saved. Optional.
    :param directory: (str) Path to the directory where file with query result is to be saved. Optional.
    """
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
                    for v, e, p in 1..1 outbound item.sequences._id graph "Extended"
                        return {"paths": p, "interactions": v}
            )

            let seqs2 = (
                for item in ints
                    for v, e, p in 1..1 inbound item.interactions._id graph "Extended"
                        return {"paths": p, "sequences": v}
            )

            let amys = (
                for item in seqs2
                    for v, e, p in 1..1 inbound item.sequences._id graph "Extended"
                        return distinct{"paths": p, "amyloids": v}
            )

            let orgs = (
                for item in amys
                    for v, e, p in 1..1 inbound item.amyloids._id graph "Extended"
                        return distinct {"paths": p, "organisms": v}
            )

            for item in union(
                for item in ints return item.paths,
                for item in amys return item.paths,
                for item in orgs return item.paths,
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
                    for v, e, p in 1..1 outbound item.sequences._id graph "Extended"
                        return {"paths": p, "interactions": v}
            )

            let seqs2 = (
                for item in ints
                    for v, e, p in 1..1 inbound item.interactions._id graph "Extended"
                        return {"paths": p, "sequences": v}
            )

            let amys = (
                for item in seqs2
                    for v, e, p in 1..1 inbound item.sequences._id graph "Extended"
                        return distinct{"paths": p, "amyloids": v}
            )

            let orgs = (
                for item in amys
                    for v, e, p in 1..1 inbound item.amyloids._id graph "Extended"
                        return distinct {"paths": p, "organisms": v}
            )

            for item in union(
                for item in ints return item.paths,
                for item in amys return item.paths,
                for item in orgs return item.paths,
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
                    for v, e, p in 1..1 outbound item.sequences._id graph "Extended"
                        return {"paths": p, "interactions": v}
            )

            let seqs2 = (
                for item in ints
                    for v, e, p in 1..1 inbound item.interactions._id graph "Extended"
                        return {"paths": p, "sequences": v}
            )

            let amys = (
                for item in seqs2
                    for v, e, p in 1..1 inbound item.sequences._id graph "Extended"
                        return distinct{"paths": p, "amyloids": v}
            )

            let orgs = (
                for item in amys
                    for v, e, p in 1..1 inbound item.amyloids._id graph "Extended"
                        return distinct {"paths": p, "organisms": v}
            )

            for item in union(
                for item in ints return item.paths,
                for item in amys return item.paths,
                for item in orgs return item.paths,
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
                    for v, e, p in 1..1 outbound item.sequences._id graph "Extended"
                        return {"paths": p, "interactions": v}
            )

            let seqs2 = (
                for item in ints
                    for v, e, p in 1..1 inbound item.interactions._id graph "Extended"
                        return {"paths": p, "sequences": v}
            )

            let amys = (
                for item in seqs2
                    for v, e, p in 1..1 inbound item.sequences._id graph "Extended"
                        return distinct{"paths": p, "amyloids": v}
            )

            let orgs = (
                for item in amys
                    for v, e, p in 1..1 inbound item.amyloids._id graph "Extended"
                        return distinct {"paths": p, "organisms": v}
            )

            for item in union(
                for item in ints return item.paths,
                for item in amys return item.paths,
                for item in orgs return item.paths,
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


def subgraph_from_amyloid_extended(database, amyloid, filename="result", directory=None):
    """This method executes a subgraph query filtering the database of EXTENDED structure based on name of an amyloid.

    :param database: (StandardDatabase) Database in which query is to be executed.
    :param amyloid: (str) Name of an amyloid which s to be searched for.
    :param filename: (str) Name of the file where query result is to be saved. Optional.
    :param directory: (str) Path to the directory where file with query result is to be saved. Optional.
    """
    cursor = database.aql.execute(
        """let amys = (
            for a in amyloidsE
                filter a.name == @amy
                return {"amyloids": a}
        )

        let seqs = (
            for item in amys
                for v, e, p in 1..1 outbound item.amyloids._id graph "Extended"
                    return distinct{"paths": p, "sequences": v}
        )

        let ints = (
            for item in seqs
                for v, e, p in 1..1 outbound item.sequences._id graph "Extended"
                    return distinct{"paths": p, "interactions": v}
        )


        let seqs2 = (
            for item in ints
                for v, e, p in 1..1 inbound item.interactions._id graph "Extended"
                    return distinct{"paths": p, "sequences": v}
        )

        let amys2 = (
            for item in seqs2
                for v, e, p in 1..1 inbound item.sequences._id graph "Extended"
                    return distinct{"paths": p, "amyloids": v}
        )

        let orgs = (
            for item in amys2
                for v, e, p in 1..1 inbound item.amyloids._id graph "Extended"
                    return distinct {"paths": p, "organisms": v}
        )


        for item in union(
            for item in ints return item.paths,
            for item in orgs return item.paths,
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


def subgraph_from_organism_extended(database, organism, filename="result", directory=None):
    """This method executes a subgraph query filtering the database of EXTENDED structure based on name of an organism.

    :param database: (StandardDatabase) Database in which query is to be executed.
    :param organism: (str) Name of an organism which is to be searched for.
    :param filename: (str) Name of the file where query result is to be saved. Optional.
    :param directory: (str) Path to the directory where file with query result is to be saved. Optional.
    """
    cursor = database.aql.execute(
        """let orgs = (
                for o in organismsE
                    filter o._key == @org
                    return {"organisms": o}
            )
            
            let amys = (
                for item in orgs
                    for v, e, p in 1..1 outbound item.organisms._id graph "Extended"
                        return distinct {"paths": p, "amyloids": v}
            )
            
            let seqs = (
                for item in amys
                    for v, e, p in 1..1 outbound item.amyloids._id graph "Extended"
                        return distinct{"paths": p, "sequences": v}
            )
            
            let ints = (
                for item in seqs
                    for v, e, p in 1..1 outbound item.sequences._id graph "Extended"
                        return distinct{"paths": p, "interactions": v}
            )
            
            let seqs2 = (
                for item in ints
                    for v, e, p in 1..1 inbound item.interactions._id graph "Extended"
                        return distinct{"paths": p, "sequences": v}
            )
            
            let amys2 = (
                for item in seqs2
                    for v, e, p in 1..1 inbound item.sequences._id graph "Extended"
                        return distinct{"paths": p, "amyloids": v}
            )
            
            let orgs2 = (
                for item in amys2
                    for v, e, p in 1..1 inbound item.amyloids._id graph "Extended"
                        return distinct {"paths": p, "organisms": v}
            )
            
            
            for item in union(
                for item in ints return item.paths,
                for item in seqs2 return item.paths,
                for item in amys2 return item.paths,
                for item in orgs2 return item.paths
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
