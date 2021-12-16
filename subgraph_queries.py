import json


def subgraph(database, q1, q2, q3, filename="result"):
    aql = database.aql

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

    inter = [i for i in cursor]

    # for x in inter:
    #     print(x)

    with open(f"json_data/{filename}.json", "w") as outfile:
        json.dump(inter, outfile)
