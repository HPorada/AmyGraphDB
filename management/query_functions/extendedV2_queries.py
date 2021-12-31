import json


def filter_questions_extendedV2(database, q1, q2, q3, filename="result"):
    q1 = "question1/" + q1.replace(".", "").replace(",", "").replace(";", "").replace(" ", "_")
    q2 = "question2/" + q2.replace(".", "").replace(",", "").replace(";", "").replace(" ", "_")
    q3 = "question3/" + q3.replace(".", "").replace(",", "").replace(";", "").replace(" ", "_")

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

    inter = [doc for doc in cursor]

    with open(f"./management/json_data/{filename}.json", "w") as outfile:
        json.dump(inter, outfile)


def contains_fragment_extendedV2(database, fragment, filename="result"):
    cursor = database.aql.execute(
        """for item in sequencesE
            for v, e, p in 1..1 any item._id graph "ExtendedV2"
                filter contains(item.sequence, @fragment)
                return p""",
        bind_vars={'fragment': fragment}
    )

    inter = [doc for doc in cursor]

    with open(f"./management/json_data/{filename}.json", "w") as outfile:
        json.dump(inter, outfile)


def search_phrase_extendedV2(database, keyword, filename="result"):
    cursor = database.aql.execute(
        """
        let items = (
            for i in extendedV2View 
                search phrase(i.general_remarks, @keyword, 'text_en') 
                return i
        )

        for item in items
            for v, e, p in 1..1 any item._id graph "ExtendedV2"
                return p""",
        bind_vars={'keyword': keyword}
    )

    inter = [doc for doc in cursor]

    with open(f"./management/json_data/{filename}.json", "w") as outfile:
        json.dump(inter, outfile)

# def search_connected_extendedV2(database, collection, start, filename="result"):
#     ()
