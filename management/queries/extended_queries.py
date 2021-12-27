import json


def filter_extended(database, q1, q2, q3, filename="result"):
    aql = database.aql

    cursor = database.aql.execute(
        """for item in interactionsE
            for v, e, p in 1..1 any item._id graph "Extended"
                filter item.question_1 == @q1
                filter item.question_2 == @q2
                filter item.question_3 == @q3
                return p""",
        bind_vars={'q1': q1, 'q2': q2, 'q3': q3}
    )

    inter = [doc for doc in cursor]

    # for x in inter:
    #     print(x)

    with open(f"./management/json_data/{filename}.json", "w") as outfile:
        json.dump(inter, outfile)


def contains_extended(database, fragment, filename="result"):
    aql = database.aql

    cursor = database.aql.execute(
        """for item in sequencesE
            for v, e, p in 1..1 any item._id graph "Extended"
                filter contains(item.sequence, @fragment)
                return p""",
        bind_vars={'fragment': fragment}
    )

    inter = [doc for doc in cursor]

    # for x in inter:
    #     print(x)

    with open(f"./management/json_data/{filename}.json", "w") as outfile:
        json.dump(inter, outfile)