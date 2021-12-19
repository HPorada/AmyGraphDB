import json


def filter_extended_v2(database, q1, q2, q3, filename="result"):
    aql = database.aql

    q1 = "question1/" + q1.replace(".", "").replace(",", "").replace(";", "").replace(" ", "_")
    q2 = "question2/" + q2.replace(".", "").replace(",", "").replace(";", "").replace(" ", "_")
    q3 = "question3/" + q3.replace(".", "").replace(",", "").replace(";", "").replace(" ", "_")

    cursor = database.aql.execute(
        """let ints = (
                for i in interactionsE
                    let q1 = (
                        for v, e, p in 1..1 outbound i._id graph "ExtendedAndEdges"
                            filter v._id == @q1
                            return {"interactions": i}
                    )
                    let q2 = (
                        for v, e, p in 1..1 outbound i._id graph "ExtendedAndEdges"
                            filter v._id == @q2
                            return {"interactions": i}
                    )
                    let q3 = (  
                        for v, e, p in 1..1 outbound i._id graph "ExtendedAndEdges"
                            filter v._id == @q3
                            return {"interactions": i}
                    )
                
                let final = intersection(q1, q2, q3)
                
                for item in final 
                    return {"interactions": item.interactions}
            )
                    
            let ints_paths = (
                    for i in ints
                        for v, e, p in 1..1 any i.interactions._id graph "ExtendedAndEdges"
                            return {"paths": p}
            )
            
            for item in ints_paths
                return item.paths""",
        bind_vars={'q1': q1, 'q2': q2, 'q3': q3}
    )

    inter = [doc for doc in cursor]

    # for x in inter:
    #     print(x)

    with open(f"./json_data/{filename}.json", "w") as outfile:
        json.dump(inter, outfile)


def contains_extended_v2(database, fragment, filename="result"):
    aql = database.aql

    cursor = database.aql.execute(
        """for item in sequencesE
            for v, e, p in 1..1 any item._id graph "ExtendedAndEdges"
                filter contains(item.sequence, @fragment)
                return p""",
        bind_vars={'fragment': fragment}
    )

    inter = [doc for doc in cursor]

    # for x in inter:
    #     print(x)

    with open(f"./json_data/{filename}.json", "w") as outfile:
        json.dump(inter, outfile)